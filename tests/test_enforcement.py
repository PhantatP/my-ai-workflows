import json
import subprocess
import sys
from pathlib import Path

import pytest

from workflow.enforcement.core import scan

ROOT = Path(__file__).resolve().parents[1]
ENFORCER = ROOT / "workflow" / "bin" / "enforce-operation"
CHANGE_SET_SCANNER = ROOT / "workflow" / "bin" / "scan-change-set"

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

@pytest.mark.parametrize("command", ["echo safe\nterraform destroy", "echo $(terraform destroy)", "echo `terraform destroy`", "echo <(terraform destroy)", "sh -c 'terraform destroy'", "eval 'terraform destroy'", "env FOO=1 terraform destroy"])
def test_shell_evaluated_commands_are_conservatively_sensitive(command):
    assert "shell_evaluated_command" in {item["id"] for item in scan(command=command)["triggers"]}

@pytest.mark.parametrize("command", ["command terraform destroy", "nice terraform destroy"])
def test_command_modifiers_do_not_hide_destructive_operations(command):
    assert "destructive_operation" in {item["id"] for item in scan(command=command)["triggers"]}

@pytest.mark.parametrize("path", [".env", ".env.production"])
def test_root_dotenv_paths_match(path):
    assert "secrets_or_security_configuration" in {item["id"] for item in scan([path])["triggers"]}

def test_intended_path_scanner_mechanically_writes_activation_log(tmp_path):
    scanner = ROOT / "workflow" / "bin" / "scan-triggers"
    subprocess.run([sys.executable, scanner, "--intended-path", "src/auth/session.ts", "--log-root", tmp_path], check=True)
    assert "trigger: authentication_sensitive(src/auth/session.ts)" in (tmp_path / ".workflow" / "log.txt").read_text(encoding="utf-8")

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

@pytest.mark.parametrize("scanner_body", ["raise SystemExit(1)", "print('{\"triggers\": [{\"id\": \"production_sensitive_operation\"}]}')"])
def test_sensitive_enforcement_fails_closed_on_scanner_error(tmp_path, scanner_body):
    fake_scanner = tmp_path / "scanner.py"
    fake_scanner.write_text(scanner_body, encoding="utf-8")
    result = subprocess.run([sys.executable, ENFORCER, "--command", "terraform apply", "--scanner", fake_scanner, "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 3

def test_shared_guard_cannot_self_approve_a_destructive_command(tmp_path):
    result = subprocess.run([sys.executable, ENFORCER, "--command", "git push -f origin main", "--log-root", tmp_path], capture_output=True, text=True)
    assert json.loads(result.stdout)["decision"] == "deny"

@pytest.mark.parametrize("command", ["echo `terraform destroy`", "eval 'terraform destroy'", "command terraform destroy"])
def test_guard_denies_shell_forms_that_would_execute_sensitive_commands(tmp_path, command):
    result = subprocess.run([sys.executable, ENFORCER, "--command", command, "--log-root", tmp_path], capture_output=True, text=True)
    assert result.returncode == 2
