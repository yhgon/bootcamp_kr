# Compression script: ~15x compression 
import h5py
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os 
filename = "2017.h5"
hf = h5py.File(filename, 'r')
n1 = hf.get('fields')

# Test set
total_days_to_save_test = 7
recordings_per_day_test = 4
start_index_test = 183

# Train set 
total_days_to_save_train = 182
recordings_per_day_train = 4
start_index_train = 0
channels_to_store = 21

# Data path for test and train
data_path_train=os.getcwd()+'/pre_data/train'
data_path_test=os.getcwd()+'/pre_data/test'

############################################### Processing for Training set 
# Create data-dir
c_list_global=[]
a_list_global=[]
if not os.path.exists(data_path_train):
    os.makedirs(data_path_train)
# loop to create images.
for i in range(total_days_to_save_train*recordings_per_day_train):
    # Create directory to store images
    dir_path = data_path_train + '/'+ str(i)
    c_list_local=[]
    a_list_local=[]
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for j in range(channels_to_store):
        H = n1[i+start_index_train][j]
        # Find c,a 
        c = H.min()
        img_range = H.max()-H.min() 
        a =  img_range / 255
        # Generate img to save as 16 bit
        H_1 = ((H-c)/a).astype(int)
        save_path = dir_path+'/'+str(j)+".png"
        cv2.imwrite(save_path,H_1)
        c_list_local.append(c)
        a_list_local.append(a)
        print('.',end='')
    c_list_global.append(c_list_local)
    a_list_global.append(a_list_local)
np.save(data_path_train+'/c_array.npy', np.array(c_list_global))
np.save(data_path_train+'/a_array.npy', np.array(a_list_global))


############################################### Processing for Test set 
# Create data-dir
c_list_global=[]
a_list_global=[]
if not os.path.exists(data_path_test):
    os.makedirs(data_path_test)
# loop to create images.
for i in range(total_days_to_save_test*recordings_per_day_test):
    # Create directory to store images
    dir_path = data_path_test + '/'+ str(i)
    c_list_local=[]
    a_list_local=[]
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for j in range(channels_to_store):
        H = n1[i+start_index_test][j]
        # Find c,a 
        c = H.min()
        img_range = H.max()-H.min() 
        a =  img_range / 255
        # Generate img to save as 16 bit
        H_1 = ((H-c)/a).astype(int)
        save_path = dir_path+'/'+str(j)+".png"
        cv2.imwrite(save_path,H_1)
        c_list_local.append(c)
        a_list_local.append(a)
        print('.',end='')
    c_list_global.append(c_list_local)
    a_list_global.append(a_list_local)
np.save(data_path_test+'/c_array.npy', np.array(c_list_global))
np.save(data_path_test+'/a_array.npy', np.array(a_list_global))