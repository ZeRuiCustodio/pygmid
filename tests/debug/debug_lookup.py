#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pygmid import Lookup as lut
from time import time

# setup mpl
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams.update({"axes.grid" : True})

#%%
import os
filepath_dir = os.getcwd()
print(f"filepath_dir = {filepath_dir}")
filepath_dir = 'C:\\Users\\jruib\\OneDrive\\Documents\\GitHub\\pygmid\\tests\\files\\'
filepath_dir_fig = filepath_dir + 'plots_LUTs_python\\'

# filepath_dir = 'C:\\Users\\jbarbosa\\Documents\\Systematic_Analog_Design\\LUT_90nm\\'
# filepath_dir_fig = filepath_dir + 'plots_LUTs_python\\Book_Chap1'

# str_vt = input("Please insert VT flavor (svt, lvt or hvt): ")
# print(f"Chosen VT flavor {str_vt}")
# # Printing type of input value
# print(f"type of VT flavor {type(str_vt)}")
# filename_LUT = '90nch_svt_mac_tt_lib_27C_v2.mat'
# filename_LUT = '90nch_'+str_vt+'_mac_tt_lib_27C_v2_Cervin.mat'

filename_LUT = '180nch.mat'
print(f"filename_LUT = {filename_LUT}")
file_LUT = filepath_dir+filename_LUT
print(f"file_LUT = {file_LUT}")

# save_Figs = False
save_Figs = True
dpi = 600

if not os.path.exists(filepath_dir_fig):
    # if the folder directory is not present then create it.
    print("Creating figures/plots directory.")
    os.makedirs(filepath_dir_fig)


#%%
NCH = lut(file_LUT)  # load MATLAB data into pygmid lookup object
# NCH = lut('tsmcN65_n25.pkl')  # load MATLAB data into pygmid lookup object

VDSs = NCH['VDS']       # lookup object has pseudo-array access to data
VGSs = np.arange(0.4, 0.6, 0.05)

# %%
# Plot ID versus VDS
ID = NCH.look_up('ID', vds=VDSs, vgs=VGSs)
plt.figure()
plt.plot(VDSs, 1e6*ID.T)
plt.ylabel(r"$I_D$ [$\mu$A]")
plt.xlabel(r"$V_{DS}$ [V]")
plt.title(r'$I_D$ vs. $V_{DS}$ for varying $V_{GS}$')
plt.legend(VGSs)
plt.show()
# TODO: use something like https://github.com/matplotlib/pytest-mpl to compare the plots

# %%
# plot Vt against L
Ls = NCH['L']
vt = NCH.look_up('VT', vgs=0.6, L=Ls)
plt.figure()
plt.plot(Ls, vt.T)
plt.ylabel(r"$V_T$ [V]")
plt.xlabel(r"$L$ [$\mu$m]")
plt.title(r'$V_T$ vs. $L$')
plt.show()

# %% 
# Plot ft against gm_id for different L
step = 0.1
gm_ids = np.arange(5, 20+step, step)
Ls = np.arange(min(NCH['L']),0.3,0.05)
s = time()
ft = NCH.look_up('GM_CGG', GM_ID=gm_ids, L =np.arange(min(Ls),0.3,0.05))/2/np.pi
e = time()
print(f"Time taken: {(e-s)*1000} [ms]")
plt.figure()
plt.plot(gm_ids, 1e-9*ft.T)
plt.ylabel(r"$f_T$ [GHz]")
plt.xlabel(r"$g_m/I_D$")
plt.title(r'$f_T$ vs. $g_m/I_D$ for varying $L$')
plt.legend(np.around(Ls, decimals=2))
plt.show()

# %%
# Plot id/w against gm_id for different L
gm_ids = np.arange(5, 20+0.1, 0.1)
step = 0.05
Ls = [0.18, 0.23, 0.28, 0.3]
id_w = NCH.look_up('ID_W', GM_ID=gm_ids, L=Ls)
plt.figure()
plt.semilogy(gm_ids, id_w.T)
plt.ylabel(r"$I_D/W$")
plt.xlabel(r"$g_m/I_D$")
plt.title(r'$I_D/W$ vs. $g_m/I_D$ for varying $L$')
plt.legend(np.around(Ls, decimals=2))
plt.show()

# %%
# Plot id/w against gm_id for different VDS (at minimum L)
gm_ids = np.arange(5, 20+0.1, 0.1)
id_w = NCH.look_up('ID_W', GM_ID=gm_ids, VDS=[0.8, 1.0, 1.2])
plt.figure()
plt.semilogy(gm_ids, id_w.T)
plt.ylabel(r"$I_D/W$")
plt.xlabel(r"$g_m/I_D$")
plt.title(r'$I_D/W$ vs. $g_m/I_D$ for varying $V_{DS}$')
plt.legend([0.8, 1.0, 1.2])
plt.show()

# %%
# Plot gm/gds against gm_id (at minimum L and default VDS)
gm_ids = np.arange(5, 20+0.1, 0.1)
gm_gds = NCH.look_up('GM_GDS', GM_ID=gm_ids)
plt.figure()
plt.semilogy(gm_ids, gm_gds.T)
plt.ylabel(r"$g_m/g_{DS}$")
plt.xlabel(r"$g_m/I_D$")
plt.title(r'$g_m/g_{DS}$ vs. $g_m/I_D$')
plt.show()

# %%
# test for utility function
gm_ID = NCH.look_up('GM_ID', VDS=np.arange(0.025, 1.2+0.025, 0.025), VSB=0.0, L=0.18)
print(gm_ID)

# %%
gm_id1 = 15
id_w1 = NCH.look_up('ID_W', GM_ID=gm_id1, L=0.18)
print(f"id_w1 = {id_w1*1e6} uA/um")
id1 = 20e-6
W1 = id1 / id_w1
print(f"W1 = {W1} um")
id2 = NCH.look_up('ID', ID_W=1e-6, VDS = 0.5, L=0.18)
print(id2)
gm1 = gm_id1 * id1
print(f"gm1 = {gm1*1e6} uS")
gm_w1 = gm1 / W1
print(f"gm_w1 = {gm_w1*1e6} uS/um")
gm_id2 = NCH.look_up('GM_ID', GM_W=gm_w1, L=0.18)
print(f"gm_id2 = {gm_id2} S/A")

# %%
gm_id = NCH.look_up('GM_ID', ID_W=1.159e-05, L=0.18)
print(gm_id)