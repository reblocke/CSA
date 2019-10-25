from openpyxl import load_workbook
import pandas as pd
from ReadExcel import *
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.sankey as sankey

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


def sankeyTypeFinalTx(df):
    fig = plt.figure()  # container object
    ax = plt.axes() # the box we'll draw in

    dx_counts = df['BaseDx'].value_counts().sort_index()
    outcome_counts = df['FinalTx'].value_counts() * -1.0
    x = dx_counts.get_values().sum()

    flow = dx_counts.get_values().tolist() + outcome_counts.get_values().tolist()
    label = dx_counts.index.tolist() + outcome_counts.index.tolist()

    sk = sankey.Sankey(ax, head_angle=120, offset=0.4, scale=1/float(x),
        unit=" Pt", gap=1.0, margin=0.1,
        flows= flow,
        labels=label,
        orientations=[1, 1, 0, -1, 1, 0, 1, -1, -1, -1, 1])

    #sk.add(flows=[0.05, 0.05, 0.9, -0.20, -0.15, -0.05, -0.50, -0.10],
    #    labels=['In1', 'In2', 'In3', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
    #    orientations=[-1, 1, 0, 1, 1, 1, 0, -1])

    sk.finish()
    # plt.tight_layout()
    ax.set_title("Percentage Central Apnea and FinalTx of Entire Dataset")
    ax.set_axis_off()
    plt.show()

def sankeyTypeOutcome(df):
    fig = plt.figure()  # container object
    ax = plt.axes() # the box we'll draw in

    dx_counts = df['BaseDx'].value_counts().sort_index()
    outcome_counts = df['Outcome'].value_counts() * -1.0
    x = dx_counts.get_values().sum()

    flow = dx_counts.get_values().tolist() + outcome_counts.get_values().tolist()
    label = dx_counts.index.tolist() + outcome_counts.index.tolist()

    sk = sankey.Sankey(ax, head_angle=120, offset=0.3, scale=1/float(x),
        unit=" patients", gap=0.6, margin=0.1,
        flows= flow,
        labels=label,
        orientations=[1, 0, -1, -1, 1, -1, 0, -1, 1])

    #sk.add(flows=[0.05, 0.05, 0.9, -0.20, -0.15, -0.05, -0.50, -0.10],
    #    labels=['In1', 'In2', 'In3', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
    #    orientations=[-1, 1, 0, 1, 1, 1, 0, -1])

    sk.finish()
    # plt.tight_layout()
    ax.set_title("Percentage Central Apnea and Outcome of Entire Dataset")
    ax.set_axis_off()
    plt.show()

def visualizations(df):
    #plt.style.use('seaborn-whitegrid')
    #fig = plt.figure()  # container object
    #ax = plt.axes() # the box we'll draw in
    sns.set()
    sns.set_palette("husl",3)
    ax = sns.catplot(x="Dx", y="Count", data=df, kind='bar')
    plt.title("Etiology of CSA; Multiple Contributors Allowed")
    ax.set_axis_labels("Etiology", "Number of Patients")

    # Severity of OSA by porcent CSAs and Sex
    #ax = sns.boxplot('BaseDx', 'AHI', hue='Sex', data=df)
    # Outcome by Base Dx as histograms
    # Todo: figure out how to normalize this
    # sns.catplot('BaseDx', hue='Outcome', kind='count', data=df)

    # Vis of distribution of AHIs
    # cleaned_df = df[df['AHI'].notnull()]
    # sns.distplot(cleaned_df['AHI'])
    plt.show()


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

    #sankeyTypeFinalTx(df)
    #visualizations(df)

    #pieChartBaseDx(df)
    printSumByBaseDx(df)

    post_dx_histo = histo_dx_includes(df)
    print("\n\n---Total of number of patients where each etiology was contributory---")
    print("---(will some to more than total given mutliple dx's)---\n")
    print(post_dx_histo)

    hist_df = pd.DataFrame({"Dx":post_dx_histo.index, "Count":post_dx_histo.data})
    visualizations(hist_df)

if __name__ == '__main__':
    main()
