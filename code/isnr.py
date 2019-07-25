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
noised = Image.open("gaussian_noise_lena.png").convert('L')
restored_bl = Image.open("gn_high_bilateral_filtering_cam_new2.png").convert('L')
restored_lpf=Image.open("gaussian_noise_filtered_lena_lpf.png").convert('L')
#original = cv2.imread("gaussian_noise_lenabw.png")

def findSum(arr): 
  
    # inner map function applies inbuilt function   
    # sum on each row of matrix arr and returns  
    # list of sum of elements of each row 
    return sum(map(sum,arr))   

def psnr(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 10 * math.log10(PIXEL_MAX / math.sqrt(mse))

def normalize(img):
    img = img/np.max(img)
    return img

def psnr2(img1,img2):
    diff=np.subtract(img1,img2)
    temp=np.power(diff,2)
    final=findSum(temp)
    
    mse=final/(img1.shape[0]*img1.shape[1])
    print(math.sqrt(mse))
    PIXEL_MAX = 255.0
    return 10 * math.log10(PIXEL_MAX**2 / math.sqrt(mse)) 

def norm(img1,img2):
    mse = np.mean( (img1 - img2) ** 2 )
    return mse

original=np.asarray(original, dtype="float" )
noised=np.asarray(noised, dtype="float" )
restored_bl=np.asarray(restored_bl, dtype="float" )
restored_lpf=np.asarray(restored_lpf, dtype="float" )

noisy_norm=psnr2(original,noised)
restored_norm=psnr2(original,restored_bl)
print(noisy_norm,restored_norm)
isnr1 = restored_norm-noisy_norm
print(isnr1)

noisy_norm=psnr2(original,noised)
restored_norm=psnr2(original,restored_lpf)
isnr2 = restored_norm-noisy_norm
print(restored_norm)
print(isnr2)
'''def isnr_calc(noisy,original):
  noisy_norm = sum(abs(original(:) - noisy(:)).^2)
  restored_norm = sum(abs(original(:) - restored(:)).^2)
  isnr = 10*log10( noisy_norm / restored_norm) '''