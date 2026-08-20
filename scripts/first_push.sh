#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${1:-https://github.com/law17/nimwuma_website.git}"

if [ ! -f "_config.yml" ] || [ ! -d "_data" ]; then
  echo "Run this script from the root of the website repository." >&2
  exit 1
fi

python3 scripts/check_site.py

git init -b main 2>/dev/null || true

git add .
if ! git diff --cached --quiet; then
  git commit -m "Initial website"
fi

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REPO_URL"
else
  git remote add origin "$REPO_URL"
fi

echo
printf 'Repository prepared. Pushing to: %s\n' "$REPO_URL"
git push -u origin main

echo
cat <<'MSG'
Push complete.
In GitHub, open Settings > Pages and set Source to GitHub Actions if it is not already selected.
Then watch the Actions tab for the Pages deployment workflow.
MSG
