# Website repository

Jekyll/GitHub Pages website for the company defined in `_data/company.yml`.

## Architecture rule

Repeated business information must come from one authoritative location rather than being hard-coded across pages.

- `_data/company.yml` — brand name, legal name, tagline, logo, contact information, mission and core company information
- `_config.yml` — technical GitHub Pages/Jekyll settings such as URL and base URL
- `_data/pricing.yml` — Ghana and global pricing
- `_data/navigation.yml` — primary navigation
- `_data/footer.yml` — footer and legal links
- `_data/services.yml` — service-category summaries
- `_data/trust.yml` — reusable trust/security statements
- `_includes/` — shared page components
- `_layouts/` — shared page structures

## Before publishing

1. Confirm the final GitHub repository name. If it is not `nimwuma_website`, update `baseurl` in `_config.yml`.
2. Confirm the public GitHub Pages URL and update `url` if needed.
3. Secure the final domain/business email and update `contact.email` in `_data/company.yml`.
4. Complete Privacy, Terms and Security content before commercial launch. Those pages are currently marked `noindex`.
5. In GitHub: **Settings → Pages → Build and deployment → Source → GitHub Actions**.
6. Push to `main`. The included `.github/workflows/pages.yml` builds and deploys the Jekyll site.
7. The repository starts with `staging: true` in `_config.yml`, which blocks search indexing. Set it to `false` only when the site is ready for commercial launch.

## Local preview

With Ruby/Bundler installed:

```bash
bundle install
bundle exec jekyll serve
```

Then visit the local URL shown by Jekyll.

## Changing the company name later

Change the central values in `_data/company.yml`:

```yaml
brand:
  name: "New brand"
  legal_name: "New brand Ltd"
  tagline: "New tagline"
  logo: "/assets/images/brand-logo.png"
```

Templates reference this single company-data file, so text changes propagate throughout the rendered site. Replace the logo asset separately if the visual identity also changes.

## Pricing changes

Edit `_data/pricing.yml`. Do not manually duplicate prices into multiple pages unless there is a deliberate copy exception.

## v6 visual refinements

- Reduced the header logo footprint and header height for better navigation balance.
- Increased teal accent contrast on light backgrounds while retaining lighter teal accents on dark surfaces.
