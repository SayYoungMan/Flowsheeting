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
def f1():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="Flashes", usecols='A:H', skiprows=1).to_numpy()
	plt.plot(df[:, 0], df[:, 6]*100, label="Ethylene Distillate")
	plt.plot(df[:, 0], df[:, 7]*100, label="Methanol Recovery")
	plt.ylabel("Recovery (%)")
	plt.xlabel("Temperatrue (°C)")
	plt.legend()
	plt.show()

def f2():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="Flashes", usecols='K:R', skiprows=1).to_numpy()
	plt.plot(df[:, 0], df[:, 6]*100, label="Ethylene Distillate")
	plt.plot(df[:, 0], df[:, 7]*100, label="Methanol Recovery")
	plt.ylabel("Recovery (%)")
	plt.xlabel("Temperatrue (°C)")
	plt.legend()
	plt.show()

def dec():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="Decanter", usecols='A:N', skiprows=1).to_numpy()
	plt.plot(df[:, 0], df[:, 10]*100, label="Water Recovery")
	plt.plot(df[:, 0], df[:, 11]*100, label="Toluene Recovery")
	plt.plot(df[:, 0], df[:, 12]*100, label="P-Xylene Recovery")
	plt.plot(df[:, 0], df[:, 13]*100, label="Benzene Recovery")
	plt.ylabel("Recovery (%)")
	plt.xlabel("Temperatrue (°C)")
	plt.legend()
	plt.show()

