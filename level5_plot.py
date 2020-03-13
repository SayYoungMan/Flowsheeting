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

def cs2hs1():
	#Values
	hs1_init = 355.13
	hs1_end = 157.50
	cs2_init = 180.63
	cs2_end = 137.50

	# HS1 Line
	plt.hlines(hs1_init, 0, 0.2, colors="red")
	plt.hlines(hs1_end, 0.8, 1, colors="red")
	plt.plot([0.2, 0.8], [hs1_init, hs1_end], color="red")

	# CS2 Line
	plt.hlines(cs2_init, 0, 0.2, colors="blue")
	plt.hlines(cs2_end, 0.8, 1, colors="blue")
	plt.plot([0.2, 0.8], [cs2_init, cs2_end], color="blue")

	# Draw Box
	plt.hlines(375, 0.2, 0.8, colors="black")
	plt.hlines(125, 0.2, 0.8, colors="black")
	plt.vlines(0.2, 125, 375, colors="black")
	plt.vlines(0.8, 125, 375, colors="black")

	# Texts
	plt.text(0.022, 360, '355.13°C', fontsize=12)
	plt.text(0.825, 123, '137.50°C', fontsize=12)
	plt.text(0.022, 185, '180.63°C', fontsize=12)
	plt.text(0.825, 162, '157.50°C', fontsize=12)

	# Arrow
	plt.annotate(s='', xy=(1.03, 162), xytext=(1.03, 133), arrowprops=dict(arrowstyle='<->'))
	plt.text(1.05, 143, r'$\Delta T_{out}=20°C$', fontsize=12)

	# Style
	plt.ylim([100, 400])
	plt.xlim([0, 1.2])
	plt.grid(False)
	plt.xticks([])
	plt.gca().spines['top'].set_visible(False)
	plt.gca().spines['right'].set_visible(False)
	plt.gca().spines['bottom'].set_visible(False)
	plt.ylabel("Temperatrue (°C)")
	plt.show()

cs2hs1()