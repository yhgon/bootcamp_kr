#BSD 3-Clause License
#
#Copyright (c) 2022, FourCastNet authors
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#3. Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#The code was authored by the following people:
#
#Jaideep Pathak - NVIDIA Corporation
#Shashank Subramanian - NERSC, Lawrence Berkeley National Laboratory
#Peter Harrington - NERSC, Lawrence Berkeley National Laboratory
#Sanjeev Raja - NERSC, Lawrence Berkeley National Laboratory 
#Ashesh Chattopadhyay - Rice University 
#Morteza Mardani - NVIDIA Corporation 
#Thorsten Kurth - NVIDIA Corporation 
#David Hall - NVIDIA Corporation 
#Zongyi Li - California Institute of Technology, NVIDIA Corporation 
#Kamyar Azizzadenesheli - Purdue University 
#Pedram Hassanzadeh - Rice University 
#Karthik Kashinath - NVIDIA Corporation 
#Animashree Anandkumar - California Institute of Technology, NVIDIA Corporation


# Instructions: 
# Set Nimgtot correctly

import h5py
from mpi4py import MPI
import numpy as np
import time
from netCDF4 import Dataset as DS
import os

def writetofile(src, dest, channel_idx, varslist, src_idx=0, frmt='nc'):
    if os.path.isfile(src):

        for variable_name in varslist:

            if frmt == 'nc':
                fsrc = DS(src, 'r', format="NETCDF4").variables[variable_name]
            elif frmt == 'h5':
                fsrc = h5py.File(src, 'r')[varslist[0]]
            
            fdest = h5py.File(dest, 'a') 

            if len(fsrc.shape) == 4:
                ims = fsrc[0:fsrc.shape[0],src_idx]
            else:
                ims = fsrc[0:fsrc.shape[0]]
                
            print("variable: ", variable_name ,end="\t")
            print("ims shape", ims.shape, end="\t")
            print("fsrc shape", fsrc.shape)
            fdest['fields'][0:fsrc.shape[0], channel_idx, :, :] = ims
            
############ Verify if these are set correctly ############# 
dest = '/workspace/python/source_code/FCN/data/ERA5/2023.h5'

src_sfc = '/workspace/python/source_code/FCN/data/ERA5/mar_2023_27_sfc.nc'
src_pl  = '/workspace/python/source_code/FCN/data/ERA5/mar_2023_27_pl.nc'
#############################################################



#u10 v10 t2m
writetofile(src_sfc, dest, 0, ['u10'])
writetofile(src_sfc, dest, 1, ['v10'])
writetofile(src_sfc, dest, 2, ['t2m'])

#sp mslp
writetofile(src_sfc, dest, 3, ['sp'])
writetofile(src_sfc, dest, 4, ['msl'])

#t850
writetofile(src_pl, dest, 5, ['t'], 2)

#uvz1000
writetofile(src_pl, dest, 6, ['u'], 3)
writetofile(src_pl, dest, 7, ['v'], 3)
writetofile(src_pl, dest, 8, ['z'], 3)

#uvz850
writetofile(src_pl, dest, 9, ['u'], 2)
writetofile(src_pl, dest, 10, ['v'], 2)
writetofile(src_pl, dest, 11, ['z'], 2)

#uvz 500
writetofile(src_pl, dest, 12, ['u'], 1)
writetofile(src_pl, dest, 13, ['v'], 1)
writetofile(src_pl, dest, 14, ['z'], 1)

#t500
writetofile(src_pl, dest, 15, ['t'], 1)

#z50
writetofile(src_pl, dest, 16, ['z'], 0)

#r500 
writetofile(src_pl, dest, 17, ['r'], 1)

#r850
writetofile(src_pl, dest, 18, ['r'], 2)

#tcwv
writetofile(src_sfc, dest, 19, ['tcwv'])



