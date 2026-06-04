# CSA Legacy Python Data Dictionary

This repository expects a historical Excel workbook layout used for the central sleep apnea project. The original workbook is restricted clinical data and is not included.

## Input Workbook Contract

`ReadExcel.py` reads the first worksheet and uses fixed zero-based column positions from the historical workbook. The first row is treated as a header row and skipped.

| Zero-based index | Historical field | Derived dataframe column | Notes |
|---:|---|---|---|
| 4 | Age at diagnostic sleep study | `Age` | Numeric years. |
| 5 | Sex | `Sex` | Lowercased and categorical. |
| 6 | Race / ethnicity | `Race` | Lowercased; historical Utah-specific recode maps `not hispanic/latino` to `white`. |
| 8 | Body mass index | `BMI` | Numeric kg/m2. |
| 9 | Smoking status | `Smoking` | Lowercased and categorical. |
| 10 | General comorbidities | `Comorb` | Recoded to combinations of `htn`, `dm`, `psych`, `ckd`, `none`. |
| 11 | Cardiac comorbidities | `Heart` | Recoded to combinations of `cad`, `afib`, `hfpef`, `hfref`, `other`, `none`. |
| 12 | CNS comorbidities | `CNS` | Recoded to combinations of `cva`, `neurodegenerative`, `dementia`, `chiari`, `other`, `none`. |
| 13 | Baseline apnea category | `BaseDx` | Recoded to ordered categories: `Mainly OSA`, `Combined OSA/CSA`, `Predominantly CSA`, `Pure CSA`. |
| 14 | Diagnostic AHI | `AHI` | Numeric events/hour. |
| 15 | Post-titration / etiologic diagnosis | `PostDx` | Recoded to `TECSA`, `Cardiac`, `Neurologic`, `Medication`, `Primary`; multiple labels may be joined with `+`. |
| 16 | Final treatment | `FinalTx` | Recoded to `niv-o2`, `niv`, `asv`, `bipap-o2`, `bipap`, `cpap`, `mad`, `O2`, `none`. |
| 17 | Outcome | `Outcome` | Historical categorical text used by downstream summaries. |
| 18 | Path to ASV | `ProcToASV` | Recoded to `other`, `initial treatment`, `after trial of cpap`, `after trial of bipap`. |
| 19 | Time to ASV | `TimeToASV` | Recoded to `other`, `within 2 mo`, `3-6 mo`, `6+ mo`. |
| 21 | Diagnostic study type | `StudyType` | Historical PSG/HSAT-like source field. |

## Derived Variables

- `AHI_label`: OSA severity category derived from `AHI`.
- `InitTx`: inferred initial treatment from `FinalTx`, `ProcToASV`, and `Outcome`.
- `FinalTx_coll`: encoded-output helper collapsing final treatment to CPAP/BPAP/ASV/Other.
- `PercOSA`: encoded-output helper collapsing `BaseDx` into mostly OSA vs mostly CSA.

## Restricted Data Rules

- Do not commit the original workbook or any row-level clinical export.
- Keep local clinical workbooks under `data/private/`, which is ignored by git.
- Use the synthetic workbook in `tests/fixtures/` only for code smoke tests.
