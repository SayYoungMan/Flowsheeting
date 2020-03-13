import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#--------------- Style ---------------------
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 15
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 15
plt.rcParams['legend.fancybox'] = True
plt.rcParams['legend.shadow'] = True
plt.rcParams['lines.linewidth'] = 2

# -------------------------------Scenario comparison---------------------------------
# Import data
def scenario():
    in_out = pd.read_excel("Data/level-2-4-case-comparison-730K.xlsx", usecols='B:C', skiprows=3, nrows=98).to_numpy()
    rec_only = pd.read_excel("Data/level-2-4-case-comparison-730K.xlsx", usecols='E:F', skiprows=2, nrows=98).to_numpy()
    pmfuel = pd.read_excel("Data/level-2-4-case-comparison-730K.xlsx", usecols='H:I', skiprows=2, nrows=98).to_numpy()
    mefuel = pd.read_excel("Data/level-2-4-case-comparison-730K.xlsx", usecols='K:L', skiprows=2, nrows=98).to_numpy()
    ep1 = 32.5528301886792

    # Plot Graph
    fig, ax = plt.subplots(2, 1)
    ax[1].plot(in_out[:,1], in_out[:,0]/1000000, label="In/Out (Case 1)", color="darkorange", linewidth=3.5)
    ax[0].plot(rec_only[:,1], rec_only[:,0]/1000000, label="Recycle Only (Case 2)", color="forestgreen", linewidth=3.5)
    ax[1].plot(rec_only[:,1], rec_only[:,0]/1000000, label="Recycle Only (Case 2)", color="forestgreen", linewidth=3.5)
    ax[1].plot(mefuel[:,1], mefuel[:,0]/1000000, label = "Toluene Recycle + Methanol Fuel (Case 3)", color = "crimson", linewidth=3.5)
    ax[0].plot(pmfuel[:,1], pmfuel[:,0]/1000000, label="Recycle + Xylene Fuel (Case 4)", color = "royalblue", linewidth=3.5)
    ax[1].plot(pmfuel[:, 1], pmfuel[:,0]/1000000, label="Recycle + Xylene Fuel (Case 4)", color="royalblue", linewidth=3.5)
    ax[0].set_ylim([0, 40])
    ax[0].set_xlim([0.025, 0.35])
    ax[0].set_xticklabels([])
    ax[0].xaxis.set_tick_params(labelsize=25)
    ax[0].yaxis.set_tick_params(labelsize=25)
    ax[1].xaxis.set_tick_params(labelsize=25)
    ax[1].yaxis.set_tick_params(labelsize=25)
    ax[1].set_ylim([-1000, 0])
    ax[1].set_xlim([0.025, 0.35])
    ax[0].axhline(ep1, linestyle='--', color='black', label='EP1', linewidth=3.5)
    ax[1].axhline(ep1, linestyle='--', color='black', label='EP1')
    ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.3), ncol=3, fancybox=True, shadow=True, fontsize=25)
    fig.text(0.04, 0.5, "Economic Potential (Million USD/yr)", va='center', rotation='vertical', fontsize=30, fontweight='bold')
    fig.text(0.5, 0.04, "Conversion", ha='center', fontsize=30, fontweight='bold')
    plt.subplots_adjust(hspace=0)
    plt.show()


# -------------------------------Temperature comparison---------------------------------
# Import data
def temperature():
    temp_730 = pd.read_excel("Data/level-2-temperature-comparison-final.xlsx", sheet_name="Sheet5", usecols='B:C', skiprows=2).to_numpy()
    temp_760 = pd.read_excel("Data/level-2-temperature-comparison-final.xlsx", sheet_name="Sheet5", usecols='E:F', skiprows=2).to_numpy()
    temp_790 = pd.read_excel("Data/level-2-temperature-comparison-final.xlsx", sheet_name="Sheet5", usecols='H:I', skiprows=2).to_numpy()
    temp_820 = pd.read_excel("Data/level-2-temperature-comparison-final.xlsx", sheet_name="Sheet5", usecols='K:L', skiprows=2).to_numpy()

    #Plot Graph
    plt.plot(temp_730[:,1], temp_730[:,0]/1000000, label="730K")
    plt.plot(temp_760[:,1], temp_760[:,0]/1000000, label="760K")
    plt.plot(temp_790[:,1], temp_790[:,0]/1000000, label="790K")
    plt.plot(temp_820[:,1], temp_820[:,0]/1000000, label="820K")
    plt.hlines(0,0,100,linestyles="--")
    #plt.title("EP Comparison of Different Temperatures")
    plt.ylabel("Economic Potential (Million USD/yr)")
    plt.xlabel("Conversion")
    plt.legend()
    plt.ylim([-40, 40])
    plt.xlim([0, 0.43])
    plt.show()


