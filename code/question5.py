# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:40:39 2018

@author: IIST
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from PIL import Image
from scipy.misc import imsave
from scipy import fftpack as fftp
import imageio
import skimage.util as skp

lpf=np.matrix([[-1,-1,-1],[-1,8,-1,],[-1,-1,-1]])
lpf = np.float_(lpf)
lpf=lpf/9
hpf=np.matrix([[1,1,1],[1,1,1],[1,1,1]])
hpf = np.float_(hpf)
hpf=hpf/9

s = (7,7)
hpf2=np.ones(s)
hpf2 = np.float_(hpf2)
hpf2=hpf2/49

img = Image.open('gaussian_noise_lenabw.png').convert('L')
img.load()

#r,g,b=img.split()

R=np.asarray( img, dtype="uint8" )
#=np.asarray( g, dtype="float" )
#B=np.asarray( b, dtype="float" )

#data1 = np.asarray( R, dtype="uint8" )
#data2 = np.asarray( G, dtype="uint8" )
#data3 = np.asarray( B, dtype="uint8" )

#noise=skp.random_noise(data,mode='gaussian')
#imsave('gaussian_noise_lenabw.png',noise)

image1=signal.convolve2d(R,hpf2,mode='same') 
#image2=signal.convolve2d(G,hpf2)
#image3=signal.convolve2d(B,hpf2)


img1 = Image.fromarray(image1).convert('L')
plt.imsave('gaussian_noise_filtered_lena_lpf2.png',img1,cmap='gray')
#img2 = Image.fromarray(image2).convert('L')
#img3 = Image.fromarray(image3).convert('L')
#bgr=Image.merge("RGB",(img1,img2,img3))

