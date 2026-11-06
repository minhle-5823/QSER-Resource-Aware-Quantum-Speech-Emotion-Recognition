#!/usr/bin/env python3
"""Display paper-reported best Macro-F1 scores (not raw result recomputation)."""
from pathlib import Path
import csv

path = Path(__file__).resolve().parents[1] / 'results/paper_tables/table3_binary_robustness.csv'
with path.open(newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
print('PDCAT 2026 QSER: best binary Macro-F1 from manuscript Table 3')
print(f'{"Model":<15} {"k":>3} {"Macro-F1":>10} {"SD":>9}  Configuration')
print('-' * 76)
for row in rows:
    print(f'{row["model_family"]:<15} {row["feature_budget_k"]:>3} '
          f'{float(row["macro_f1_mean"]):>10.3f} {float(row["macro_f1_sd"]):>9.3f}  '
          f'{row["best_configuration"]}')
print('\nValues manually transcribed from accepted manuscript; not recalculated.')
