# AGENTS

## Project Purpose
Legacy Python table and figure workflow associated with the Lung 2023 central sleep apnea CPAP-prescribing paper.

## Public and Data-Safety Rules
- Treat this repository as public. Do not add PHI, restricted datasets, credentials, private drafts, or publisher-formatted article text.
- Clinical sleep-center data are restricted; never add raw patient-level workbook exports, PHI, credentials, or local path files.
- Treat `CSA-CPAP-Prescribing` as the final Stata analysis repository named by the paper. This repo preserves the older Python workflow.

## How to Orient Quickly
- Start with `README.md` for project scope, workflow, data notes, citation, and license information.
- Use `CITATION.cff` for structured citation metadata when present.
- Inspect scripts/notebooks before running them; do not assume generated outputs are current.

## Workflow
From the repository root, use this as the initial run guidance:

```bash
python DataAnalysis.py --input data/private/CSA-Db-Working.xlsm --output-dir outputs/legacy-python
```

Use `tests/fixtures/synthetic_csa_workbook.xlsx` for smoke testing only; it is not scientifically meaningful.

## Verification Before Publishing Changes
- Run `git diff --check`.
- Validate `CITATION.cff` as YAML after citation edits.
- Run `python -m pytest` after workflow edits.
- Do not commit generated outputs, logs, caches, virtual environments, `.DS_Store`, or checkpoint files unless intentionally released.
- For clinical or collaborator data, confirm that no row-level restricted data or identifiers are included.
