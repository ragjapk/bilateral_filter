# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 18:59:46 2018

@author: IIST
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:28:10 2018

@author: IIST
"""
from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
def g(x):
    val=(x/25)**2
    return math.exp(-val)

def get_image():
    λ=0.21
    img = Image.open('gauss__noise.png').convert('L')      
    img.load()
    I = np.asarray( img, dtype="uint8" )
    data=I
    print("Image is {}",data)
    N=np.zeros((I.shape[0],I.shape[1]))
    S=np.zeros((I.shape[0],I.shape[1]))
    E=np.zeros((I.shape[0],I.shape[1]))
    W=np.zeros((I.shape[0],I.shape[1]))
    cN=np.zeros((I.shape[0],I.shape[1]))
    cS=np.zeros((I.shape[0],I.shape[1]))
    cE=np.zeros((I.shape[0],I.shape[1]))
    cW=np.zeros((I.shape[0],I.shape[1]))
    I_new=np.zeros((I.shape[0],I.shape[1]))
    for k in range(20):
        for x in range(I.shape[0]-1):
            for y in range(I.shape[1]-1):
                N[x,y] = I[x-1,y] - I[x,y]
                S[x,y] = I[x+1,y] - I[x,y]
                E[x,y] = I[x,y+1] - I[x,y]
                W[x,y] = I[x,y-1] - I[x,y]
                
                cN[x,y] = g(N[x,y])
                cS[x,y] = g(S[x,y])
                cE[x,y] = g(E[x,y])
                cW[x,y] = g(W[x,y])
                
        for i in range(I.shape[0]):
            for j in range(I.shape[1]):            
                sum=cN[i, j]*N[i, j] + cS[i, j]*S[i, j]+ cE[i, j]*E[i, j] + cW[i, j]*W[i, j]
                I_new[i, j] = I[i, j] +λ * sum
        I=np.copy(I_new)
    plt.imsave('original_image.png',I_new,cmap='gray')
            
            
get_image()