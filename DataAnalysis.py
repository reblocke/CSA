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


def vis_hist_etio(df):
    post_dx_histo = histo_dx_includes(df)
    hist_df = pd.DataFrame({"Dx":post_dx_histo.index, "Count":post_dx_histo.data})
    sns.set()
    sns.set_palette("husl",3)
    ax = sns.catplot(x="Dx", y="Count", data=hist_df, kind='bar')
    plt.title("Etiology of CSA; Multiple Contributors Allowed")
    ax.set_axis_labels("Etiology", "Number of Patients")
    plt.show()


def sankeyEtioTx(df):
    SMALL_SIZE = 7
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    fig, axs = plt.subplots(3,2)
    fig.set_size_inches(15,11)
    fig.suptitle("Flow (Sankey) Diagram of Etiology of Central Apneas and Final Treatment, Separated by %Central Events")
    sankeySubPlot(axs[0,0], df, "All Patients w/ Dx of CSA")
    sankeyLegendPlot(axs[0,1])
    sankeySubPlot(axs[1,0], df.loc[df['BaseDx'] == "Mainly OSA"],
        "Patients w/ <10% CSAs")
    sankeySubPlot(axs[2,0], df.loc[df['BaseDx'] == "Combined OSA/CSA"],
        "Patients w/ 10-50% CSAs")
    sankeySubPlot(axs[1,1], df.loc[df['BaseDx'] == "Predominantly CSA"],
        "Patients w/ 50-90% CSAs")
    sankeySubPlot(axs[2,1], df.loc[df['BaseDx'] == "Pure CSA"],
        "Patients w/ >90% CSAs")
    axs[0,1].set_alpha(0.5)
    #plt.tight_layout()
    fig.savefig('test2png.png', dpi=100)
    plt.show()

def sankeyLegendPlot(ax):
    ax.set_title("Legend", fontsize=10)
    style = dict(size=7, color='grey')
    ax.text(1, -1,
     "Abbreviations:\n\
     \n\
     Etiologies\n\
     Prim = Primary CSA\n\
     OSA = Central events associated only with Obstructive events\n\
     TE = Treatment Emergent CSA\n\
     CV = CSA associated with HFrEF, HFpEF, or AFib\n\
     CNS = CSA associated with CVA, TBI, Mass Lesion,\n\
            Dementia, or Neurodegenerative disease\n\
     Med = CSA associated with high-dose opiate use\n\
     \n\
     Treatments\n\
     Final tx ASV = patients eventually treated using\n\
            Resmed/Respironics ASV, broken into flows by \n\
            prior traetment tried\n\
     O2 = treatment with supplemental oxygen only \n\
            (bleed-in not included)\n", ha="left", **style)
    sk = sankey.Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=100,
                    unit=' Patients')
    sk.add(flows=[25, 5, 60, -35, -25, -40],
               labels=['Etiology 1', 'Etiology 2', 'Etiology 3', 'Treatment 1', 'Treatment 2', 'Treatment 3'],
               orientations=[-1, 1, 0, 1, -1, 0],
               pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               patchlabel="All Patients\nn = 100\nArrow size corresponds to number patients",
               trunklength=2.0,
               facecolor='lightblue',
               alpha=0.5)  # Arguments to matplotlib.patches.PathPatch()
    sk.finish()
    ax.set_axis_off()

    return ax

def sankeySubPlot(ax, df, title):
    dx_counts = df['PostDx'].value_counts()
    dx_counts = dx_counts[dx_counts > 0]  # Drop labels with 0
    outcome_counts = df['FinalTx'].value_counts() * -1.0
    outcome_counts = outcome_counts[outcome_counts < 0]  # drop labels with 0
    x = dx_counts.get_values().sum()
    #print(dx_counts)
    #print(outcome_counts)

    flow = dx_counts.get_values().tolist() + outcome_counts.get_values().tolist()
    label = dx_counts.index.tolist() + outcome_counts.index.tolist()
    orientation = [0]  # Generate alternating 1, -1 for inputs / outputs
    pathlength = [0.25]
    for i in range(len(flow) - 1):
        if i == len(dx_counts)-1:  # 1st outcome
            orientation.append(0)
            pathlength.append(0.25)
        else:
            if i%2 == 1:
                orientation.append(1)
                if (i//2)%2 == 0:  # alternate (per side) pathlengths
                    pathlength.append(0.5)
                else:
                    pathlength.append(0.15)
            else:
                orientation.append(-1)
                if (i//2)%2 == 0:
                    pathlength.append(0.5)
                else:
                    pathlength.append(0.15)
    asvIndex = label.index("asv")
    label[asvIndex] = ""  # because this will be connected to sub-sankey

    sk = sankey.Sankey(ax, head_angle=120, offset=0.3, scale=1/float(x),
        unit="", gap=0.5, margin=0.1)
    sk.add(flows= flow,
        labels=label,
        orientations=orientation,
        pathlengths=pathlength,
        patchlabel=title,
        trunklength=2.0,
        facecolor='lightblue',
        alpha=0.75)

    # Create ASV subdigram
    ASV_df = df.loc[df['FinalTx'] == "asv"]
    ASV_dx_count = abs(flow[asvIndex])
    ASV_path_counts = ASV_df['ProcToASV'].value_counts() * -1.0
    ASV_flow = [ASV_dx_count]
    ASV_flow = ASV_flow + ASV_path_counts.tolist()
    ASV_label = [""]
    ASV_label = ASV_label + ASV_path_counts.index.tolist()
    ASV_orientation = [orientation[asvIndex] * -1, 0]  # start w/ ASV, opp
    ASV_pathlength = [1.0, 0.25]  # largest outcome straight

    for i in range(len(ASV_flow) - 2):
        if i%2 == 1:
            ASV_orientation.append(1)
            if (i//2)%2 == 0:  # alternate (per side) pathlengths
                ASV_pathlength.append(0.5)
            else:
                ASV_pathlength.append(0.15)
        else:
            ASV_orientation.append(-1)
            if (i//2)%2 == 0:
                ASV_pathlength.append(0.5)
            else:
                ASV_pathlength.append(0.15)

    sk.add(flows= ASV_flow,
        labels= ASV_label,
        orientations= ASV_orientation,
        pathlengths= ASV_pathlength,
        prior = 0,
        connect = (asvIndex, 0),
        patchlabel=" Final tx ASV",
        trunklength= 1.6,
        facecolor='lightyellow',
        alpha=.75)

    # Todo: add trunk, clean db (N/A proc to ASV), add legend, make diagrams stratified by %CSA

    sk.finish()
    # plt.tight_layout()
    ax.set_axis_off()
    return ax


def visualizations(df):
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()  # container object
    ax = plt.axes() # the box we'll draw in
    #sns.set()
    #sns.set_palette("husl",3)

    # Severity of OSA by percent CSAs and Sex
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
    #vis_hist_etio(df)

    #pieChartBaseDx(df)
    printSumByBaseDx(df)

    print("\n\n---Total of number of patients where each etiology was contributory---")
    print("---(will some to more than total given mutliple dx's)---\n")

    #visualizations(df)
    sankeyEtioTx(df)

if __name__ == '__main__':
    main()
