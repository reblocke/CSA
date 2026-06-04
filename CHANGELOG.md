# Changelog

## 2026-06-03

- Removed tracked credentials, IDE files, bytecode/cache files, and generated root outputs from the default branch cleanup branch.
- Archived historical generated PNG/XLSX root outputs in the GitHub release `legacy-python-outputs-2026-06-03`.
- Replaced the hard-coded local workbook path in `DataAnalysis.py` with `--input` and `--output-dir` arguments.
- Redirected legacy generated outputs to the selected output directory.
- Fixed the `infer_initial_treatment()` `bipap-o2` indexing typo.
- Added publication-specific README, `CITATION.cff`, `llms.txt`, data dictionary, reproduction guide, dependency files, and no-PHI synthetic smoke tests.
