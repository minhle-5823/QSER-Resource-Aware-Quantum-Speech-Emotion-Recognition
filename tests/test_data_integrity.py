"""Lightweight tests over paper-reported CSV tables."""
import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    with (ROOT / 'results/paper_tables' / name).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


class TestResearchTables(unittest.TestCase):
    def test_table3_has_all_model_budget_pairs(self):
        rows = read('table3_binary_robustness.csv')
        self.assertEqual(len(rows), 8)
        self.assertEqual(set((r['model_family'], r['feature_budget_k']) for r in rows),
                         set((m, k) for m in ('QSVC', 'VQC', 'QCNN-like', 'Classical') for k in ('4', '8')))

    def test_table4_holm_correction_not_significant(self):
        rows = read('table4_nested_qubo.csv')
        self.assertEqual(len(rows), 4)
        self.assertTrue(all(float(r['holm_adjusted_p']) >= 0.05 for r in rows))

    def test_cross_corpus_matching_selectors_exactly_one(self):
        rows = read('table6a_cross_corpus.csv')
        self.assertEqual(sum(r['ravdess_selector'] == r['cmu_mosei_selector'] for r in rows), 1)

    def test_figure_files(self):
        for n in ('figure1_workflow.png', 'figure2_selector_architecture.png',
                  'figure3_qubo_and_stability.png', 'figure4_simulator_scaling.png'):
            self.assertTrue((ROOT / 'figures' / n).is_file())


if __name__ == '__main__':
    unittest.main()
