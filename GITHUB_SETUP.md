# Publish the public QSER repository on GitHub

This folder is the **public-safe research overview package**, not the full internal experiment archive.

1. Open https://github.com/new and name it `QSER-PDCAT2026`.
2. Choose **Public**. Do not add a GitHub README, `.gitignore`, or license during creation; they are already managed here (no software license has been granted yet).
3. Extract the ZIP and open a terminal inside `QSER-PDCAT2026-PUBLIC`.
4. Replace `YOUR_GITHUB_USERNAME` below with your own:

```bash
git init
git add .
git commit -m "Publish QSER PDCAT 2026 research overview"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/QSER-PDCAT2026.git
git push -u origin main
```

This ZIP excludes the manuscript PDF, original manuscript figures, private acceptance proof, raw experiment CSVs, local configs and original dataset assets.

**Before publishing:** confirm public-release permission with the other authors, including for the selected manuscript-derived tables and summary chart. The work is accepted, not published; add the official Springer DOI only after publication.
