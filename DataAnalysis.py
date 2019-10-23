from openpyxl import load_workbook
import pandas as pd
from ReadExcel import *
import matplotlib.pyplot as plt
import seaborn as sns

def summary_stats(df):

    print("\nAge Summary Statistics:\n")
    print(str(df['Age'].describe()))

    print("\nBMI Summary Statistics:\n")
    print(str(df['BMI'].describe()))

    print("\nAHI Summary Statistics:\n")
    print(str(df['AHI'].describe()))

    print("\nBase Dx Counts:\n")
    print(str(df['BaseDx'].value_counts()))

    print("\nPost Dx Counts:\n")
    print(str(df['PostDx'].value_counts()))

    print("\nFinal Tx Counts:\n")
    print(str(df['FinalTx'].value_counts()))

    print("\nOutcome Counts:\n")
    print(str(df['Outcome'].value_counts()))


def pieChartBaseDx(df):
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()  # container object
    ax = plt.axes() # the box we'll draw in

    dx_counts = df['BaseDx'].value_counts().sort_index()
    colors = ["#d6cb9c", "#9cc1ec", "#8fd9c8", "#e7aeca"]  # IWantHue fancy, light
    ax.pie(dx_counts, labels=dx_counts.index, autopct="%1.1f%%", startangle=0,
        colors=colors, wedgeprops={'edgecolor' :'black'})
    ax.axis('equal')
    ax.set_title("Patients Categorized by Percentage of Apneas of Central Origin")
    ax.legend(["<10% Central", "10-50% Central", "50-90% Central", ">90% Central"],
        loc='lower left', frameon=True)
    plt.tight_layout()
    plt.show()


def visualizations(df):

    # Severity of OSA by porcent CSAs and Sex
    #ax = sns.boxplot('BaseDx', 'AHI', hue='Sex', data=df)
    # Outcome by Base Dx as histograms
    # Todo: figure out how to normalize this
    # sns.catplot('BaseDx', hue='Outcome', kind='count', data=df)

    # Vis of distribution of AHIs
    # cleaned_df = df[df['AHI'].notnull()]
    # sns.distplot(cleaned_df['AHI'])
    pass


def printSumByBaseDx(df):
    print("\n\n----AMONG THE ENTIRE DATASET----\n")
    summary_stats(df)

    print("\n\n----AMONG PATIENTS WITH PREDOMINANTLY CSA (MORE THAN 50%)----\n")
    CSA_predom = df.loc[df['BaseDx'] == "Predominantly CSA"]
    CSA_pure = df.loc[df['BaseDx'] == "Pure CSA"]
    summary_stats(pd.merge(CSA_predom, CSA_pure, how='outer'))

    print("\n\n----AMONG PATIENTS WITH < 50% CSA-----")
    OSA_predom = df.loc[df['BaseDx'] == "Mainly OSA"]
    OSA_pure = df.loc[df['BaseDx'] == "Combined OSA/CSA"]
    summary_stats(pd.merge(OSA_predom, OSA_pure, how='outer'))


def main():
    # Location of Db file
    db_loc = "/Users/reblocke/Box/Residency Personal Files/Scholarly Work/CSA/Databases/CSA-Db-Working.xlsm"
    df = arrays_to_df(sheet_to_arrays(load_sheet(db_loc)))

    # ['ID', 'Age', 'Sex', 'BMI', 'AHI', 'BaseDx', 'PostDx', 'FinalTx', 'Outcome',
    # "ProcToASV", "TimeToASV]
    df.to_excel('output.xlsx')

    visualizations(df)

    pieChartBaseDx(df)
    #printSumByBaseDx(df)

if __name__ == '__main__':
    main()
