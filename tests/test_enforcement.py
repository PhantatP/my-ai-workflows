import json
import subprocess
import sys
from pathlib import Path

import pytest

from workflow.enforcement.core import scan

ROOT = Path(__file__).resolve().parents[1]
ENFORCER = ROOT / "workflow" / "bin" / "enforce-operation"
CHANGE_SET_SCANNER = ROOT / "workflow" / "bin" / "scan-change-set"
CLAUDE_HOOK = ROOT / ".claude" / "hooks" / "pre_tool_use.py"

@pytest.mark.parametrize("path", ["authors.md", "src/author.ts", "src/useAuthorList.tsx", "AUTHORS"])
def test_author_paths_do_not_match_authentication(path):
    assert "authentication_sensitive" not in {item["id"] for item in scan([path])["triggers"]}

@pytest.mark.parametrize("path", ["src/auth/session.ts", "lib/permissions.ts", "src/rbac/roles.ts", "src/oauth/client.ts"])
def test_explicit_authentication_paths_match(path):
    assert "authentication_sensitive" in {item["id"] for item in scan([path])["triggers"]}

@pytest.mark.parametrize("path", ["schemas/user.zod.ts", "src/validation/schema.ts"])
def test_generic_schema_paths_do_not_match_database(path):
    assert not {item["id"] for item in scan([path])["triggers"]} & {"database_migration", "database_schema"}

@pytest.mark.parametrize("path, trigger", [("migrations/0012_add_user.sql", "database_migration"), ("db/migrations/20260812_users.sql", "database_migration"), ("alembic/versions/0012_users.py", "database_migration"), ("supabase/migrations/20260812_users.sql", "database_migration"), ("prisma/schema.prisma", "database_schema"), ("db/schema.ts", "database_schema")])
def test_database_artifacts_match(path, trigger):
    assert trigger in {item["id"] for item in scan([path])["triggers"]}

@pytest.mark.parametrize("path, trigger", [("package.json", "dependency_or_lockfile"), ("infra/main.tf", "production_or_infrastructure"), ("deploy/prod.yaml", "production_or_infrastructure"), ("openapi.yaml", "public_api_or_protocol"), ("contracts/user.proto", "public_api_or_protocol")])
def test_other_sensitive_artifacts_match(path, trigger):
    assert trigger in {item["id"] for item in scan([path])["triggers"]}

@pytest.mark.parametrize("command", ["rm -rf /some/path", "git push --force origin main", "git push -f origin main", "terraform destroy", "kubectl delete deployment api", "DROP TABLE users", "TRUNCATE TABLE users"])
def test_destructive_commands_match_only_as_commands(command):
    assert "destructive_operation" in {item["id"] for item in scan(command=command)["triggers"]}

def test_prose_is_not_scanned_as_an_executable_command():
    assert scan(command="Documentation: never run `terraform destroy` in production.")["mechanical_floor"] == 0

@pytest.mark.parametrize("command", ["Documentation:; terraform destroy", "Documentation: && terraform destroy", "Documentation: `terraform destroy`"])
def test_documentation_prefix_cannot_hide_an_executable_command(command):
    assert scan(command=command)["mechanical_floor"] == 3

@pytest.mark.parametrize("command", ["echo safe && terraform destroy", "cd /tmp; terraform destroy", "rm -r -f /some/path", "git -c foo=bar push --force origin main"])
def test_destructive_command_segments_and_variants_are_detected(command):
    assert "destructive_operation" in {item["id"] for item in scan(command=command)["triggers"]}

@pytest.mark.parametrize("command", ["echo $(terraform destroy)", "echo `terraform destroy`", "echo <(terraform destroy)", "sh -c 'terraform destroy'", "bash -c 'terraform destroy'", "eval 'terraform destroy'"])
def test_shell_evaluated_commands_are_conservatively_sensitive(command):
    assert "shell_evaluated_command" in {item["id"] for item in scan(command=command)["triggers"]}

@pytest.mark.parametrize("command", ["echo hello\npytest", "FOO=test pytest", "env FOO=test pytest", "bash script.sh"])
def test_ordinary_shell_forms_are_not_automatically_sensitive(command):
    assert scan(command=command)["mechanical_floor"] == 0

