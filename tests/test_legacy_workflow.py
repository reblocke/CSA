from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd

from ReadExcel import arrays_to_df, infer_initial_treatment, load_sheet, sheet_to_arrays


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "synthetic_csa_workbook.xlsx"


def test_synthetic_workbook_loads_and_derives_columns() -> None:
    rows = sheet_to_arrays(load_sheet(FIXTURE))
    assert len(rows) == 4

    df = arrays_to_df(rows)
    assert set(["Age", "BaseDx", "PostDx", "FinalTx", "InitTx", "StudyType"]).issubset(df.columns)
    assert list(df["BaseDx"].cat.categories) == [
        "Mainly OSA",
        "Combined OSA/CSA",
        "Predominantly CSA",
        "Pure CSA",
    ]
    assert set(df["PostDx"].astype(str)) >= {"TECSA", "Cardiac", "Medication", "Primary"}


def test_infer_initial_treatment_key_cases() -> None:
    cases = [
        ({"FinalTx": "cpap", "Outcome": "resolved w/ cpap", "ProcToASV": "other"}, "cpap"),
        ({"FinalTx": "bipap", "Outcome": "failed cpap", "ProcToASV": "other"}, "cpap"),
        ({"FinalTx": "bipap-o2", "Outcome": "failed cpap", "ProcToASV": "other"}, "cpap"),
        ({"FinalTx": "asv", "Outcome": "n/a", "ProcToASV": "initial treatment"}, "asv"),
        ({"FinalTx": "none", "Outcome": "resolved w/ cpap", "ProcToASV": "other"}, "cpap"),
    ]

    for payload, expected in cases:
        assert infer_initial_treatment(pd.Series(payload)) == expected


def test_data_analysis_script_writes_expected_outputs(tmp_path: Path) -> None:
    output_dir = tmp_path / "legacy-output"
    proc = subprocess.run(
        [
            sys.executable,
            "DataAnalysis.py",
            "--input",
            str(FIXTURE),
            "--output-dir",
            str(output_dir),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert (output_dir / "coded_output.xlsx").exists()
    assert (output_dir / "keys_coded_output.xlsx").exists()
    assert (output_dir / "tables.xlsx").exists()
    assert (output_dir / "Figure 2 - etio by perc csa.png").exists()
    assert (output_dir / "Figure 3 - outcome of cpap by etio.png").exists()
    assert (output_dir / "Figure 4 - final tx by perc csa.png").exists()
