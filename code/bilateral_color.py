# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 15:17:26 2018

@author: IIST
"""
from PIL import Image
import numpy as np

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

img = Image.open('balloons_noisy.png')  
img.load()

b,g,r=img.split()

R=np.asarray( r, dtype="float" )
G=np.asarray( g, dtype="float" )
B=np.asarray( b, dtype="float" )

Rnew=np.zeros((R.shape[0],R.shape[1]))
Gnew=np.zeros((G.shape[0],G.shape[1]))
Bnew=np.zeros((B.shape[0],B.shape[1]))

width = img.size[0] #define W and H
height = img.size[1]

for y in range(0, height): #each pixel has coordinates
    row = ""
    for x in range(0, width):

        RGB = img.getpixel((x,y))
        R[y,x],G[y,x],B[y,x] = RGB  #now you can use the RGB value
        
radius=7
I=np.lib.pad(R, 3, 'mean')
I_new=np.copy(R)
for i in range(1,R.shape[0]):
    for j in range(1,R.shape[1]):
        I_new[i-1,j-1]=bilateral_filter(i-1,j-1,radius,I,7,7)
Rnew=I_new

I=np.lib.pad(G, 3, 'mean')
I_new=np.copy(G)
for i in range(1,G.shape[0]):
    for j in range(1,G.shape[1]):
        I_new[i-1,j-1]=bilateral_filter(i-1,j-1,radius,I,7,7)
Gnew=I_new

I=np.lib.pad(B, 3, 'mean')
I_new=np.copy(B)
for i in range(1,B.shape[0]):
    for j in range(1,B.shape[1]):
        I_new[i-1,j-1]=bilateral_filter(i-1,j-1,radius,I,7,7)
Bnew=I_new

img1 = Image.fromarray(Rnew).convert('L')
img2 = Image.fromarray(Gnew).convert('L')
img3 = Image.fromarray(Bnew).convert('L')
img1.save('myimg1.png')
img2.save('myimg2.png')
img3.save('myimg3.png')
rgbArray = np.zeros((height,width,3), 'uint8')
rgbArray[:,:,0] = Rnew*256
rgbArray[:,:,1] = Gnew*256
rgbArray[:,:,2] = Bnew*256
img = Image.fromarray(rgbArray)
bgr=Image.merge("RGB",(img1,img2,img3))
bgr.save('myimgballoon.png')
                   
            