def dis1():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="AqueDis", usecols='A:N', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df[:, 0], df[:, 5]*100, label="Water Recovery")
	ax[0].plot(df[:, 0], df[:, 6]*100, label="Methanol Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df[:, 7], df[:, 12]*100, label="Water Recovery")
	ax[1].plot(df[:, 7], df[:, 13]*100, label="Methanol Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.9), ncol=2)
	plt.subplots_adjust(hspace=0.5)
	plt.show()

def dis3():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="AqueDis", usecols='O:AB', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df[:, 0], df[:, 5]*100, label="Water Recovery")
	ax[0].plot(df[:, 0], df[:, 6]*100, label="Methanol Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df[:, 7], df[:, 12]*100, label="Water Recovery")
	ax[1].plot(df[:, 7], df[:, 13]*100, label="Methanol Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.9), ncol=2)
	plt.subplots_adjust(hspace=0.5)
	plt.show()

def dis2():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="OrgDis", usecols='A:N', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df[:, 0], df[:, 5]*100, label="Toluene Recovery")
	ax[0].plot(df[:, 0], df[:, 6]*100, label="P-Xylene Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df[:, 7], df[:, 12]*100, label="Toluene Recovery")
	ax[1].plot(df[:, 7], df[:, 13]*100, label="P-Xylene Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.9), ncol=2)
	plt.subplots_adjust(hspace=0.5, left = 0.15)
	plt.show()

def dis4():
	df1 = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="XyDis", usecols='A:M', skiprows=1).to_numpy()
	df2 = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="XyDis", usecols='O:AA', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df1[:, 0], df1[:, 9]*100, label="Toluene Recovery")
	ax[0].plot(df1[:, 0], df1[:, 10]*100, label="P-Xylene Recovery")
	ax[0].plot(df1[:, 0], df1[:, 11]*100, label="M-Xylene Recovery")
	ax[0].plot(df1[:, 0], df1[:, 12]*100, label="O-Xylene Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df2[:, 0], df2[:, 9]*100, label="Toluene Recovery")
	ax[1].plot(df2[:, 0], df2[:, 10]*100, label="P-Xylene Recovery")
	ax[1].plot(df2[:, 0], df2[:, 11]*100, label="M-Xylene Recovery")
	ax[1].plot(df2[:, 0], df2[:, 12]*100, label="O-Xylene Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.7), ncol=2)
	plt.subplots_adjust(hspace=0.3)
	plt.show()

def dis5():
	df1 = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="XyDis", usecols='AC:AO', skiprows=1).to_numpy()
	df2 = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="XyDis", usecols='AQ:BC', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df1[:, 0], df1[:, 9]*100, label="Toluene Recovery")
	ax[0].plot(df1[:, 0], df1[:, 10]*100, label="P-Xylene Recovery")
	ax[0].plot(df1[:, 0], df1[:, 11]*100, label="M-Xylene Recovery")
	ax[0].plot(df1[:, 0], df1[:, 12]*100, label="O-Xylene Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df2[:, 0], df2[:, 9]*100, label="Toluene Recovery")
	ax[1].plot(df2[:, 0], df2[:, 10]*100, label="P-Xylene Recovery")
	ax[1].plot(df2[:, 0], df2[:, 11]*100, label="M-Xylene Recovery")
	ax[1].plot(df2[:, 0], df2[:, 12]*100, label="O-Xylene Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.7), ncol=2)
	plt.subplots_adjust(hspace=0.3)
	plt.show()

def dis6():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="XyDis", usecols='BE:BO', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df[:, 0], df[:, 3]*100, label="O-Xylene Purity")
	ax[0].plot(df[:, 0], df[:, 4]*100, label="O-Xylene Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df[:, 6], df[:, 9]*100, label="O-Xylene Purity")
	ax[1].plot(df[:, 6], df[:, 10]*100, label="O-Xylene Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.9), ncol=2)
	plt.subplots_adjust(hspace=0.5)
	plt.show()

def dis7():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="BenDis", usecols='A:O', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df[:, 0], df[:, 5]*100, label="Benzene Recovery")
	ax[0].plot(df[:, 0], df[:, 6]*100, label="Toluene Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df[:, 8], df[:, 13]*100, label="Benzene Recovery")
	ax[1].plot(df[:, 8], df[:, 14]*100, label="Toluene Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.9), ncol=2)
	plt.subplots_adjust(hspace=0.5)
	plt.show()

def dis8():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="BenDis", usecols='Q:AE', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df[:, 0], df[:, 5]*100, label="Benzene Recovery")
	ax[0].plot(df[:, 0], df[:, 6]*100, label="Methanol Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df[:, 8], df[:, 13]*100, label="Benzene Recovery")
	ax[1].plot(df[:, 8], df[:, 14]*100, label="Methanol Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.9), ncol=2)
	plt.subplots_adjust(hspace=0.5)
	plt.show()

def dis9():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="BenDis", usecols='AG:AW', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df[:, 0], df[:, 5]*100, label="Benzene Purity")
	ax[0].plot(df[:, 0], df[:, 6]*100, label="Toluene Recovery")
	ax[0].plot(df[:, 0], df[:, 7]*100, label="Benzene Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df[:, 9], df[:, 14]*100, label="Benzene Purity")
	ax[1].plot(df[:, 9], df[:, 15]*100, label="Toluene Recovery")
	ax[1].plot(df[:, 9], df[:, 16]*100, label="Benzene Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.7), ncol=2)
	plt.subplots_adjust(hspace=0.3)
	plt.show()

def dis10():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="BenDis", usecols='AY:BI', skiprows=1).to_numpy()
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(df[:, 0], df[:, 3]*100, label="Benzene Purity")
	ax[0].plot(df[:, 0], df[:, 4]*100, label="Benzene Recovery")
	ax[0].set_xlabel("Feed Stage")
	ax[0].set_ylabel("Recovery (%)")
	ax[1].plot(df[:, 6], df[:, 9]*100, label="Benzene Purity")
	ax[1].plot(df[:, 6], df[:, 10]*100, label="Benzene Recovery")
	ax[1].set_xlabel("Condenser Pressure(Bar)")
	ax[1].set_ylabel("Recovery (%)")
	ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, 2.9), ncol=2)
	plt.subplots_adjust(hspace=0.5)
	plt.show()

def crys():
	df = pd.read_excel("Data/Separation Unit Sensitivity.xlsx", sheet_name="Crystal", usecols='B:E', skiprows=1).to_numpy()
	plt.plot(df[:, 0], df[:, 3])
	plt.ylabel("Recovery (%)")
	plt.xlabel("Temperatrue (K)")
	plt.subplots_adjust(left = 0.15)
	plt.show()
#-------------- Execute -------------------
crys()