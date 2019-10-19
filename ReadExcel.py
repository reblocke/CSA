# Read Excel Files for the CSA project
from openpyxl import load_workbook
import pandas as pd

def load_sheet(location):
    """loads the sheet excel doc and returns the 1st sheet"""
    wb = load_workbook(location, read_only=True, data_only=True)
    return wb[wb.sheetnames[0]]

def sheet_to_arrays(excel_sheet):
    """makes a 2 dimensional list database and fills it based on an
    openpyxl excel sheet"""
    # Name_Column = 1
    # MRN_Column = 2
    # DOB_Column = 3
    Age_Column = 4 # Age at diag sleep study
    Sex_Column = 5
    # Race_Columnn = 6
    # Zip_Column = 7
    BMI_Column = 8
    # Smoking_Column = 9
    # Comorb_Column = 10 (split?)
    # Heart_Column = 11 (split?)
    # CNS_Coluimn = 12 (split?)
    Base_Dx_Column = 13
    AHI_Column = 14 # Diagnostic AHI
    Post_Dx_Column = 15
    Final_Tx_Column = 16
    Outcome_Column = 17
    Path_ASV_Column = 18
    Time_ASV_Column = 19
    # Loc_Column = 20
    # Sleep_Study_Column = 21

    Patients = list()

    # print("Processing excel spreadsheet")
    i = 1

    for patient in excel_sheet.iter_rows():
        # For each row that has an MRN entry...
        # print("Processing chart #" + str(i))
        row = list()
        row.append(i-1) # = ID, previously (patient[MRN_Column].value)

        try:
            row.append(int(patient[Age_Column].value))
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        try:
            row.append(patient[Sex_Column].value.lower()) #Make discrete?
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        try:
            row.append(float(patient[BMI_Column].value))
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        try:
            row.append(float(patient[AHI_Column].value))
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        # Should these following ones be made discrete?
        try:
            row.append(patient[Base_Dx_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        try:
            row.append(patient[Post_Dx_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        try:
            row.append(patient[Final_Tx_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        try:
            row.append(patient[Outcome_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            row.append(None)

        try:
            row.append(patient[Path_ASV_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        try:
            row.append(patient[Time_ASV_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        Patients.append(row)
        i = i+1

    return Patients[1:]  # take off the first row = labels


def arrays_to_df(patient_array):
    """takes the database in array form and outputs a dataframe with variables
    categorized.

    ['ID', Age', 'Sex', 'BMI', 'AHI', 'BaseDx', 'PostDx', 'FinalTx', 'Outcome',
    "ProcToASV", "TimeToASV]"""

    df = pd.DataFrame.from_records(patient_array, columns=['ID', 'Age',
        'Sex', 'BMI', 'AHI', 'BaseDx', 'PostDx', 'FinalTx', 'Outcome',
        "ProcToASV", "TimeToASV"])

    df['Sex'] = df['Sex'].astype('category')

    BaseDxCat = pd.api.types.CategoricalDtype(categories=[
        "Mainly OSA (<10% CSA or most centra events either SOCAPACA)".lower(),
        "Combined OSA/CSA (CSA 10-50%)".lower(),
        "Predominantly CSA (>50% CSA)".lower(),
        "Pure CSA (<10% OSA)".lower()], ordered=True)
    df['BaseDx'] = df['BaseDx'].astype(BaseDxCat)

    # Not sure why this doesn't update cats going forward
    # df['BaseDx'].cat.rename_categories({
    #    "Mainly OSA (<10% CSA or most centra events either SOCAPACA)".lower(): '<10% CSA',
    #    "Combined OSA/CSA (CSA 10-50%)".lower(): '10-50% CSA',
    #    "Predominantly CSA (>50% CSA)".lower(): '50-90% CSA',
    #    "Pure CSA (<10% OSA)".lower(): '>90% CSA'})

    # Need to figure how to split
    df['PostDx'] = df['PostDx'].astype('category')

    FinalTxCat = pd.api.types.CategoricalDtype(categories=["cpap", "bipap",
        "asv (resmed/ respironics)","supplemental oxygen", "no treatment",
        "other", "ivaps"], ordered=False)
    df['FinalTx'] = df['FinalTx'].astype(FinalTxCat)

#    OutcomeCat = pd.api.types.CategoricalDtype(categories=[
#        "resolved w/ cpap", "failed cpap", "non-compliant", "n/a"], ordered=False)

    df['Outcome'] = df['Outcome'].astype('category')

    df['ProcToASV'] = df['ProcToASV'].astype('category')
    df['TimeToASV'] = df['TimeToASV'].astype('category')

    return df


def test_db_gen():
    # db = RecordsDb()
    pass


def main():
    # 0 for testing, 1 to run
    testing_mode = 1

    if testing_mode == 0:
        test_db_gen()
    else:
        # run the main program
        pass

if __name__ == '__main__':
    main()
