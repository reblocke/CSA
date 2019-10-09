# Read Excel Files for the CSA project
from openpyxl import load_workbook
import pandas as pd

# Locations
db_loc = "/Users/reblocke/Box/Residency Personal Files/Scholarly Work/CSA/Databases/CSA Db Starting from Z.xlsm"


def load_sheet(location):
    """loads the sheet excel doc and returns the 1st sheet"""
    wb = load_workbook(location, read_only=True, data_only=True)
    return wb[wb.sheetnames[0]]

def sheet_to_arrays(excel_sheet):
    """makes a 2 dimensional list database and fills it based on an openpyxl excel sheet"""
    MRN_Column = 2
    Age_Column = 4 # Age at diag sleep study
    Sex_Column = 5
    BMI_Column = 8
    AHI_Column = 14 # Diagnostic AHI
    Final_Tx_Column = 16
    Outcome_Column = 17

    Patients = list()

    print("Processing excel spreadsheet")
    i = 1

    for patient in excel_sheet.iter_rows():
        # For each row that has an MRN entry...
        print("Processing chart #" + str(i))
        row = list()
        row.append(patient[MRN_Column].value)

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
            row.append(patient[Final_Tx_Column].value.lower())
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        try:
            row.append(patient[Outcome_Column].value.lower())
        except(ValueError, TypeError, AttributeError):
            row.append(None)
        Patients.append(row)
        i = i+1

    return Patients[1:]  # take off the first row = labels


def test_db_gen():
    # db = RecordsDb()
    pass


def main():
    # 0 for testing, 1 to run
    testing_mode = 1

    if testing_mode == 0:
        #test mode
        pass
    else:
        # run the main program
        sheet = load_sheet(db_loc)
        patient_array = sheet_to_arrays(sheet)
        df = pd.DataFrame.from_records(patient_array, columns= ['MRN', 'Age', 'Sex', 'BMI', 'AHI', 'FinalTx', 'Outcome'])

        print("Age Descriptive Statistics:\n")
        print(str(df['Age'].describe()))

        print("BMI Descriptive Statistics:\n")
        print(str(df['BMI'].describe()))

        print("AHI Descriptive Statistics:\n")
        print(str(df['AHI'].describe()))

        #print("Age\n" +df['Age'].describe())


if __name__ == '__main__':
    main()
