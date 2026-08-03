# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-08-03

### Added
- Created complete Open Source Governance suite (`LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `NOTICE`, `CITATION.cff`).
- Created complete Community & Infrastructure configuration under `.github/`:
  - `CODEOWNERS`, `SUPPORT.md`, `FUNDING.yml`, `dependabot.yml`, `release.yml`, `labels.yml`.
  - Structured YAML Issue Templates (`bug_report.yml`, `feature_request.yml`, `documentation.yml`, `question.yml`).
  - Production-grade Pull Request Template (`PULL_REQUEST_TEMPLATE.md`).
- Added complete Technical Documentation Suite under `docs/`:
  - `INSTALLATION.md`, `QUICK_START.md`, `ARCHITECTURE.md`, `HARDWARE_SETUP.md`, `FIRMWARE_GUIDE.md`, `TROUBLESHOOTING.md`, `ROADMAP.md`, `FAQ.md`.
- Added GitHub Actions workflow `lint-markdown.yml` for automated documentation validation.

### Changed
- Refactored `profile-3d.yml` workflow to support Node 24 runners and `actions/checkout@v5`.
- Updated `README.md` Top Programming Languages widget URL parameters to support private repository language aggregation.
- Re-scaled skill matrix SVG icons to `1.55x` scale with borderless floating card aesthetic in `assets/tech-stack.svg`.

### Fixed
- Fixed Vercel stats API timing out by pointing to high-availability Vercel mirror.
- Resolved non-fast-forward push failures in GitHub Actions automated contribution workflows.

## [1.1.0] - 2026-08-02

### Added
- Integrated automated 3D Contribution Calendar workflow (`profile-3d.yml`) using `yoshi389111/github-profile-3d-contrib`.
- Integrated animated GitHub Contribution Grid Snake workflow (`snake.yml`) using `Platane/snk`.
- Designed 7 custom vector SVG graphics in `assets/` matching the Dark Neon NIR Dashboard aesthetic (`#090A12`, `#22D3EE`, `#8B5CF6`).

## [1.0.0] - 2026-08-01

### Added
- Initial public release of Krishna Kant Garhe's GitHub Engineering Profile & Open Source Showcase.
