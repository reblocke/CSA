# CSA Legacy Python Workflow for ATS 2020 Central Sleep Apnea Abstract

Legacy Python code for the central sleep apnea (CSA) cohort described in the ATS 2020 abstract **"Spectrum of Central Sleep Apnea at an Academic Sleep Center Between 2016-2018 and Treatment Responses to CPAP vs. Adaptive Servo Ventilation."**

## Description

This repository is a cleaned preservation copy of historical Python scripts for CSA cohort description, treatment-response summaries, tables, and exploratory figures. It is intended for code inspection, documentation of the old workflow, and local reruns on authorized compatible data.

The associated indexed abstract is:

- J. Sellman, B. W. Locke, J. McFarland, F. Uribe, and K. Sundar. **Spectrum of Central Sleep Apnea at an Academic Sleep Center Between 2016-2018 and Treatment Responses to CPAP vs. Adaptive Servo Ventilation.** *American Journal of Respiratory and Critical Care Medicine*. 2020;201(Supplement_1):A2430. DOI: [10.1164/ajrccm-conference.2020.201.1_MeetingAbstracts.A2430](https://doi.org/10.1164/ajrccm-conference.2020.201.1_MeetingAbstracts.A2430).

This repository is not the code repository for the later CPAP-prescribing publication. The downstream Stata repository [reblocke/CSA-CPAP-Prescribing](https://github.com/reblocke/CSA-CPAP-Prescribing) supports that separate final paper workflow.

## Project Status

- Status: legacy Python workflow associated with an indexed ATS 2020 abstract.
- Primary use: inspect or rerun the historical Python workflow on a compatible local workbook.
- Public data status: no patient-level clinical data are included.
- Citation: cite the ATS 2020 abstract for the scholarly work and this repository for software/code reuse; see [CITATION.cff](CITATION.cff).

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

Generated root-level PNG and XLSX outputs that were previously tracked in git were archived before cleanup in the GitHub release [legacy-python-outputs-2026-06-03](https://github.com/reblocke/CSA/releases/tag/legacy-python-outputs-2026-06-03). These files are historical artifacts from the Python workflow associated with the ATS 2020 abstract and are not treated as final journal-paper figures.

## Dependencies

The legacy workflow uses Python plus `pandas`, `openpyxl`, `matplotlib`, `seaborn`, and `scikit-learn`. The project intentionally remains a script repository rather than a packaged Python library.

## Citation

Please cite the ATS 2020 abstract for the scholarly analysis and this repository as a legacy software artifact if you reuse or adapt the code. Machine-readable citation metadata are provided in [CITATION.cff](CITATION.cff).

An author-written repository summary for machine indexing is available at [abstract/ats-2020-summary.md](abstract/ats-2020-summary.md). This repository links to the publisher record and does not mirror the full publisher abstract text.

## Security and Hygiene Notes

Historical SSH key files were removed from the default branch during the 2026 repository cleanup and should be treated as compromised. Removal from the current branch does not remove old blobs from git history.

## License

Repository code is released under the MIT License. Restricted clinical data, third-party material, and unpublished manuscript drafts are not included and are not covered by this repository license.

## Contact

Maintainer: Brian W. Locke (`@reblocke`, ORCID [0000-0002-3588-5238](https://orcid.org/0000-0002-3588-5238)). Use GitHub issues or pull requests for repository-specific questions.
