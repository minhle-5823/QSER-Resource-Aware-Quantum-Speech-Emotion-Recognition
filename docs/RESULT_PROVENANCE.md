# Result provenance and caveats

There are **two fundamentally different** sources of tables in this repository:

1. `results/paper_tables/`: **manually transcribed** from the manuscript supplied in the upload (Tables 3–6). These are the paper's reported figures, not outputs of the included scripts.
2. `results/supplied/`: **byte-for-byte copied** CSV/JSON files selected from the original experiment ZIP. The original archive contained multiple nested ZIPs, repeated caches, plots and logs; this release selects representative *machine-readable* artifacts to avoid duplication. `docs/SOURCE_INVENTORY.csv` records each included file's original ZIP path, size and SHA-256.

## Important comparability warning

The supplied `quantum_partial` and `qcnn_partial` folders include **three-seed experiment subsets**, not necessarily the final 10-seed paper-report aggregates. They must not be interpreted as independent confirmations of manuscript Table 3. Likewise `stress_partial` contains only selected supplied partial files. Some `classical` data refer to different split modes or higher feature budgets and are not direct matches for the final manuscript comparison. Always filter by `split_mode`, seed count, feature budget, and task.

## Paper tables

| CSV | Source in supplied manuscript |
|---|---|
| `table3_binary_robustness.csv` | Table 3, best ten-seed configurations |
| `table4_nested_qubo.csv` | Table 4, fixed vs nested QUBO |
| `table5_stress_and_eight_class.csv` | Table 5, stress and eight-class |
| `table6a_cross_corpus.csv` | Table 6(a), RAVDESS vs CMU-MOSEI |
| `table6b_hardware_noise.csv` | Table 6(b), noise accuracy/F1 deltas for k=4 and k=8 |
| `table6b_circuit_variants.csv` | Table 6(b), all listed circuit variant deltas by k |

### Rounding

Paper tables report rounded values. Small arithmetic mismatches can arise when calculating differences from rounded means, and should not be used to challenge the recorded raw inferential results.

## Excluded on purpose

- Dataset audio, derived `.npy` feature caches and repeated heavy intermediates.
- Nested ZIP bundles and duplicated microbatch artifacts.
- Emails, acceptance proof screenshots, academic/course materials, internal comments.
- PDF manuscript (copyright/self-archiving policy not checked).
- Unverified training source code (none supplied).

No new quantum performance claim is derived from the data curation process.
