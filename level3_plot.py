import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------Scenario comparison---------------------------------
def heating_method():
    PMC = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet3", usecols='B:J').to_numpy()
    HTC = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet2", usecols='B:R').to_numpy()
    plt.plot(PMC[:,0], PMC[:,8]/1000000, label="Pump then Compress")
    plt.plot(HTC[:,0], HTC[:,5]/1000000, label="Heat then Compress")
    plt.ylabel("Opex (Million USD/yr)")
    plt.xlabel("Conversion (%)")
    plt.legend()
    plt.show()

def cost_optimal():
    df = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet2", usecols='B:R').to_numpy()
    plt.plot(df[:, 0], df[:, 14] / 1000000)
    plt.ylabel("Cost (Million USD/yr)")
    plt.xlabel("Conversion (%)")
    plt.show()

def ep3_optimal():
    df = pd.read_excel("Data/new graph seyoung 04032020.xlsx", sheet_name="Sheet2", usecols='B:R').to_numpy()
    plt.plot(df[:, 0], df[:, 16] / 1000000)
    plt.hlines(0,0,100,linestyles="--")
    plt.ylabel("Economic Potential (Million USD/yr)")
    plt.xlabel("Conversion (%)")
    plt.xlim([0, 25])
    plt.show()

def ada_iso():
    ada = pd.read_excel("Data/Adiabatic vs isothermal.xlsx", sheet_name="Summary", usecols='C:K', skiprows=3).to_numpy()
    iso = pd.read_excel("Data/Adiabatic vs isothermal.xlsx", sheet_name="Summary", usecols='M:O', skiprows=1).to_numpy()



heating_method()
