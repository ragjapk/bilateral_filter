# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:49:39 2018

@author: IIST
"""
import numpy as np
import math
from PIL import Image
from scipy import fftpack as fftp
import cmath
from matplotlib import pyplot as plt
def return_degraded_image():
    img = Image.open('gauss__noise.png').convert('L')
    img.load()
    data = np.asarray( img, dtype="float64" )
    
    image_fft=fftp.fft2(data)
    a=1
    b=1
    T=10 
    H=np.zeros((256,256),dtype="complex")
    
    for u in range(1,257):
        for v in range(1,257):
            den=math.pi*(u*a+v*b)
            #print(den)
            temp=math.sin(den)
            complexno=1j
            exponent=cmath.exp((-complexno)*den)
            num=T*temp*exponent
            #num=complex(numerator)
            H[u-1,v-1]=num/den
    final_image2=image_fft*H
    image2=np.fft.ifft2(final_image2)   
    plt.imsave('2_degraded_image.png',image2.real, cmap='gray')
    return(image2,H)
return_degraded_image()