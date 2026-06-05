# AGENTS

## Project Purpose

Legacy Python table and figure workflow for an unpublished central sleep apnea descriptive analysis.

## Public and Data-Safety Rules

- Treat this repository as public. Do not add PHI, restricted datasets, credentials, private drafts, or publisher-formatted article text.
- Clinical sleep-center data are restricted; never add raw patient-level workbook exports, PHI, credentials, or local path files.
- Do not describe this repository as the code repository for the later CPAP-prescribing publication.
- `CSA-CPAP-Prescribing` is a separate downstream Stata repository for the final paper workflow; this repository preserves the older descriptive Python workflow.

## How to Orient Quickly

- Start with `README.md` for project scope, workflow, data notes, citation, and license information.
- Use `llms.txt` for machine-readable repository purpose and agent cautions.
- Use `CITATION.cff` for structured repository software citation metadata.
- Inspect scripts before running them; do not assume generated outputs are current.

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
- Search documentation for incorrect publication identifiers or article framing before release.
- Do not commit generated outputs, logs, caches, virtual environments, `.DS_Store`, or checkpoint files unless intentionally released.
- For clinical or collaborator data, confirm that no row-level restricted data or identifiers are included.
