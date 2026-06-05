# Changelog

## 2026-06-05

- Updated repository framing to cite the indexed ATS 2020 abstract, **"Spectrum of Central Sleep Apnea at an Academic Sleep Center Between 2016-2018 and Treatment Responses to CPAP vs. Adaptive Servo Ventilation."**
- Added the ATS 2020 abstract DOI and preferred citation metadata while preserving the correction that `CSA` is separate from the later `CSA-CPAP-Prescribing` paper repository.
- Added an author-written abstract summary for machine indexing without copying full publisher abstract text.

## 2026-06-04

- Corrected repository framing: `CSA` is an unpublished legacy Python descriptive-analysis repository, not the code repository for the later CPAP-prescribing publication.
- Removed incorrect article citation metadata and identifiers from repository documentation while preserving the 2026 cleanup, reproducibility, data-safety, and smoke-test changes.

## 2026-06-03

- Removed tracked credentials, IDE files, bytecode/cache files, and generated root outputs from the default branch cleanup branch.
- Archived historical generated PNG/XLSX root outputs in the GitHub release `legacy-python-outputs-2026-06-03`.
- Replaced the hard-coded local workbook path in `DataAnalysis.py` with `--input` and `--output-dir` arguments.
- Redirected legacy generated outputs to the selected output directory.
- Fixed the `infer_initial_treatment()` `bipap-o2` indexing typo.
- Added README, `CITATION.cff`, `llms.txt`, data dictionary, reproduction guide, dependency files, and no-PHI synthetic smoke tests.
