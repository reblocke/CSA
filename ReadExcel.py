# Read Excel Files for the CSA project
import openpyxl as op
import pandas as pd

def load_sheet(location):
    """loads the sheet excel doc and returns the 1st sheet"""
    wb = op.load_workbook(location, read_only=True, data_only=True)
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
            print("Age Column Error: Row " + str(i))
            row.append(None)
        try:
            row.append(patient[Sex_Column].value.lower()) #Make discrete?
        except(ValueError, TypeError, AttributeError):
            print("Sex Column Error: Row " + str(i))
            row.append(None)
        try:
            row.append(float(patient[BMI_Column].value))
        except(ValueError, TypeError, AttributeError):
            print("BMI Column Error: Row " + str(i))
            row.append(None)
        try:
            row.append(float(patient[AHI_Column].value))
        except(ValueError, TypeError, AttributeError):
            print("AHI Column Error: Row " + str(i))
            row.append(None)
        # Should these following ones be made discrete?
        try:
            row.append(patient[Base_Dx_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            print("Base Dx Column Error: Row " + str(i))
            row.append(None)
        try:
            row.append(patient[Post_Dx_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            print("Post DX Column Error: Row " + str(i))
            row.append(None)
        try:
            row.append(patient[Final_Tx_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            print("Final Tx Column Error: Row " + str(i))
            row.append(None)
        try:
            row.append(patient[Outcome_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            print("Outcome Column Error: Row " + str(i))
            row.append(None)

        try:
            row.append(patient[Path_ASV_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            print("Path to ASV Column Error: Row " + str(i))
            row.append(None)
        try:
            row.append(patient[Time_ASV_Column].value.lower().strip())
        except(ValueError, TypeError, AttributeError):
            print("Time to ASV Column Error: Row " + str(i))
            row.append(None)
        Patients.append(row)
        i = i+1

    return Patients[1:]  # take off the first row = labels


def histo_dx_includes(df):
    """Returns a historgram (pandas series) of diagnosis where a post-titration diagnosis of
    w/ multiple factors (e.g. Meds+CV) each are counted toward their respective
    category counts"""

    # TODO: need to find and delete combination TE + other etiology postDx's
    histo = pd.Series({"TECSA":0,
        "OSA-CSA":0,
        "Cardiac":0,
        "Neurologic":0,
        "Medication":0,
        "Primary":0})

    for dx in df['PostDx']:
        dxstr = str(dx)
        for cat in histo.index:
            if cat in dxstr:
                histo[cat] +=1
    return histo

def arrays_to_df(patient_array):
    """takes the database in array form and outputs a dataframe with variables
    categorized.

    ['ID', Age', 'Sex', 'BMI', 'AHI', 'BaseDx', 'PostDx', 'FinalTx', 'Outcome',
    "ProcToASV", "TimeToASV]"""

    df = pd.DataFrame.from_records(patient_array, columns=['ID', 'Age',
        'Sex', 'BMI', 'AHI', 'BaseDx', 'PostDx', 'FinalTx', 'Outcome',
        "ProcToASV", "TimeToASV"])

    df['Sex'] = df['Sex'].astype('category')

    df['BaseDx'] = df['BaseDx'].replace(
        {"Mainly OSA (<10% CSA or most centra events either SOCAPACA)".lower(): 'Mainly OSA',
        "Combined OSA/CSA (CSA 10-50%)".lower(): 'Combined OSA/CSA',
        "Predominantly CSA (>50% CSA)".lower(): 'Predominantly CSA',
        "Pure CSA (<10% OSA)".lower(): 'Pure CSA'})

    BaseDxCat = pd.api.types.CategoricalDtype(categories=[
        'Mainly OSA', 'Combined OSA/CSA', 'Predominantly CSA',
        'Pure CSA'], ordered=True)
    df['BaseDx'] = df['BaseDx'].astype(BaseDxCat)

    # transform PostDx to shorter labels
    df['PostDx'] = df['PostDx'].apply(matchDx).astype('category')

    df['FinalTx'] = df['FinalTx'].replace(
        {"cpap": "cpap",
        "bipap": "bipap",
        "asv (resmed/ respironics)": "asv",
        "supplemental oxygen": "O2",
        "no treatment": "none",
        "other": "other",
        "ivaps": "ivaps"})
    FinalTxCat = pd.api.types.CategoricalDtype(categories=["ivaps", "asv",
        "bipap", "cpap", "O2", "none", "other"], ordered=True)
    df['FinalTx'] = df['FinalTx'].astype(FinalTxCat)

#    OutcomeCat = pd.api.types.CategoricalDtype(categories=[
#        "resolved w/ cpap", "failed cpap", "non-compliant", "n/a"], ordered=False)

    df['Outcome'] = df['Outcome'].astype('category')

    df['ProcToASV'] = df['ProcToASV'].replace(
        {"n/a": 'other',
        "initial treatment": "initial treatment",
        "after trial of cpap": "after trial of cpap",
        "after trial of bipap": 'after trial of bipap'
        })
    procToASVCat = pd.api.types.CategoricalDtype(categories=['other',
        "initial treatment", 'after trial of cpap', 'after trial of bipap'],
        ordered=True)
    df['ProcToASV'] = df['ProcToASV'].astype(procToASVCat)

    df['TimeToASV'] = df['TimeToASV'].replace(
        {"n/a": 'other',
        "0-1 month": 'within 2 mo',
        "3-6 months": '3-6 mo',
        ">6 months": '6+ mo'})
    timeToASVCat = pd.api.types.CategoricalDtype(categories=['other',
        "within 2 mo", '3-6 mo', '6+ mo'], ordered=True)
    df['TimeToASV'] = df['TimeToASV'].astype(timeToASVCat)

    return df


def matchDx(pt_dx):
    """match the diagnosis up with the shorter labels"""
    # print(pt_dx)
    new_dx = ""
    rep = {"te csa": "+TECSA",
        "csa w/cns dz (tbi/ cerebrovascular dz/ mass lesion/ neurodegenerative dz/ other)":"+Neurologic",
        "primary csa (idiopathic csa)":"+Primary",
        "osa-associated":"+OSA-CSA",
        "csa w/opioid (methadone/ fentanyl/ oxycontin/ suboxone/ other)":"+Medication",
        "csa w/heart dz (hfref <45%/ hfpef >45% /a.fib)":"+Cardiac"}
    for dx in pt_dx.split(","):
        new_dx = new_dx + rep[dx.strip().lower()]
    return new_dx[1:]  #-first +


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
