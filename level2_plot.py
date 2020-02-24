import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------Scenario comparison---------------------------------
# Import data
def scenario():
    in_out = pd.read_excel("Data/level-2-4-case-comparison-730K.xlsx", usecols='B:C', skiprows=3, nrows=98).to_numpy()
    rec_only = pd.read_excel("Data/level-2-4-case-comparison-730K.xlsx", usecols='E:F', skiprows=2, nrows=98).to_numpy()
    pmfuel = pd.read_excel("Data/level-2-4-case-comparison-730K.xlsx", usecols='H:I', skiprows=2, nrows=98).to_numpy()
    mefuel = pd.read_excel("Data/level-2-4-case-comparison-730K.xlsx", usecols='K:L', skiprows=2, nrows=98).to_numpy()
    ep1 = 32552830.1886792

    # Plot Graph
    plt.figure(1)
    fig, ax = plt.subplots(2, 1)
    ax[1].plot(in_out[:,1], in_out[:,0]/1000000, label="In/Out", color="darkorange")
    ax[0].plot(rec_only[:,1], rec_only[:,0]/1000000, label="Recycle Only", color="forestgreen")
    ax[1].plot(rec_only[:,1], rec_only[:,0]/1000000, label="Recycle Only", color="forestgreen")
    ax[0].plot(pmfuel[:,1], pmfuel[:,0]/1000000, label="Recycle + Xylene Fuel", color = "royalblue")
    ax[1].plot(pmfuel[:, 1], pmfuel[:,0]/1000000, label="Recycle + Xylene Fuel", color="royalblue")
    ax[1].plot(mefuel[:,1], mefuel[:,0]/1000000, label = "Methanol Fuel", color = "crimson")
    ax[0].set_ylim([0, 40])
    ax[0].set_xlim([0, 0.4])
    ax[0].set_xticks([])
    ax[1].set_ylim([-1000, 0])
    ax[1].set_xlim([0, 0.4])
    fig.suptitle('Comparison of Different Scenarios')
    fig.text(0.04, 0.5, "Economic Potential (Million USD/yr)", va='center', rotation='vertical')
    fig.text(0.5, 0.04, "Conversion", ha='center')
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
    plt.figure(2)
    plt.plot(temp_730[:,1], temp_730[:,0]/1000000, label="730K")
    plt.plot(temp_760[:,1], temp_760[:,0]/1000000, label="760K")
    plt.plot(temp_790[:,1], temp_790[:,0]/1000000, label="790K")
    plt.plot(temp_820[:,1], temp_820[:,0]/1000000, label="820K")
    plt.title("EP Comparison of Different Temperatures")
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

scenario()