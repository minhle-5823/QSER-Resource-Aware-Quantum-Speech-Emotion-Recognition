# Reproducibility and public-release scope

This public repository **is not an end-to-end experimental reproduction package**. The author-provided archive did not contain original `.py` model-training code or `.ipynb` notebooks. This public version also excludes all unpublished raw experiment results and local configurations.

What can be done with the included files:
- Inspect and validate six manually transcribed summary CSV tables from the accepted paper.
- Print the main Macro-F1 comparison using `scripts/show_summary.py`.
- Replot the summary using `scripts/plot_paper_results.py`.

What cannot be done:
- Repeat feature extraction from RAVDESS/CMU-MOSEI audio.
- Train QSVC/VQC/QCNN-like models, reselect features or rerun tuning.
- Independently reproduce or audit all ten-seed and five-seed experiments.

**Important:** The included values are manuscript transcriptions, not recalculated results. Classically simulated quantum circuits must not be presented as quantum hardware experiments.

To release a full reproduction package in the future, obtain original experiment code, verify all dependencies/data licenses, and scan for credentials and sensitive data before publishing.
