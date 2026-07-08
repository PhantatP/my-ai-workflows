#!/usr/bin/env python3
"""
Generate upgraded HTML graph visualization from graph.json.

Usage:
    python generate_viz.py <graph_json> <output_html> <template_html> [community_labels_json]
"""

import sys
import json
import math
from pathlib import Path

PALETTE = [
    '#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F',
    '#EDC948', '#B07AA1', '#FF9DA7', '#9C755F', '#BAB0AC',
    '#86BCB6', '#D4A6C8', '#8CD17D', '#B6992D', '#499894',
    '#F1CE63', '#FABFD2', '#D7B5A6', '#79706E', '#D37295'
]


def load_graph(graph_path):
    """Load networkx node-link format graph."""
    with open(graph_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_community_labels(labels_path):
    """Load community labels if provided."""
    if not labels_path or not Path(labels_path).exists():
        return {}
    with open(labels_path, 'r', encoding='utf-8') as f:
        raw = json.load(f)
        return {int(k): v for k, v in raw.items()}


def compute_degree(nodes, links):
    """Compute degree for each node."""
    degree = {}
    for link in links:
        src = link['source']
        tgt = link['target']
        degree[src] = degree.get(src, 0) + 1
        degree[tgt] = degree.get(tgt, 0) + 1
    return degree


def convert_nodes(nodes, links, community_labels):
    """Convert nodes to vis.js format with community colors."""
    degree = compute_degree(nodes, links)

    # Group nodes by community and sort by size desc
    communities = {}
    for n in nodes:
        cid = n.get('community', 0)
        if cid not in communities:
            communities[cid] = []
        communities[cid].append(n)

    sorted_cids = sorted(communities.keys(), key=lambda c: len(communities[c]), reverse=True)

    # Assign colors
    cid_to_color = {}
    for i, cid in enumerate(sorted_cids):
        cid_to_color[cid] = PALETTE[i % len(PALETTE)]

    vis_nodes = []
    for n in nodes:
        cid = n.get('community', 0)
        color = cid_to_color.get(cid, PALETTE[0])
        community_label = community_labels.get(cid, f'Community {cid}')

        vis_nodes.append({
            'id': n['id'],
            'label': n.get('label', n['id']),
            'color': {
                'background': color,
                'border': color,
                'highlight': {
                    'background': color,
                    'border': '#ffffff'
                }
            },
            'size': 6 + math.sqrt(max(0, degree.get(n['id'], 0))) * 3.5,
            'font': {
                'color': '#e6edf3',
                'size': 11,
                'face': 'Segoe UI, system-ui, sans-serif'
            },
            '_file_type': n.get('file_type', ''),
            '_community_name': community_label,
            '_community_id': cid,
            '_source_file': n.get('source_file', ''),
            '_degree': degree.get(n['id'], 0),
            'community': cid,
        })

    return vis_nodes, cid_to_color, communities


def convert_edges(links):
    """Convert edges to vis.js format."""
    vis_edges = []
    for i, link in enumerate(links):
        relation = link.get('relation', '')
        confidence = link.get('confidence', '')
        score = link.get('confidence_score', 0.0)
        dashed = confidence != 'EXTRACTED'

        title = f"{relation} [{confidence} {score:.2f}]" if relation else confidence

        vis_edges.append({
            'id': i,
            'from': link['source'],
            'to': link['target'],
            'title': title,
            'relation': relation,
            'confidence': confidence,
            'confidence_score': score,
            'dashes': dashed,
            'width': 0.5 + link.get('weight', 1.0),
            'color': {
                'color': '#3a3f4b',
                'highlight': '#58a6ff',
                'hover': '#58a6ff',
                'opacity': 0.6 if dashed else 0.85
            }
        })

    return vis_edges


def build_legend(communities, cid_to_color, community_labels):
    """Build legend sorted by community size desc."""
    sorted_cids = sorted(communities.keys(), key=lambda c: len(communities[c]), reverse=True)

    legend = []
    for cid in sorted_cids:
        legend.append({
            'cid': cid,
            'label': community_labels.get(cid, f'Community {cid}'),
            'color': cid_to_color[cid],
            'count': len(communities[cid])
        })

    return legend


def generate_html(graph_data, template_path, output_path, community_labels):
    """Generate HTML from template with injected data."""
    nodes = graph_data['nodes']
    links = graph_data['links']
    hyperedges = graph_data.get('graph', {}).get('hyperedges', [])

    vis_nodes, cid_to_color, communities = convert_nodes(nodes, links, community_labels)
    vis_edges = convert_edges(links)
    legend = build_legend(communities, cid_to_color, community_labels)

    stats = f"{len(nodes)} nodes · {len(links)} edges · {len(communities)} communities"
    title = Path(output_path).parent.parent.name

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    html = template \
        .replace('__RAW_NODES__', json.dumps(vis_nodes)) \
        .replace('__RAW_EDGES__', json.dumps(vis_edges)) \
        .replace('__LEGEND__', json.dumps(legend)) \
        .replace('__HYPEREDGES__', json.dumps(hyperedges)) \
        .replace('__STATS__', stats) \
        .replace('__TITLE__', title)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return len(vis_nodes), len(vis_edges)


def main():
    if len(sys.argv) < 4:
        print("Usage: python generate_viz.py <graph_json> <output_html> <template_html> [community_labels_json]")
        sys.exit(1)

    graph_path = sys.argv[1]
    output_path = sys.argv[2]
    template_path = sys.argv[3]
    labels_path = sys.argv[4] if len(sys.argv) > 4 else None

    if not Path(graph_path).exists():
        print(f"Error: graph.json not found at {graph_path}")
        sys.exit(1)

    if not Path(template_path).exists():
        print(f"Error: template not found at {template_path}")
        sys.exit(1)

    graph_data = load_graph(graph_path)
    community_labels = load_community_labels(labels_path)

    node_count, edge_count = generate_html(graph_data, template_path, output_path, community_labels)

    print(f"Generated {output_path}")
    print(f"  {node_count} nodes, {edge_count} edges")


if __name__ == '__main__':
    main()
