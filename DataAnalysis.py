from ReadExcel import *
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.sankey as sankey
import matplotlib.gridspec as gridspec
import pandas as pd

def summary_stats(df):

    print("\nAge Summary Statistics:\n")
    print(str(df['Age'].describe()))

    print("\nSex Summary Statistics:\n")
    print(str(df['Sex'].value_counts()))

    print("\nBMI Summary Statistics:\n")
    print(str(df['BMI'].describe()))

    print("\nAHI Summary Statistics:\n")
    print(str(df['AHI'].describe()))

    print("\nBase Dx Counts:\n")
    print(str(df['BaseDx'].value_counts()))

    print("\nEtiology Counts:\n")
    print(str(df['PostDx'].value_counts()))

    print("\nFinal Treatment Counts:\n")
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

    sk = sankey.Sankey(ax, head_angle=120, offset=0.25, scale=1/float(x),
        unit=" patients", gap=0.9, margin=0.05,
        flows= flow,
        labels=label,
        orientations=[1, 0, -1, -1, 1, -1, 0, -1, 1, -1])

    sk.finish()
    # plt.tight_layout()
    ax.set_title("Percentage Central Apnea and Outcome of Entire Dataset")
    ax.set_axis_off()
    plt.show()


def vis_hist_etio(df):
    post_dx_histo = histo_dx_includes(df)
    hist_df = pd.DataFrame({"Dx":post_dx_histo.index, "Count":post_dx_histo.data})
    print(hist_df)
    hist_df = hist_df.drop(1)
    sns.set()
    sns.set_palette("husl",3)
    ax = sns.catplot(x="Dx", y="Count", data=hist_df, kind='bar')
    plt.title("Etiology of CSA; Multiple Contributors Allowed")
    ax.set_axis_labels("Etiologies of Central Sleep Apnea", "Number of Patients")
    plt.legend()
    plt.show()


def sankeyEtioTx(df):
    SMALL_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 14

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    #fig, axs = plt.subplots(4,2)
    fig = plt.figure()
    spec = gridspec.GridSpec(ncols=2, nrows=5, figure=fig)

    f_ax1 = fig.add_subplot(spec[:-3, :])
    #f_ax2 = fig.add_subplot(spec[0, 1])
    f_ax3 = fig.add_subplot(spec[2, 0])
    f_ax4 = fig.add_subplot(spec[2, 1])
    f_ax5 = fig.add_subplot(spec[3, 0])
    f_ax6 = fig.add_subplot(spec[3, 1])
    f_ax7 = fig.add_subplot(spec[4, 0])
    f_ax8 = fig.add_subplot(spec[4, 1])

    fig.set_size_inches(18,11)
    fig.suptitle("Flow (Sankey) Diagram of Etiology of Central Apneas and Final Treatment, Separated by %Central Events")

    sankeySubPlot(f_ax1, df, "All Patients with a diagnosis including CSA")

    #f_ax3.set_title("Mainly OSA", fontsize=10)
    sankeySubPlot(f_ax3, df.loc[df['BaseDx'] == "Mainly OSA"],
        "<10% CSAs")
    #f_ax5.set_title("Combined OSA/CSA", fontsize=10)
    sankeySubPlot(f_ax5, df.loc[df['BaseDx'] == "Combined OSA/CSA"],
        "10-50% CSAs")
    #f_ax4.set_title("Predominantly CSA", fontsize=10)
    sankeySubPlot(f_ax4, df.loc[df['BaseDx'] == "Predominantly CSA"],
        "50-90% CSAs")
    #f_ax6.set_title("Pure CSA", fontsize=10)
    sankeySubPlot(f_ax6, df.loc[df['BaseDx'] == "Pure CSA"],
        ">90% CSAs")

    #Make Legend + Abbreviations
    sankeyLegendPlot(f_ax7)

    f_ax8.set_title("Abbreviations", fontsize=10)
    style = dict(size=7, color='black')
    f_ax8.text(0.1, -0.1,
     "Etiologies\n\
     Prim = Primary CSA\n\
     OSA = Central events associated only with Obstructive events\n\
     TE = Treatment Emergent CSA\n\
     CV = CSA associated with HFrEF, HFpEF, or AFib\n\
     CNS = CSA associated with CVA, TBI, Mass Lesion, Dementia, or Neurodegenerative disease\n\
     Med = CSA associated with high-dose opiate use\n\
     \n\
Treatments\n\
     Final tx ASV = patients eventually treated using Resmed/Respironics ASV, broken into flows by prior traetment tried\n\
     O2 = treatment with supplemental oxygen only (bleed-in not included)\n",
     ha="left", **style)
    f_ax8.set_axis_off()
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig('test2png.png', dpi=100)
    #plt.show()

