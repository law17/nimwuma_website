#!/usr/bin/env bash
set -euo pipefail

MESSAGE="${*:-Update website}"

if [ ! -d ".git" ]; then
  echo "This directory is not a Git repository. Use scripts/first_push.sh first." >&2
  exit 1
fi

python3 scripts/check_site.py

git add .
if git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

git commit -m "$MESSAGE"
git push
