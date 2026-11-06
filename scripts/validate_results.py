#!/usr/bin/env python3
"""Check only the bundled research tables; does NOT rerun QML experiments."""
from pathlib import Path
import csv
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    'results/paper_tables/table3_binary_robustness.csv': {'model_family', 'feature_budget_k', 'macro_f1_mean', 'seeds'},
    'results/paper_tables/table4_nested_qubo.csv': {'model', 'feature_budget_k', 'holm_adjusted_p'},
    'results/paper_tables/table5_stress_and_eight_class.csv': {'experiment', 'macro_f1_mean', 'seeds'},
    'results/paper_tables/table6a_cross_corpus.csv': {'model', 'ravdess_selector', 'cmu_mosei_selector'},
    'results/paper_tables/table6b_hardware_noise.csv': {'model', 'noise_delta_macro_f1'},
    'results/paper_tables/table6b_circuit_variants.csv': {'model', 'circuit_variant'},
}


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as fh:
        reader = csv.DictReader(fh)
        return reader.fieldnames or [], list(reader)


def validate():
    n = 0
    for rel, required_cols in REQUIRED.items():
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f'Missing paper table: {rel}')
        header, rows = read_csv(path)
        if missing := required_cols.difference(header):
            raise ValueError(f'Missing columns {sorted(missing)} in {rel}')
        if not rows:
            raise ValueError(f'Empty table: {rel}')
        for r in rows:
            for c in ('macro_f1_mean', 'fixed_macro_f1', 'tuned_macro_f1', 'ravdess_macro_f1', 'cmu_mosei_macro_f1'):
                if c in r and r[c] and not 0 <= float(r[c]) <= 1:
                    raise ValueError(f'Out-of-range {c} in {rel}: {r[c]}')
        n += len(rows)

    inventory, items = read_csv(ROOT / 'docs/SOURCE_INVENTORY.csv')
    for row in items:
        p = ROOT / row['repository_path']
        if not p.is_file():
            raise ValueError(f'Missing source data: {p}')
        content = p.read_bytes()
        if hashlib.sha256(content).hexdigest() != row['sha256']:
            raise ValueError(f'Checksum mismatch: {p}')
    print(f'OK: {len(REQUIRED)} paper tables ({n} rows), {len(items)} original CSV/JSON artifacts verified.')
    print('Note: checks verify packaged-file integrity, not scientific reproduction.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(validate())
    except (ValueError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