def sankeyLegendPlot(ax):
    ax.set_title("Legend", fontsize=10)
    sk = sankey.Sankey(ax=ax, scale=0.01, offset=0.3, head_angle=100,
                    unit=' Patients')
    sk.add(flows=[25, 5, 60, -35, -25, -40],
               labels=['Etiology 1', 'Etiology 2', 'Etiology 3 (Most Common)', 'Treatment 1', 'Treatment 2', 'Treatment 3 (most common)'],
               orientations=[-1, 1, 0, 1, -1, 0],
               pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               patchlabel="All Patients\nn = 100\nRelative arrow size corresponds \nto proportion of patients",
               trunklength=5.0,
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
                    pathlength.append(0.85)
                else:
                    pathlength.append(0.15)
            else:
                orientation.append(-1)
                if (i//2)%2 == 0:
                    pathlength.append(0.85)
                else:
                    pathlength.append(0.15)
    asvIndex = label.index("asv")
    label[asvIndex] = ""  # because this will be connected to sub-sankey

    sk = sankey.Sankey(ax, head_angle=120, offset=0.3, scale=1/float(x),
        unit="", gap=1.6, margin=0.05)
    sk.add(flows= flow,
        labels=label,
        orientations=orientation,
        pathlengths=pathlength,
        patchlabel=title + "\nn = " + str(x)+" patients",
        trunklength=6.0,
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
            if (i//2)%2 == 1:  # alternate (per side) pathlengths
                ASV_pathlength.append(0.5)
            else:
                ASV_pathlength.append(0.15)
        else:
            ASV_orientation.append(-1)
            if (i//2)%2 == 1:
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
        trunklength= 4.5,
        facecolor='lightyellow',
        alpha=.75)

    sk.finish()
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

    print("\n\n----AMONG PATIENTS WITH PURE CSA (MORE THAN 90%)----\n")
    CSA_pure = df.loc[df['BaseDx'] == "Pure CSA"]
    summary_stats(CSA_pure)

    print("\n\n----AMONG PATIENTS WITH PREDOMINANTLY CSA (50 - 90%)----\n")
    CSA_predom = df.loc[df['BaseDx'] == "Predominantly CSA"]
    summary_stats(CSA_predom)

    print("\n\n----AMONG PATIENTS WITH Combined OSA/CSA (10 - 50% CSA)-----")
    OSA_predom = df.loc[df['BaseDx'] == "Mainly OSA"]
    summary_stats(OSA_predom)

    print("\n\n----AMONG PATIENTS WITH PURE OSA (< 10% CSA)-----")
    OSA_pure = df.loc[df['BaseDx'] == "Combined OSA/CSA"]
    summary_stats(OSA_pure)

    # print("\n\n----AMONG PATIENTS WITH PREDOMINANTLY CSA (MORE THAN 50%)----\n")
    # summary_stats(pd.merge(CSA_predom, CSA_pure, how='outer'))
    # print("\n\n----AMONG PATIENTS WITH < 50% CSA-----")
    # summary_stats(pd.merge(OSA_predom, OSA_pure, how='outer'))




def main():
    # Location of Db file
    db_loc = "/Users/reblocke/Box/Residency Personal Files/Scholarly Work/CSA/Databases/CSA-Db-Working.xlsm"
    df = arrays_to_df(sheet_to_arrays(load_sheet(db_loc)))

    # ['ID', 'Age', 'Sex', 'BMI', 'AHI', 'BaseDx', 'PostDx', 'FinalTx', 'Outcome',
    # "ProcToASV", "TimeToASV]
    df.to_excel('output.xlsx')

    #sankeyTypeFinalTx(df)
    # vis_hist_etio(df)

    #pieChartBaseDx(df)
    printSumByBaseDx(df)

    #print("\n\n---Total of number of patients where each etiology was contributory---")
    #print("---(will some to more than total given mutliple dx's)---\n")

    #visualizations(df)
    #sankeyEtioTx(df)
    #sankeyTypeFinalTx(df)
    #sankeyTypeOutcome(df)

if __name__ == '__main__':
    main()
