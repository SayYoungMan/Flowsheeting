import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------Scenario comparison---------------------------------
# Import data
in_out = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Compariso of 4 case", usecols='B:C', skiprows=2, nrows=97).to_numpy()
rec_only = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Compariso of 4 case", usecols='E:F', skiprows=2, nrows=97).to_numpy()
pmfuel = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Compariso of 4 case", usecols='H:I', skiprows=2, nrows=97).to_numpy()
mefuel = pd.read_excel("Data/level 2 plots.xlsx", sheet_name="Compariso of 4 case", usecols='K:L', skiprows=2, nrows=97).to_numpy()
ep1 = 32552830.1886792

# Plot Graph
plt.plot(in_out[:,1], in_out[:,0])
plt.plot(rec_only[:,1], rec_only[:,0])
plt.plot(pmfuel[:,1], pmfuel[:,0])
plt.plot(mefuel[:,1], mefuel[:,0])
plt.title("EP Comparison of 4 Scenarios")
plt.ylabel("Economic Potential ($/yr)")
plt.xlabel("Conversion")
ticks = np.array([50000000, 40000000, 30000000, 20000000, 10000000, 0]); a = np.arange(6)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), useMathText=True)
plt.show()