# -------------------------------Pressure comparison---------------------------------
# Import data
def pressure():
    pres_1 = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Pressure comparison", usecols='B:C', skiprows=2, nrows=97).to_numpy()
    pres_5 = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Pressure comparison", usecols='E:F', skiprows=2, nrows=99).to_numpy()
    pres_10 = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Pressure comparison", usecols='H:I', skiprows=2, nrows=99).to_numpy()

    #Plot Graph
    plt.plot(pres_1[:,1], pres_1[:,0]/1000000, label="1 bar")
    plt.plot(pres_5[:,1], pres_5[:,0]/1000000, label="5 bar")
    plt.plot(pres_10[:,1], pres_10[:,0]/1000000, label="10 bar")
    plt.hlines(0,0,100,linestyles="--")
    #plt.title("EP Comparison of Different Pressures")
    plt.ylabel("Economic Potential (Million USD/yr)")
    plt.xlabel("Conversion")
    plt.legend()
    plt.xlim([0.05, 0.45])
    plt.ylim([-50, 40])
    plt.show()

'''
# -------------------------------Feed Ratio comparison---------------------------------
# Import data
fr1 = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Pressure comparison", usecols='B:C', skiprows=2, nrows=97).to_numpy()
fr2 = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Pressure comparison", usecols='E:F', skiprows=2, nrows=99).to_numpy()
fr3 = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Pressure comparison", usecols='H:I', skiprows=2, nrows=99).to_numpy()

#Plot Graph
plt.figure(3)
plt.plot(pres_1[:,1], pres_1[:,0]/1000000, label="1 bar")
plt.plot(pres_5[:,1], pres_5[:,0]/1000000, label="5 bar")
plt.plot(pres_10[:,1], pres_10[:,0]/1000000, label="10 bar")
plt.title("EP Comparison of Different Pressures")
plt.ylabel("Economic Potential (Million USD/yr)")
plt.xlabel("Conversion")
plt.legend()
plt.xlim([0.05, 0.45])
plt.ylim([-50, 40])
plt.show()
'''

# -------------------------------Feed Ratio comparison with EP---------------------------------
def feed_ratio_ep():
    one = pd.read_excel("Data/LEVEL 3 excel.xlsx", sheet_name="EP2 vary feed ratio", usecols='A:B', nrows=20).to_numpy()
    two = pd.read_excel("Data/LEVEL 3 excel.xlsx", sheet_name="EP2 vary feed ratio", usecols='A:B', nrows=13, skiprows=23).to_numpy()
    three = pd.read_excel("Data/LEVEL 3 excel.xlsx", sheet_name="EP2 vary feed ratio", usecols='A:B', nrows=11, skiprows=39).to_numpy()
    four = pd.read_excel("Data/LEVEL 3 excel.xlsx", sheet_name="EP2 vary feed ratio", usecols='A:B', nrows=10, skiprows=53).to_numpy()

    plt.plot(one[:, 0] / 100, one[:, 1] / 1000000, label="MeOH 1:1 Tol")
    plt.plot(two[:, 0] / 100, two[:, 1] / 1000000, label="MeOH 1:2 Tol")
    plt.plot(three[:, 0] / 100, three[:, 1] / 1000000, label="MeOH 1:3 Tol")
    plt.plot(four[:, 0] / 100, four[:, 1] / 1000000, label="MeOH 1:4 Tol")

    plt.hlines(0,0,100,linestyles="--")
    plt.ylabel("Economic Potential (Million USD/yr)")
    plt.xlabel("Conversion")
    plt.xlim([0.025, 0.25])
    plt.ylim([-45, 35])
    plt.legend()
    plt.show()

#------------------------------Selectivity vs Conversion------------------------------
def sel_conv():
    df = pd.read_excel("Data/level 2 selec vs convo.xlsx", sheet_name="Sheet2", usecols='B:I', skiprows=1).to_numpy()
    plt.plot(df[:, 0], df[:, 1], label="730K")
    plt.plot(df[:, 6], df[:, 7], label="750K")
    plt.plot(df[:, 3], df[:, 4], label="770K")
    plt.ylabel("Selectivity")
    plt.xlabel("Conversion")
    plt.legend(loc='lower left')
    plt.show()


scenario()