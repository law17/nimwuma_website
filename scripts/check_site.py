#!/usr/bin/env python3
"""Lightweight architecture and route checks for the Jekyll site.

Uses only the Python standard library so it can run in GitHub Actions before Jekyll builds.
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

errors = []
allowed_brand_files = {COMPANY.resolve()}
text_suffixes = {".html", ".md", ".yml", ".yaml", ".js", ".css", ".xml", ".txt"}
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.resolve() in allowed_brand_files:
        continue
    if path.suffix.lower() not in text_suffixes and path.name != "robots.txt":
        continue
    data = path.read_text(encoding="utf-8", errors="ignore")
    if brand in data:
        errors.append(f"Hard-coded brand name outside _data/company.yml: {path.relative_to(ROOT)}")

required = [
    "index.html",
    "_includes/header.html",
    "_includes/footer.html",
    "_data/company.yml",
    "_data/pricing.yml",
    "assets/css/main.css",
    "assets/js/main.js",
    "assets/images/brand-logo.png",
    "assets/images/favicon.png",
    "privacy/index.md",
    "terms/index.md",
    "security/index.md",
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"Required site file is missing: {rel}")

# Internal routes explicitly declared in YAML and Liquid relative_url calls.
routes = set()
url_pattern = re.compile(r'^\s*url:\s*["\']?(/[^"\'\n#]*)', flags=re.MULTILINE)
relative_pattern = re.compile(r"['\"](/[^'\"]+)['\"]\s*\|\s*relative_url")
asset_pattern = re.compile(r'^\s*(?:logo|favicon):\s*["\']?(/[^"\'\n#]+)', flags=re.MULTILINE)
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() not in text_suffixes and path.name != "robots.txt":
        continue
    data = path.read_text(encoding="utf-8", errors="ignore")
    routes.update(url_pattern.findall(data))
    routes.update(relative_pattern.findall(data))
    for asset in asset_pattern.findall(data):
        if not (ROOT / asset.lstrip("/")).exists():
            errors.append(f"Configured asset does not exist: {asset}")

# Map pretty routes to source files.
for route in sorted(routes):
    if not route.startswith("/") or "{{" in route:
        continue
    if route == "/":
        candidates = [ROOT / "index.html", ROOT / "index.md"]
    elif route.endswith("/"):
        rel = route.strip("/")
        candidates = [ROOT / rel / "index.html", ROOT / rel / "index.md"]
    else:
        rel = route.lstrip("/")
        candidates = [ROOT / rel, ROOT / f"{rel}.html", ROOT / f"{rel}.md"]
    if not any(c.exists() for c in candidates):
        errors.append(f"Internal route has no source page: {route}")

# Staging should not advertise an unconfirmed business mailbox as active.
staging_text = (ROOT / "_config.yml").read_text(encoding="utf-8")
staging = bool(re.search(r'^staging:\s*true\s*$', staging_text, flags=re.MULTILINE | re.IGNORECASE))
email_active = bool(re.search(r'^\s{2}email_active:\s*true\s*$', text, flags=re.MULTILINE | re.IGNORECASE))
if staging and email_active:
    errors.append("Staging is true but contact.email_active is also true. Confirm mailbox before enabling it.")

if errors:
    print("ERROR: Site checks failed:")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)

print(f"Site architecture and route checks passed for brand: {brand}")
