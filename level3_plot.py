import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------Scenario comparison---------------------------------
def heating_method():
    df = pd.read_excel("Data/graphst to seyoung.xlsx", sheet_name="heating methods graphs", usecols='A:C').to_numpy()
    plt.plot(df[:,0], df[:,1]/1000000, label="Pump then Compress")
    plt.plot(df[:,0], df[:,2]/1000000, label="Heat then Compress")
    plt.ylabel("Opex (Million USD/yr)")
    plt.xlabel("Conversion (%)")
    plt.legend()
    plt.show()

def cost_optimal():
    df = pd.read_excel("Data/graphst to seyoung.xlsx", sheet_name="EP3 cost atoptimal capex & opex", usecols='A:B').to_numpy()
    plt.plot(df[:, 0], df[:, 1] / 1000000)
    plt.ylabel("Cost (Million USD/yr)")
    plt.xlabel("Conversion (%)")
    plt.show()

def ep3_optimal():
    df = pd.read_excel("Data/graphst to seyoung.xlsx", sheet_name="EP3", usecols='A:B').to_numpy()
    plt.plot(df[:, 0], df[:, 1] / 1000000)
    plt.hlines(0,0,100,linestyles="--")
    plt.ylabel("Cost (Million USD/yr)")
    plt.xlabel("Conversion (%)")
    plt.xlim([0, 25])
    plt.show()

cost_optimal()
ep3_optimal()
