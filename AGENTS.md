# AGENTS

## Project Purpose
Central sleep apnea data analysis at U of U sleep-wake center

## Public and Data-Safety Rules
- Treat this repository as public. Do not add PHI, restricted datasets, credentials, private drafts, or publisher-formatted article text.
- Clinical sleep-center data likely restricted; verify no PHI
- Manuscript status: Superseded or overlaps with CSA-CPAP-Prescribing; accepted draft candidates exist locally

## How to Orient Quickly
- Start with `README.md` for project scope, workflow, data notes, citation, and license information.
- Use `CITATION.cff` for structured citation metadata when present.
- Inspect scripts/notebooks before running them; do not assume generated outputs are current.

## Workflow
From the repository root, use this as the initial run guidance:

```bash
Review Python workflow
```

If the command is a placeholder, refine it after reading the local scripts and existing README.

## Verification Before Publishing Changes
- Run `git diff --check`.
- Validate `CITATION.cff` as YAML after citation edits.
- Do not commit generated outputs, logs, caches, virtual environments, `.DS_Store`, or checkpoint files unless intentionally released.
- For clinical or collaborator data, confirm that no row-level restricted data or identifiers are included.
