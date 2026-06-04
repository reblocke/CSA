# Reproducing the Legacy Python Workflow

This repository can rerun the historical Python table and figure workflow on a compatible local workbook. It does not include the original patient-level data.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run on Authorized Local Data

Place an authorized, de-identified workbook outside git tracking, for example:

```text
data/private/CSA-Db-Working.xlsm
```

Run:

```bash
python DataAnalysis.py --input data/private/CSA-Db-Working.xlsm --output-dir outputs/legacy-python
```

Generated legacy outputs will be written under `outputs/legacy-python/`.

## Smoke Test Without Clinical Data

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest
python DataAnalysis.py --input tests/fixtures/synthetic_csa_workbook.xlsx --output-dir /tmp/csa-smoke
```

The synthetic fixture validates workbook parsing and output writing, but it is not scientifically meaningful.

## Relationship to Published Results

The final Lung 2023 paper analysis repository is [reblocke/CSA-CPAP-Prescribing](https://github.com/reblocke/CSA-CPAP-Prescribing). This repository is retained for historical Python workflow transparency.
