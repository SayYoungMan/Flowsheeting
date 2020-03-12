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

#---------------- Graphs ------------------
def heating_method():
    PMC = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet3", usecols='B:J').to_numpy()
    HTC = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet2", usecols='B:R').to_numpy()
    plt.plot(PMC[:,0] / 100, PMC[:,8]/1000000, label="Pump then Heat")
    plt.plot(HTC[:,0] / 100, HTC[:,5]/1000000, label="Heat then Compress")
    plt.ylabel("Opex (Million USD/yr)")
    plt.xlabel("Conversion")
    plt.legend()
    plt.show()

def optimal():
    plt.rcParams['axes.labelsize'] = 16
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['xtick.labelsize'] = 16
    plt.rcParams['ytick.labelsize'] = 16
    plt.rcParams['legend.fontsize'] = 17
    fig, ax = plt.subplots(1, 2)
    df1 = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet2", usecols='B:R').to_numpy()
    ax[0].plot(df1[:, 0] / 100, df1[:, 14] / 1000000)
    ax[0].set_ylabel("Cost (Million USD/yr)")
    ax[0].set_xlabel("Conversion")
    df2 = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet2", usecols='B:R').to_numpy()
    ax[1].plot(df2[:, 0] / 100, df2[:, 16] / 1000000)
    ax[1].axhline(0,0,100, linestyle="--", color="black")
    ax[1].set_ylabel("Economic Potential (Million USD/yr)")
    ax[1].set_xlabel("Conversion")
    ax[1].set_xlim([0, 0.25])
    plt.subplots_adjust(wspace=0.5)
    plt.show()


def cost_optimal():
    df = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet2", usecols='B:R').to_numpy()
    plt.plot(df[:, 0] / 100, df[:, 14] / 1000000)
    plt.ylabel("Cost (Million USD/yr)")
    plt.xlabel("Conversion")
    plt.show()

def ep3_optimal():
    df = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet2", usecols='B:R').to_numpy()
    plt.plot(df[:, 0] / 100, df[:, 16] / 1000000)
    plt.hlines(0,0,100,linestyles="--")
    plt.ylabel("Economic Potential (Million USD/yr)")
    plt.xlabel("Conversion")
    plt.xlim([0, 0.25])
    plt.show()

def ep3_no_heat():
    df = pd.read_excel("Data/new graph seyoung 06032020 (1).xlsx", sheet_name="Sheet2", usecols='B:T').to_numpy()
    plt.plot(df[:, 0] / 100, df[:, 18] / 1000000)
    plt.ylabel("Economic Potential (Million USD/yr)")
    plt.xlabel("Conversion")
    plt.xlim([0, 0.26])
    plt.show()

def ada_iso():
    df = pd.read_excel("Data/Adiabatic vs isothermal.xlsx", sheet_name="Summary", usecols='D:K', skiprows=2)
    iso = pd.read_excel("Data/Adiabatic vs isothermal.xlsx", sheet_name="Summary", usecols='M:O', skiprows=1).to_numpy()

    cov = df.loc[0].to_numpy().reshape(-1) / 100
    sixsix = df.loc[4].to_numpy().reshape(-1)
    sixeight = df.loc[5].to_numpy()
    sevenzero = df.loc[6].to_numpy()
    seventwo = df.loc[7].to_numpy()
    sevenfour = df.loc[9].to_numpy()
    sevensix = df.loc[10].to_numpy()
    seveneight = df.loc[11].to_numpy()

    plt.plot(cov, sixsix / 1000000, label="660K", color = 'blue')
    plt.plot(cov, sixeight / 1000000, label="680K", color = 'aqua')
    plt.plot(cov, sevenzero / 1000000, label="700K", color = 'darkgreen')
    plt.plot(cov, seventwo / 1000000, label="720K", color = 'limegreen')
    plt.plot(cov, sevenfour / 1000000, label="740K", color = 'yellow')
    plt.plot(cov, sevensix / 1000000, label="760K", color = 'darkorange')
    plt.plot(cov, seveneight / 1000000, label="780K", color = 'red')

    plt.plot(iso[:, 2] / 100, iso[:, 0] / 1000000, linestyle='--', label="Isothermal", color = 'indigo')
    plt.hlines(0,0,100,linestyles="-")
    plt.legend(loc = 'lower left')
    plt.xlim([0, 0.30])
    plt.ylim([-25, 35])
    plt.ylabel("Economic Potential (Million USD/yr)")
    plt.xlabel("Conversion")
    plt.show()


heating_method()