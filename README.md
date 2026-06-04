# CSA Legacy Python Analysis

Legacy Python code for early central sleep apnea (CSA) descriptive analyses associated with the publication **“Predictors of Initial CPAP Prescription and Subsequent Course with CPAP in Patients with Central Sleep Apneas at a Single Center.”**

## Description

This repository is a cleaned, citable preservation copy of the historical Python workflow used before the final paper-facing Stata analysis repository. It is intended for transparency, code inspection, and local reruns on authorized compatible data.

## Publication Links

- Version of record: Locke BW, Sellman J, McFarland J, Uribe F, Workman K, Sundar KM. *Lung*. 2023;201(6):625-634. DOI: [10.1007/s00408-023-00657-z](https://doi.org/10.1007/s00408-023-00657-z). PMID: [37987861](https://pubmed.ncbi.nlm.nih.gov/37987861/). PMCID: [PMC10869204](https://pmc.ncbi.nlm.nih.gov/articles/PMC10869204/).
- Historical preprint: DOI [10.21203/rs.3.rs-3199807/v1](https://doi.org/10.21203/rs.3.rs-3199807/v1). PMID: [37547021](https://pubmed.ncbi.nlm.nih.gov/37547021/). PMCID: [PMC10402256](https://pmc.ncbi.nlm.nih.gov/articles/PMC10402256/).
- Final paper analysis repository named by the code availability statement: [reblocke/CSA-CPAP-Prescribing](https://github.com/reblocke/CSA-CPAP-Prescribing).

## Relationship to the Paper

This repository preserves a historical Python workflow used during the CSA project. The final manuscript regression analyses and paper-facing outputs are maintained in `CSA-CPAP-Prescribing`, which is the primary code repository for reproducing the published Lung article. Use this repository when you need to inspect or rerun the legacy Python table/figure workflow on a compatible local workbook.

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
- `llms.txt` and `CITATION.cff` - machine-readable discovery and citation metadata.

## Legacy Outputs

Generated root-level PNG and XLSX outputs that were previously tracked in git were archived before cleanup in the GitHub release [legacy-python-outputs-2026-06-03](https://github.com/reblocke/CSA/releases/tag/legacy-python-outputs-2026-06-03). These files are historical Python workflow artifacts and are not guaranteed to match the final Lung 2023 manuscript figures.

## Dependencies

The legacy workflow uses Python plus `pandas`, `openpyxl`, `matplotlib`, `seaborn`, and `scikit-learn`. The project intentionally remains a script repository rather than a packaged Python library.

## Citation

Please cite the published article as the primary scholarly object and this repository as the legacy software artifact. Machine-readable citation metadata are provided in [CITATION.cff](CITATION.cff).

## Security and Hygiene Notes

Historical SSH key files were removed from the default branch during the 2026 repository cleanup and should be treated as compromised. Removal from the current branch does not remove old blobs from git history.

## License

Repository code is released under the MIT License. Restricted clinical data, third-party material, and publisher-formatted article text are not included and are not covered by this repository license.

## Contact

Maintainer: Brian W. Locke (`@reblocke`, ORCID [0000-0002-3588-5238](https://orcid.org/0000-0002-3588-5238)). Use GitHub issues or pull requests for repository-specific questions.
