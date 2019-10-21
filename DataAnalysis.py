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

def visualizations(df):
    sns.set()
    # Severity of OSA by porcent CSAs and Sex
    ax = sns.boxplot('BaseDx', 'AHI', hue='Sex', data=df)
    ax.set_title("Severity of OSA by Percent CSAs and Sex")

    # Outcome by Base Dx as histograms
    # Todo: figure out how to normalize this
    # sns.catplot('BaseDx', hue='Outcome', kind='count', data=df)

    # Vis of distribution of AHIs
    # cleaned_df = df[df['AHI'].notnull()]
    # sns.distplot(cleaned_df['AHI'])

    #Box plot? https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f
    #Need to find counts transformation

    plt.show()


def printSumByBaseDx(df):
    print("\n\n----AMONG THE ENTIRE DATASET----\n")
    summary_stats(df)

    print("\n\n----AMONG PATIENTS WITH PREDOMINANTLY CSA (MORE THAN 50%)----\n")
    CSA_predom = df.loc[df['BaseDx'] == "Predominantly CSA (>50% CSA)".lower()]
    CSA_pure = df.loc[df['BaseDx'] == "Pure CSA (<10% OSA)".lower()]
    summary_stats(pd.merge(CSA_predom, CSA_pure, how='outer'))

    print("\n\n----AMONG PATIENTS WITH < 50% CSA-----")
    OSA_predom = df.loc[df['BaseDx'] == "Mainly OSA (<10% CSA or most centra events either SOCAPACA)".lower()]
    OSA_pure = df.loc[df['BaseDx'] == "Combined OSA/CSA (CSA 10-50%)".lower()]
    summary_stats(pd.merge(OSA_predom, OSA_pure, how='outer'))


def main():
    # Location of Db file
    db_loc = "/Users/reblocke/Box/Residency Personal Files/Scholarly Work/CSA/Databases/CSA-Db-Working.xlsm"
    df = arrays_to_df(sheet_to_arrays(load_sheet(db_loc)))

    # ['ID', 'Age', 'Sex', 'BMI', 'AHI', 'BaseDx', 'PostDx', 'FinalTx', 'Outcome',
    # "ProcToASV", "TimeToASV]
    df.to_excel('output.xlsx')

    visualizations(df)

    # printSumByBaseDx(df)


    # "Pure CSA (<10% OSA)".lower()

if __name__ == '__main__':
    main()
