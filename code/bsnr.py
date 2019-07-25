# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:06:08 2018

@author: IIST
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:41:26 2018

@author: IIST
"""

import numpy as np
import math
import cv2
from PIL import Image
from numpy import linalg as la

original = Image.open("lenabw.jpg").convert('L')
noised = Image.open("gaussian_noise_lenabw.png").convert('L')
restored_bl = Image.open("gn_lo_bilateral_filtering_lena_new.png").convert('L')
restored_edge=Image.open("after_edge_smoothening.png").convert('L')
restored_lpf=Image.open("gaussian_noise_filtered_lena_lpf2.png").convert('L')
#original = cv2.imread("gaussian_noise_lenabw.png")

def findSum(arr): 
  
    # inner map function applies inbuilt function   
    # sum on each row of matrix arr and returns  
    # list of sum of elements of each row 
    return sum(map(sum,arr))   

def lsnr(img1,img2,img3):
    diff=np.subtract(img1,img2)
    temp=np.power(diff,2)
    final=findSum(temp)

    diff=np.subtract(img1,img3)
    temp=np.power(diff,2)
    final2=findSum(temp)
    
    return 10 * math.log10(final/final2) 

original=np.asarray(original, dtype="float" )
noised=np.asarray(noised, dtype="float" )
restored_bl=np.asarray(restored_bl, dtype="float" )
restored_lpf=np.asarray(restored_lpf, dtype="float" )
restored_edge=np.asarray(restored_edge, dtype="float" )

lsnrrr=lsnr(original,noised,restored_bl)
print(lsnrrr)

lsnrrr=lsnr(original,noised,restored_lpf)
print(lsnrrr)

lsnrrr=lsnr(original,noised,restored_edge)
print(lsnrrr)
