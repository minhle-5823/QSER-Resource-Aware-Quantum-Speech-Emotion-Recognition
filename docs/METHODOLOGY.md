# Methodology summary

This document summarizes the supplied **accepted manuscript**. It is not a claim that all its methods can currently be re-executed from this repository.

## Data and fixed acoustic representation

- RAVDESS: 1,440 deduplicated speech utterances from 24 actors for the main dataset.
- Audio: mono, 16 kHz; pad/crop to 4 seconds.
- Features (206 total): 26 MFCC, 26 delta-MFCC, 26 second-order delta-MFCC, 80 Mel-spectrogram, 24 Chroma, 10 spectral summary, 14 spectral contrast statistics.
- Primary task: binary **calm vs. happy**; main evaluation uses actor-disjoint splits.

## Evaluation design

**Robustness tier:** 10 outer random seeds: `7, 11, 23, 42, 101, 314, 777, 999, 2025, 2026`. Splits avoid actor overlap; training data only are used to fit scalers and feature selectors. Selected features are mapped to `[0, π]`. Main quantum training/test caps: 25/15 utterances **per class**.

**Stress tier:** `k = 16` quantum/QCNN with 3 outer seeds; not directly comparable in inferential strength with 10-seed main results. Classical controls retain 10 seeds in the manuscript.

**Additional evaluations:** 5-seed eight-class RAVDESS, six-emotion RAVDESS/CMU-MOSEI, hardware-derived noisy simulation, and circuit variants. These are descriptive tiers.

## Feature selection and QUBO

Five selector families are evaluated: Random, mutual information (MI), PCA loading, greedy mRMR and QUBO simulated annealing (SA). The QUBO optimization balances MI relevance, feature redundancy and cardinality, with **top-64 MI prefiltering** trained only on the outer training set. The fixed QUBO coefficients are α=1, β=0.5, γ=2 with 3,000 annealing iterations. A separate nested training-only 3-fold validation selects from 12 coefficient triples and is interpreted cautiously.

## Model families

| Family | Paper setup |
|---|---|
| QSVC | `ZZFeatureMap` (1 repetition, linear entanglement), fidelity kernel |
| VQC | `ZZFeatureMap` + `RealAmplitudes` (1 repetition), COBYLA up to 50 iterations |
| QCNN-like | PennyLane angle encoding, convolution/pooling-style layers; 30 epochs, batch size 16 |
| Classical | RBF SVM, linear SVM, logistic regression, random forest, MLP |

Classical controls use the **same selected and angle-scaled matrices** and appropriate matching sample caps.

## Statistics and limitations

Accuracy, Macro-F1, Weighted-F1, time and resources are recorded. Main 10-seed results include sample standard deviations and 95% t confidence intervals. Paired tests for QUBO tuning use Wilcoxon, Cohen's dz, and Holm correction. The five-seed ablations are descriptive. All quantum experiments are **classical simulations**; FakeBrisbane-derived noise models **do not mean execution on a physical quantum device**.

Read the accepted paper for exact model and ablation definitions. Beware that the supplied CSV subsets do not include the entire original 10-seed and five-seed result sets.
