# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 18:43:44 2018

@author: IIST
"""
import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image
def distance(i, j):
    return np.absolute(i-j)

def bilateral_filter(i,j,d,I,sigma_d,sigma_r):
    arr=[]
    sum_num=0
    sum_den=0
    for k in range(i-math.floor(d/2),i+math.ceil(d/2)):
        for l in range(j-math.floor(d/2),j+math.ceil(d/2)):
            term1=(((i-k)**2)+(j-l)**2)/(sigma_d**2*2)
            term2=(distance(I[i,j],I[k,l]))/(sigma_r**2*2)
            term=term1+term2
            w=math.exp(-term)
            arr.append(w)
            sum_num=sum_num+(I[k,l]*w)
            sum_den=sum_den+w      
    return sum_num/sum_den
    
def main():
    img = Image.open('gaussian_noise_lenabw.png').convert('L')      
    img.load()
    I = np.asarray( img, dtype="float" )
    data=I
    radius=7
    #print(I)
    I=np.lib.pad(I, 1, 'mean')
    I_new=np.copy(data)
    for i in range(1,data.shape[0]):
        for j in range(1,data.shape[1]):
            I_new[i-1,j-1]=bilateral_filter(i-1,j-1,radius,I,7,6.5)
            #print(I_new[i-1,j-1])
    plt.imsave('gn_lo2_bilateral_filtering_lena_new.png',I_new,cmap='gray')
    #isnr_calc(img,Image.fromarray(I_new))
    
   
    
main()