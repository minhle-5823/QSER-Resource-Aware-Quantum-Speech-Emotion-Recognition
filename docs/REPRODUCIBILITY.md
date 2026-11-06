# Reproducibility and scope

## What was actually supplied

The uploaded ZIP contained an accepted manuscript PDF, manuscript figures, evidence screenshots, aggregate CSV/JSON tables, feature caches and many nested ZIP bundles. **No `.py` experiment source file or `.ipynb` notebook was present**, including inside the nested experiment ZIPs inspected. The available CSV files are also not uniformly complete with respect to the 10-seed primary evaluation and five-seed revision tiers described in the manuscript.

## What this repository can do now

- Read and validate selected **unchanged** supplied CSV/JSON outputs under `results/supplied`.
- Show paper-reported Tables 3–6 transcribed into CSV under `results/paper_tables`.
- Draw an additional chart using the paper-reported Macro-F1 values.
- Describe the evaluation protocol, data access, interpretation and limitations.

## What it cannot yet do

- Rebuild the original 206-dimensional acoustic feature matrix from audio.
- Run the exact QSVC/VQC/QCNN-like training loops, hyperparameter tuning and statistical tests from the paper.
- Regenerate the full 10-seed/5-seed results from scratch, or independently verify those results against complete raw logs.

**Do not cite `results/paper_tables` as newly recomputed evidence.** Those files are paper transcriptions. Do not mix incomplete `results/supplied` summaries with the manuscript's full ten-seed summary.

## To make this an end-to-end reproducibility release

1. Obtain original Kaggle notebooks or Python source from the authors, ideally organized by primary quantum experiment, classical controls, QCNN, tuning, multiclass/cross-corpus and ablations.
2. Provide environment versions, stable dependency lockfile and deterministic seed setup.
3. Remove sensitive credentials, dataset mirrors and licensed raw media from tracked files.
4. Add the exact final logs/checkpoints or an externally hosted artifact archive, with checksums and a mapping to manuscript tables.
5. Write commands for feature extraction, experimental evaluation, result aggregation and figure reproduction, then test on a clean environment.
6. Verify copyright/author permissions and Springer self-archiving rules before changing the repo visibility.
