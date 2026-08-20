#!/usr/bin/env python3
"""Lightweight architecture checks for the Jekyll site.

Uses only the Python standard library so it can run in GitHub Actions.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
COMPANY = ROOT / "_data" / "company.yml"

text = COMPANY.read_text(encoding="utf-8")
match = re.search(r'^\s{2}name:\s*["\']?([^"\'\n]+)', text, flags=re.MULTILINE)
if not match:
    print("ERROR: Could not determine brand name from _data/company.yml")
    sys.exit(1)
brand = match.group(1).strip()

allowed_brand_files = {COMPANY.resolve()}
text_suffixes = {".html", ".md", ".yml", ".yaml", ".js", ".css", ".xml", ".txt"}
violations = []
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.resolve() in allowed_brand_files:
        continue
    if path.suffix.lower() not in text_suffixes and path.name != "robots.txt":
        continue
    data = path.read_text(encoding="utf-8", errors="ignore")
    if brand in data:
        violations.append(path.relative_to(ROOT))

required = [
    "index.html",
    "_includes/header.html",
    "_includes/footer.html",
    "_data/company.yml",
    "_data/pricing.yml",
    "privacy/index.md",
    "terms/index.md",
    "security/index.md",
]
missing = [p for p in required if not (ROOT / p).exists()]

if violations:
    print("ERROR: Hard-coded brand name found outside _data/company.yml:")
    for p in violations:
        print(f"  - {p}")
if missing:
    print("ERROR: Required site files are missing:")
    for p in missing:
        print(f"  - {p}")
if violations or missing:
    sys.exit(1)

print(f"Site architecture check passed for brand: {brand}")
