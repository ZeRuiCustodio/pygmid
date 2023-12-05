#%%
import matplotlib.pyplot as plt
import numpy as np
from pygmid import Lookup as lk
from pygmid import EKV_param_extraction, XTRACT

# %%
import os
file_LUT = os.path.dirname(__file__) + '\\..\\files\\180nch.mat'

#%%    
NCH = lk(file_LUT)  # load MATLAB data into pygmid lookup object
# NCH = lk('180nch.mat')  # load MATLAB data into pygmid lookup object

#%% Test 1
(VDS, n, VT, JS, d1n, d1VT, d1logJS, d2n, d2VT, d2logJS) = EKV_param_extraction(NCH, 1, L = 0.18, VDS = 0.6, VSB = 0.0)

print(f"EKV_param_extraction: VDS = {VDS}")
print(f"EKV_param_extraction: n = {n}")
print(f"EKV_param_extraction: VT = {VT}")
print(f"EKV_param_extraction: JS = {JS}")
print(f"EKV_param_extraction: d1n = {d1n}")
print(f"EKV_param_extraction: d1VT = {d1VT}")
print(f"EKV_param_extraction: d1logJS = {d1logJS}")
print(f"EKV_param_extraction: d2n = {d2n}")
print(f"EKV_param_extraction: d2VT = {d2VT}")
print(f"EKV_param_extraction: d2logJS = {d2logJS}")

#%% Test 2
(VDS, n, VT, JS, d1n, d1VT, d1logJS, d2n, d2VT, d2logJS) = XTRACT(NCH, 1, L = 0.4, VDS = 0.6, VSB = 0.0)

print(f"XTRACT: VDS = {VDS}")
print(f"XTRACT: n = {n}")
print(f"XTRACT: VT = {VT}")
print(f"XTRACT: JS = {JS}")
print(f"XTRACT: d1n = {d1n}")
print(f"XTRACT: d1VT = {d1VT}")
print(f"XTRACT: d1logJS = {d1logJS}")
print(f"XTRACT: d2n = {d2n}")
print(f"XTRACT: d2VT = {d2VT}")
print(f"XTRACT: d2logJS = {d2logJS}")

# %%