@pytest.mark.parametrize("command", ["command terraform destroy", "nice terraform destroy"])
def test_command_modifiers_do_not_hide_destructive_operations(command):
    assert "destructive_operation" in {item["id"] for item in scan(command=command)["triggers"]}

@pytest.mark.parametrize("command", ["sudo terraform destroy", "sudo -u root terraform destroy", "sudo --user root git push --force origin main", "timeout 5 terraform destroy", "timeout -k 1 5 terraform destroy", "timeout -s KILL 5 terraform destroy", "command -p terraform destroy", "env -i terraform destroy", "env -u PATH terraform destroy", "env -C /tmp terraform destroy", "FOO=test terraform destroy"])
def test_safe_wrappers_do_not_hide_destructive_operations(command):
    assert "destructive_operation" in {item["id"] for item in scan(command=command)["triggers"]}

@pytest.mark.parametrize("command", ["echo hello\npytest", "FOO=test pytest", "env FOO=test pytest", "bash script.sh"])
def test_guard_allows_ordinary_shell_forms(tmp_path, command):
    result = subprocess.run([sys.executable, ENFORCER, "--command", command, "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 0

@pytest.mark.parametrize("path", [".env", ".env.production"])
def test_root_dotenv_paths_match(path):
    assert "secrets_or_security_configuration" in {item["id"] for item in scan([path])["triggers"]}

def test_intended_path_scanner_mechanically_writes_activation_log(tmp_path):
    scanner = ROOT / "workflow" / "bin" / "scan-triggers"
    subprocess.run([sys.executable, scanner, "--intended-path", "src/auth/session.ts", "--log-root", tmp_path], check=True)
    assert "trigger: authentication_sensitive(src/auth/session.ts)" in (tmp_path / ".workflow" / "log.txt").read_text(encoding="utf-8")

def test_command_scanner_log_uses_signature_instead_of_raw_command(tmp_path):
    scanner = ROOT / "workflow" / "bin" / "scan-triggers"
    command = "terraform destroy --token TOPSECRET"
    result = subprocess.run([sys.executable, scanner, "--command", command, "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 0
    log = (tmp_path / ".workflow" / "log.txt").read_text(encoding="utf-8")
    assert "trigger: destructive_operation(terraform_destroy)" in log
    assert command not in log
    assert "TOPSECRET" not in log

def test_actual_change_set_rescans_undeclared_sensitive_path():
    initial = scan(["src/ui/button.tsx"])
    actual = scan(["src/ui/button.tsx", "src/auth/session.ts"])
    assert initial["mechanical_floor"] < actual["mechanical_floor"] == 3

def test_actual_change_set_scanner_detects_an_untracked_sensitive_edit(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / "README.md").write_text("base", encoding="utf-8")
    subprocess.run(["git", "add", "README.md"], cwd=tmp_path, check=True)
    subprocess.run(["git", "-c", "user.name=test", "-c", "user.email=test@example.invalid", "commit", "-qm", "base"], cwd=tmp_path, check=True)
    target = tmp_path / "src" / "auth"
    target.mkdir(parents=True)
    (target / "session.ts").write_text("export {}", encoding="utf-8")
    result = subprocess.run([sys.executable, CHANGE_SET_SCANNER], cwd=tmp_path, capture_output=True, text=True, check=True)
    assert "authentication_sensitive" in {item["id"] for item in json.loads(result.stdout)["triggers"]}
    assert "trigger: authentication_sensitive(src/auth/session.ts)" in (tmp_path / ".workflow" / "log.txt").read_text(encoding="utf-8")

def test_actual_change_set_scanner_works_before_first_commit_and_finds_ignored_env(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / ".gitignore").write_text(".env\n", encoding="utf-8")
    (tmp_path / ".env").write_text("KEY=value", encoding="utf-8")
    result = subprocess.run([sys.executable, CHANGE_SET_SCANNER], cwd=tmp_path, capture_output=True, text=True, check=True)
    assert "secrets_or_security_configuration" in {item["id"] for item in json.loads(result.stdout)["triggers"]}

def test_destructive_command_is_denied_and_mechanism_writes_log(tmp_path):
    result = subprocess.run([sys.executable, ENFORCER, "--command", "terraform destroy", "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 2
    assert "DENIED: destructive_operation" in (tmp_path / ".workflow" / "log.txt").read_text(encoding="utf-8")

def test_operational_log_contains_v23_routing_fields(tmp_path):
    result = subprocess.run([sys.executable, ENFORCER, "--command", "terraform destroy", "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 2
    log = (tmp_path / ".workflow" / "log.txt").read_text(encoding="utf-8")
    assert "platform=unknown" in log
    assert "domain=BUILD" in log
    assert "level_after=L3" in log
    assert "assurance_state=NORMAL" in log

def test_sensitive_command_log_does_not_store_raw_command_or_secret(tmp_path):
    command = "terraform destroy --token TOPSECRET"
    result = subprocess.run([sys.executable, ENFORCER, "--command", command, "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 2
    log = (tmp_path / ".workflow" / "log.txt").read_text(encoding="utf-8")
    assert command not in log
    assert "TOPSECRET" not in log

def test_cli_platform_is_recorded_in_operational_log(tmp_path):
    scanner = ROOT / "workflow" / "bin" / "scan-triggers"
    result = subprocess.run([sys.executable, scanner, "--intended-path", "src/auth/session.ts", "--log-root", tmp_path, "--platform", "codex"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "platform=codex" in (tmp_path / ".workflow" / "log.txt").read_text(encoding="utf-8")

@pytest.mark.parametrize("scanner_body", ["raise SystemExit(1)", "print('{\"triggers\": [{\"id\": \"production_sensitive_operation\"}]}')"])
def test_sensitive_enforcement_fails_closed_on_scanner_error(tmp_path, scanner_body):
    fake_scanner = tmp_path / "scanner.py"
    fake_scanner.write_text(scanner_body, encoding="utf-8")
    result = subprocess.run([sys.executable, ENFORCER, "--command", "terraform apply", "--scanner", fake_scanner, "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 3

def test_scanner_failure_log_does_not_store_scanner_stderr(tmp_path):
    fake_scanner = tmp_path / "scanner.py"
    fake_scanner.write_text("import sys\nprint('TOPSECRET', file=sys.stderr)\nraise SystemExit(1)", encoding="utf-8")
    result = subprocess.run([sys.executable, ENFORCER, "--command", "terraform apply", "--scanner", fake_scanner, "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 3
    log = (tmp_path / ".workflow" / "log.txt").read_text(encoding="utf-8")
    assert "TOPSECRET" not in log
    assert "reason=RuntimeError" in log

def test_shared_guard_cannot_self_approve_a_destructive_command(tmp_path):
    result = subprocess.run([sys.executable, ENFORCER, "--command", "git push -f origin main", "--log-root", tmp_path], capture_output=True, text=True)
    assert json.loads(result.stdout)["decision"] == "deny"

def test_claude_hook_denies_and_logs_malformed_payload():
    result = subprocess.run([sys.executable, CLAUDE_HOOK], input="not json", capture_output=True, text=True)
    assert result.returncode == 2
    event = (ROOT / ".workflow" / "log.txt").read_text(encoding="utf-8").splitlines()[-1]
    assert "malformed hook payload" in event
    assert "platform=claude_code" in event
    assert "not json" not in event

@pytest.mark.parametrize("payload", ['{"tool_name":"Bash","tool_input":"not-an-object"}', '{"tool_name":"Bash","tool_input":{"command":3}}'])
def test_claude_hook_denies_malformed_bash_shapes(payload):
    result = subprocess.run([sys.executable, CLAUDE_HOOK], input=payload, capture_output=True, text=True)
    assert result.returncode == 2

@pytest.mark.parametrize("command", ["printf '%s' 'x; terraform destroy'", "printf '%s' 'x|terraform destroy'"])
def test_quoted_list_separators_do_not_create_false_commands(command):
    assert scan(command=command)["mechanical_floor"] == 0

@pytest.mark.parametrize("command", ["echo `terraform destroy`", "eval 'terraform destroy'", "command terraform destroy"])
def test_guard_denies_shell_forms_that_would_execute_sensitive_commands(tmp_path, command):
    result = subprocess.run([sys.executable, ENFORCER, "--command", command, "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 2
