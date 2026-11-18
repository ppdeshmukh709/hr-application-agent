# HR Application Agent

A local-first job discovery, fit-scoring, application tracking, and verification workspace for HR roles.

This repository is designed to be opened in Claude Code locally or connected to Claude Code in the cloud through GitHub.

## Important design principles

- The database is the source of truth for application status.
- A redirect is **ATS_PENDING**, never `SUBMITTED_VERIFIED`.
- A submission requires visible confirmation evidence or a reliable confirmation email/application ID.
- Never bypass CAPTCHAs, MFA, bot checks, or platform restrictions.
- Never invent candidate information or answer legal declarations without the candidate's judgment.
- Keep personal data, CVs, browser state, and credentials out of Git.

## Quick start

1. Create a **private** GitHub repository named `hr-application-agent`.
2. Upload/push this starter project.
3. Open `https://claude.ai/code`, connect GitHub, authorize access to this repository, and start a cloud session.
4. Ask Claude to inspect `CLAUDE.md` and implement Phase 1 only: database, candidate profile loading from a local ignored file, job ledger, and tests.
5. Do not enable live application submission until discovery, duplicate detection, and status verification have been tested.

## Local setup

Python 3.11+ is recommended. The starter uses the Python standard library.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m src.db.init_db
```

Create your private candidate file by copying `config/candidate.example.json` to `config/candidate.local.json` and filling it in. This local file is git-ignored.

## Phases

- Phase 1: candidate profile, SQLite schema, application ledger, duplicate checks, tests.
- Phase 2: job discovery and normalization; manual review queue.
- Phase 3: role-fit scoring and CV/role mapping.
- Phase 4: browser-assisted application workflow, initially dry-run only.
- Phase 5: evidence-based submission verification and reporting.

## Cloud-session note

Claude Code cloud sessions clone the GitHub repository into an isolated cloud environment. They do not automatically inherit files that exist only on your PC and are excluded from Git. Keep sensitive candidate data and the actual CV local unless you deliberately configure a secure, private transfer workflow. Cloud browser access and local Chrome session access are separate concerns.
