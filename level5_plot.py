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

#--------------- Distillation -----------------
def CI():
	GCC = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AE:AF', skiprows=1, nrows=20).to_numpy()
	D2 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AC:AD', skiprows=25, nrows=4).to_numpy()
	D3 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AF:AG', skiprows=25, nrows=4).to_numpy()
	D4 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AI:AJ', skiprows=25, nrows=4).to_numpy()
	D5 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AC:AD', skiprows=31, nrows=4).to_numpy()
	D6 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AF:AG', skiprows=31, nrows=4).to_numpy()
	D10 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AI:AJ', skiprows=31, nrows=4).to_numpy()

	plt.rcParams['axes.labelsize'] = 30
	plt.rcParams['xtick.labelsize'] = 25
	plt.rcParams['ytick.labelsize'] = 25
	plt.rcParams['legend.fontsize'] = 28
	plt.rcParams['lines.linewidth'] = 3.5
	plt.rcParams['lines.markersize'] = 10

	plt.plot(GCC[:, 1], GCC[:, 0], marker='o', label="Grand Composite Curve")
	plt.plot(D2[:, 1], D2[:, 0], marker='o', label="DIST-2")
	plt.plot(D3[:, 1], D3[:, 0], marker='o', label="DIST-3")
	plt.plot(D4[:, 1], D4[:, 0], marker='o', label="DIST-4")
	plt.plot(D5[:, 1], D5[:, 0], marker='o', label="DIST-5")
	plt.plot(D6[:, 1], D6[:, 0], marker='o', label="DIST-6")
	plt.plot(D10[:, 1], D10[:, 0], marker='o', label="DIST-10")

	plt.xlabel("Enthalpy (kW)")
	plt.xlim([0, 60000])
	plt.ylabel("Temperatrue (°C)")
	plt.legend()

	plt.show()

def CI_zoom():
	GCC = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AE:AF', skiprows=1, nrows=20).to_numpy()
	D2 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AC:AD', skiprows=25, nrows=4).to_numpy()
	D3 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AF:AG', skiprows=25, nrows=4).to_numpy()
	D4 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AI:AJ', skiprows=25, nrows=4).to_numpy()
	D5 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AC:AD', skiprows=31, nrows=4).to_numpy()
	D6 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AF:AG', skiprows=31, nrows=4).to_numpy()
	D10 = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="DISTILLATION", usecols='AI:AJ', skiprows=31, nrows=4).to_numpy()

	plt.plot(GCC[:, 1], GCC[:, 0], marker='o', label="Grand Composite Curve")
	plt.plot(D2[:, 1], D2[:, 0], marker='o', label="DIST-2")
	plt.plot(D3[:, 1], D3[:, 0], marker='o', label="DIST-3")
	plt.plot(D4[:, 1], D4[:, 0], marker='o', label="DIST-4")
	plt.plot(D5[:, 1], D5[:, 0], marker='o', label="DIST-5")
	plt.plot(D6[:, 1], D6[:, 0], marker='o', label="DIST-6")
	plt.plot(D10[:, 1], D10[:, 0], marker='o', label="DIST-10")

	plt.xlabel("Enthalpy (kW)")
	plt.xlim([0, 2500])
	plt.ylabel("Temperatrue (°C)")
	plt.ylim([50, 180])

	plt.show()

def HC3():
	df = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="HEAT and COOL 3", usecols='M:N', skiprows=40, nrows=20).to_numpy()

	plt.plot(df[:, 1], df[:, 0], marker='o')
	plt.xlabel("Enthalpy (kW)")
	plt.ylabel("Temperatrue (°C)")
	plt.show()

def HC4():
	df = pd.read_excel("Data/Heat Integration Calculation.xlsx", sheet_name="HEAT and COOL 4", usecols='M:N', skiprows=54, nrows=28).to_numpy()

	plt.plot(df[:, 1], df[:, 0], marker='o')
	plt.xlabel("Enthalpy (kW)")
	plt.ylabel("Temperatrue (°C)")
	plt.show()

CI_zoom()