# Upload this folder to a new GitHub repository

## Recommended initial visibility: **Private**

The paper is accepted at PDCAT 2026 but the conference presentation and publisher release are still pending. Before sharing publicly, obtain coauthor permission and check self-archiving terms.

1. Sign in to GitHub and visit https://github.com/new.
2. Name the repository **`QSER-PDCAT2026`** (or `resource-aware-quantum-ser`).
3. Suggested description: `Research artifacts for an accepted PDCAT 2026 paper on resource-aware quantum speech emotion recognition (QSVC, VQC, QCNN-like, QUBO).`
4. Select **Private**. Don't initialize with a README/license/gitignore because these files are already included.
5. Extract this ZIP on your computer, open a terminal in the **`QSER-PDCAT2026`** folder, then run (replace `YOUR_GITHUB_USERNAME`):

```bash
git init
git add .
git commit -m "Initial QSER PDCAT 2026 research artifacts"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/QSER-PDCAT2026.git
git push -u origin main
```

If `git commit` asks for author identity, set your Git username/email locally. For HTTPS authentication, GitHub uses a credential manager or personal access token rather than an account password. GitHub Desktop can also publish the folder without commands.

## Before switching to Public

Review `docs/RELEASE_CHECKLIST.md`. The repository currently contains **result analysis tools and curated data**, not the original experiment training code. Add code/notebooks separately after verifying the final camera-ready version and publisher policy.
