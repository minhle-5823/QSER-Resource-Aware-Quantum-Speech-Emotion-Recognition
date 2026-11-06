#!/usr/bin/env python3
"""Plot manually transcribed Table 3, not an experimental training script."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
rows = pd.read_csv(ROOT / 'results/paper_tables/table3_binary_robustness.csv')
models = ['QSVC', 'VQC', 'QCNN-like', 'Classical']
ks = [4, 8]
fig, ax = plt.subplots(figsize=(9, 5.4))
width = 0.35
for i, model in enumerate(models):
    data = rows[rows.model_family == model].sort_values('feature_budget_k')
    x = [j + (i - 1.5) * (width / 2) for j in range(len(ks))]
    ax.bar(x, data['macro_f1_mean'], width / 2, label=model,
           yerr=data['macro_f1_sd'], capsize=3)
ax.set_xticks(range(len(ks)), [f'k = {k}' for k in ks])
ax.set_ylim(0, 1.0)
ax.set_ylabel('Macro-F1 (mean ± sample SD)')
ax.set_title('Best reported binary configurations by feature budget (10 seeds)')
ax.legend(ncol=4, loc='upper center', bbox_to_anchor=(0.5, -0.12), frameon=False)
ax.grid(axis='y', alpha=0.25)
fig.tight_layout()
out = ROOT / 'figures/generated/table3_macro_f1.png'
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=180)
plt.close(fig)
print(f'Saved {out.relative_to(ROOT)}')
print('Source: manual Table 3 transcription, not a rerun of the experiment.')
