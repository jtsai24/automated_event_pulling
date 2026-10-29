# Website publishing and custom domain

Related issues: [#1 — publishing pipeline](https://github.com/jtsai24/automated_event_pulling/issues/1) and [#2 — custom domain](https://github.com/jtsai24/automated_event_pulling/issues/2).

## Pipeline

1. The separate weekly event workflow verifies public events, updates Notion, and commits a Markdown report under `reports/`.
2. A relevant push to `main` triggers `.github/workflows/pages.yml`.
3. GitHub Actions checks out the repository on a temporary Ubuntu runner and prepares Python 3.12.
4. `python scripts/build_site.py` selects the newest weekly report and generates `docs/index.html` with embedded CSS and report navigation.
5. The workflow packages `docs/` and deploys it to GitHub Pages.
6. GitHub Pages serves the finished HTML; Python does not run when a visitor opens the site.

The v0 website has no backend, login, runtime Notion access, or browser-storage features. Only public report content is published.

## Files

| File | Purpose |
|---|---|
| `reports/* - Career AI Events for *.md` | Public report input |
| `scripts/build_site.py` | HTML rendering and styling |
| `docs/index.html` | Generated preview / website output |
| `.github/workflows/pages.yml` | Build and deployment recipe |

Run `python scripts/build_site.py` locally, then open `docs/index.html`. Edit the generator to change presentation. Changes to reports, the generator or workflow trigger publication; changing only the generated HTML does not.

GitHub Actions executes temporary build/deployment jobs; GitHub Pages hosts the result afterward. The website workflow does not collect events or update Notion.

## Hosting setup

Repository **Settings → Pages → Build and deployment → Source: GitHub Actions** must be enabled once. Inspect the [Actions tab](https://github.com/jtsai24/automated_event_pulling/actions) for run status and logs. A successful build followed by a Configure Pages error can mean this setting is missing.

## Custom domain

Website: https://events.jimmytsai.org/

Set the repository's Pages **Custom domain** to `events.jimmytsai.org`. In Squarespace's DNS settings for `jimmytsai.org`, use:

| Type | Name | Data / target | TTL |
|---|---|---|---|
| CNAME | `events` | `jtsai24.github.io` | 4 hours |

A CNAME target is a hostname, so it excludes `https://` and the repository path. GitHub's custom-domain setting identifies which project serves this hostname. Preserve existing email DNS records.

After DNS validation, GitHub provisions a TLS certificate; keep **Enforce HTTPS** enabled. The option can temporarily be disabled while issuance is pending. GitHub documents that HTTPS availability can take up to 24 hours.

For this custom Actions publishing mode, GitHub does not require a repository `CNAME` file; use the repository Pages setting.

## Verification and privacy

Check the custom-domain HTTPS address, navigation and event links after setup. Preserve unknown times and source-gap notices in generated output. Do not commit credentials, email receipts, mailbox links, billing details, private notes or account screenshots.

## References

- [GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)
- [GitHub Pages custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [Squarespace DNS records](https://support.squarespace.com/hc/en-us/articles/360002101888-Edit-your-domain-s-DNS-records)
