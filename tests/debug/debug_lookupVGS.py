#%%
import matplotlib.pyplot as plt
import numpy as np
from pygmid import Lookup as lk

# %%
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

# %%
NCH = lk(file_LUT)  # load MATLAB data into pygmid lookup object
# NCH = lk('180nch.mat')  # load MATLAB data into pygmid lookup object

#%% Test 1
VGS = NCH.look_upVGS(GM_ID = 10, VDS = 0.6, VSB = 0.1, L = 0.18)
print(f'VGS is: {VGS}')

#%% Test 2
VGS = NCH.look_upVGS(GM_ID = np.arange(10, 16, 1), VDS = 0.6, VSB = 0.1, L = 0.18)
print(f'VGS is: {VGS}')

#%% Test 3
VGS = NCH.look_upVGS(ID_W = 1e-4, VDS = 0.6, VSB = 0.1, L = 0.18)
print(f'VGS is: {VGS}')

#%% Test 4
VGS = NCH.look_upVGS(ID_W = 1e-4, VDS = 0.6, VSB = 0.1, L = np.arange(0.18, 0.5, 0.1))
print(f'VGS is: {VGS}')

#%% Test 5
VGS = NCH.look_upVGS(GM_ID = 10, VDB = 0.6, VGB = 1, L = 0.18)
print(f'VGS is: {VGS}')

#%% Test 6
VGS = NCH.look_upVGS(ID_W = 1e-4, VDB = 0.6, VGB = 1, L = 0.18)
print(f'VGS is: {VGS}')

# %%
