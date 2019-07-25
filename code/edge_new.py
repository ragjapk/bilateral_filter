# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:50:38 2018

@author: IIST
"""
from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
def get_image():
    img = Image.open('gaussian_noise_lenabw.png').convert('L')      
    img.load()
    I = np.asarray( img, dtype="uint8" )
    data=I
    print("Image is {}",data)
    I=np.lib.pad(I, 2, 'mean')
    I_new=np.zeros((data.shape[0],data.shape[1]))
    mean_arr=[]
    var_arr=[]
    for x in range(1,data.shape[0]):
        for y in range(1,data.shape[1]):
            one = np.matrix([[I[x-2,y-2], I[x-1,y-2],I[x,y-2]],[I[x-2,y-1], I[x-1,y-1],I[x,y-1]],[I[x-2,y], I[x-1,y],I[x,y]]])
            mean_arr.append(np.mean(one))
            var_arr.append(np.var(one))
            two = np.matrix([[I[x-1,y-2], I[x,y-2],I[x+1,y-2]],[I[x-1,y-1], I[x,y-1],I[x+1,y-1]],[I[x-1,y], I[x,y],I[x+1,y]]])
            mean_arr.append(np.mean(two))
            var_arr.append(np.var(two))
            thr = np.matrix([[I[x,y-2], I[x+1,y-2],I[x+2,y-2]],[I[x,y-1], I[x+1,y-1],I[x+2,y-1]],[I[x,y], I[x+1,y],I[x+2,y]]])
            mean_arr.append(np.mean(thr))
            var_arr.append(np.var(thr))
            four =np.matrix([[I[x-2,y-1], I[x-1,y-1],I[x,y-1]],[I[x-2,y], I[x-1,y],I[x,y]],[I[x-2,y+1], I[x-1,y+1],I[x,y+1]]])
            mean_arr.append(np.mean(four))
            var_arr.append(np.var(four))
            fiv = np.matrix([[I[x-1,y-1], I[x,y-1],I[x+1,y-1]],[I[x-1,y], I[x,y],I[x+1,y]],[I[x-1,y+1], I[x,y+1],I[x+1,y+1]]])
            mean_arr.append(np.mean(fiv))
            var_arr.append(np.var(fiv))
            six = np.matrix([[I[x,y-1], I[x+1,y-1],I[x+2,y-1]],[I[x,y], I[x+1,y],I[x+2,y]],[I[x,y+1], I[x+1,y+1],I[x+2,y+1]]])
            mean_arr.append(np.mean(six))
            var_arr.append(np.var(six))
            sev = np.matrix([[I[x-2,y], I[x-1,y],I[x,y]],[I[x-2,y+1], I[x-1,y+1],I[x,y+1]],[I[x-2,y+2], I[x-1,y+2],I[x,y+2]]])
            mean_arr.append(np.mean(sev))
            var_arr.append(np.var(sev))
            eig = np.matrix([[I[x-1,y], I[x,y],I[x+1,y]],[I[x-1,y+1], I[x,y+1],I[x+1,y+1]],[I[x-1,y+2], I[x,y+2],I[x+1,y+2]]])
            mean_arr.append(np.mean(eig))
            var_arr.append(np.var(eig))
            nin = np.matrix([[I[x,y], I[x+1,y],I[x+2,y]],[I[x,y+1], I[x+1,y+1],I[x+2,y+1]],[I[x,y+2], I[x+1,y+2],I[x+2,y+2]]])
            mean_arr.append(np.mean(nin))
            var_arr.append(np.var(nin))
            meanarr=np.array(mean_arr)
            vararr=np.array(var_arr)
            min_index=np.argmin(vararr)
            I_new[x-1,y-1]=meanarr[min_index]
            #print(x,y)
            mean_arr=[]
            var_arr=[]
    plt.imsave('after_edge_smoothening.png',I_new,cmap='gray')
            
            
get_image();
                    
            
            
            
            
            
            
            
            
            
            
            