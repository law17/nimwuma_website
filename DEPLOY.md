# GitHub Pages deployment

The repository is configured for the project-site URL:

`https://law17.github.io/nimwuma_website/`

If the repository uses a different name, change `baseurl` in `_config.yml` before deployment.

## First push

Create an empty GitHub repository named `nimwuma_website`, then from the extracted project directory run:

```bash
git init -b main
git add .
git commit -m "Initial website"
git remote add origin https://github.com/law17/nimwuma_website.git
git push -u origin main
```

## Enable Pages

In the GitHub repository:

1. Open **Settings**.
2. Open **Pages** under **Code and automation**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Open the **Actions** tab and confirm the `Deploy Jekyll site to GitHub Pages` workflow completes successfully.

The workflow builds the Jekyll site and deploys it automatically whenever `main` is pushed.

## Before commercial launch

- Confirm the business email in `_data/company.yml` and set `contact.email_active: true`.
- Complete Privacy, Terms and Security content.
- Review pricing and package scope.
- Replace the GitHub project URL with a custom domain later if desired.
- Keep `staging: true` until the email and legal/security content are ready; change it to `false` for commercial launch.
