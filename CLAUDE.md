# Claude Code Operating Instructions

You are building a reliable HR job-search and application-management system.

## Candidate and scope

The candidate profile is loaded from `config/candidate.local.json` when present. Never hard-code personal details in source code, tests, logs, commits, or documentation. Use `config/candidate.example.json` as a schema/template only.

Target roles:
- HR Business Partner / HRBP
- Talent Acquisition
- Talent Management
- Organizational Development
- HR Technology / HR Transformation

Geography: India-wide, relocation permitted.

Platforms in priority order:
1. LinkedIn Easy Apply
2. Naukri
3. Indeed
4. IIMJobs
5. Company career portals

## Non-negotiable accuracy rules

1. Do not claim an application was submitted merely because a job page redirected to an ATS.
2. `SUBMITTED_VERIFIED` requires confirmation evidence recorded in the database.
3. A redirect or open ATS form is `ATS_PENDING`.
4. A partially completed form is `APPLYING`.
5. Detect duplicates by platform job ID, canonical URL, and company/title similarity.
6. Do not fabricate experience, dates, skills, education, salary, or achievements.
7. If candidate data conflicts with the CV or application form, flag it for review. Do not silently choose a convenient answer.
8. Do not bypass CAPTCHA, MFA, device verification, bot detection, access controls, or platform rate limits.
9. Stop for candidate intervention on legal declarations, demographic/EEO declarations where optional or sensitive, payment, offer acceptance, interview scheduling commitments, or contractual commitments.
10. Respect each platform's terms and technical restrictions. Prefer supported integrations and normal user-facing browser flows.

## Autonomy boundary

The candidate has authorized routine job application submissions, but that does not authorize false statements, security circumvention, payments, legal commitments, or acceptance of employment terms. Start in dry-run mode. Require explicit configuration to enable submission after tests pass.

## Development workflow

- Read the existing code before changing it.
- Make small, testable changes.
- Add tests for duplicate detection, scoring, state transitions, and evidence verification.
- Never commit CVs, candidate.local.json, browser profiles, cookies, tokens, `.env`, or application confirmation emails.
- Use environment variables or local ignored files for secrets.
- Keep an audit trail of actions and status changes.
- Prefer SQLite and deterministic logic for records and scoring. Use an LLM for interpretation, not as the only source of truth.

## Required statuses

`DISCOVERED`, `SHORTLISTED`, `APPLYING`, `ATS_PENDING`, `SUBMITTED_VERIFIED`, `ALREADY_APPLIED`, `REJECTED`, `EXPIRED`, `BLOCKED`, `NEEDS_REVIEW`.

Only the verification module may transition a record to `SUBMITTED_VERIFIED`.

## Initial task

Implement Phase 1 only:
- Validate candidate profile schema.
- Create SQLite schema and initialization.
- Add job/application CRUD functions.
- Add duplicate detection.
- Add status transition validation.
- Add unit tests.
- Do not implement browser automation or submit applications until Phase 1 is tested and reviewed.
