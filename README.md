# CSA Legacy Python Descriptive Analysis

Legacy Python code for an unpublished central sleep apnea (CSA) descriptive analysis developed during an ATS-era manuscript workflow.

## Description

This repository is a cleaned preservation copy of historical Python scripts for CSA cohort description, tables, and exploratory figures. It is intended for code inspection, documentation of the old workflow, and local reruns on authorized compatible data.

This repository is not the code repository for the later CPAP-prescribing publication. The downstream Stata repository [reblocke/CSA-CPAP-Prescribing](https://github.com/reblocke/CSA-CPAP-Prescribing) supports that separate final paper workflow.

## Project Status

- Status: unpublished legacy descriptive analysis.
- Primary use: inspect or rerun the historical Python workflow on a compatible local workbook.
- Public data status: no patient-level clinical data are included.
- Repository code citation: see [CITATION.cff](CITATION.cff).

## Data Access

The original analysis used restricted single-center electronic health record and sleep-center data under University of Utah IRB #00123537. Raw patient-level data are not public and must not be committed to this repository.

To run the code, provide your own authorized, de-identified workbook with the historical column layout documented in [DATA_DICTIONARY.md](DATA_DICTIONARY.md). A synthetic workbook fixture is included only for smoke testing code paths.

## Quick Start

```bash
python -m pip install -r requirements.txt
python DataAnalysis.py --input data/private/CSA-Db-Working.xlsm --output-dir outputs/legacy-python
```

The script writes legacy generated files such as `tables.xlsx`, `coded_output.xlsx`, `keys_coded_output.xlsx`, and selected PNG figures under the chosen output directory.

For a no-PHI smoke test:

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest
python DataAnalysis.py --input tests/fixtures/synthetic_csa_workbook.xlsx --output-dir /tmp/csa-smoke
```

## Repository Layout

- `DataAnalysis.py` - legacy Python table, figure, and encoded-output workflow.
- `ReadExcel.py` - workbook ingestion, category recoding, and derived-variable helpers.
- `DATA_DICTIONARY.md` - expected workbook columns and derived variables.
- `REPRODUCING.md` - guidance for reproducing the legacy workflow with local restricted data.
- `tests/` - synthetic smoke tests that contain no clinical data.
- `llms.txt` and `CITATION.cff` - machine-readable discovery and repository citation metadata.

## Legacy Outputs

Generated root-level PNG and XLSX outputs that were previously tracked in git were archived before cleanup in the GitHub release [legacy-python-outputs-2026-06-03](https://github.com/reblocke/CSA/releases/tag/legacy-python-outputs-2026-06-03). These files are historical unpublished Python workflow artifacts and are not treated as final manuscript figures.

## Dependencies

The legacy workflow uses Python plus `pandas`, `openpyxl`, `matplotlib`, `seaborn`, and `scikit-learn`. The project intentionally remains a script repository rather than a packaged Python library.

## Citation

Please cite this repository as a legacy software artifact if you reuse or adapt the code. Machine-readable citation metadata are provided in [CITATION.cff](CITATION.cff).

## Security and Hygiene Notes

Historical SSH key files were removed from the default branch during the 2026 repository cleanup and should be treated as compromised. Removal from the current branch does not remove old blobs from git history.

## License

Repository code is released under the MIT License. Restricted clinical data, third-party material, and unpublished manuscript drafts are not included and are not covered by this repository license.

## Contact

Maintainer: Brian W. Locke (`@reblocke`, ORCID [0000-0002-3588-5238](https://orcid.org/0000-0002-3588-5238)). Use GitHub issues or pull requests for repository-specific questions.
