# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:43:20 2018

@author: IIST
"""

import numpy as np
from PIL import Image
from scipy import fftpack as fftp
from matplotlib import pyplot as plt
from degradation import return_degraded_image
g,H=return_degraded_image()
G=fftp.fft2(g)
img = Image.open('2_degraded_image.png').convert('L')
img.load()
data = np.asarray( img, dtype="float64" )
img0 = Image.open('gauss__noise.png').convert('L')
img0.load()

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 5),
                       sharex=True, sharey=True)
F=np.zeros((256,256),dtype="complex")
K=0
for u in range(1,257):
    for v in range(1,257):
        den=1/H[u-1,v-1]
        temp=(abs(H[u-1,v-1])**2)/((abs(H[u-1,v-1])**2)+K)
        filt=den*temp
        F[u-1,v-1]=filt*G[u-1,v-1]
image2=np.fft.ifft2(F)
plt.gray()

ax[0].imshow(img0)
ax[0].axis('off')
ax[0].set_title('Original Image')

ax[1].imshow(img)
ax[1].axis('off')
ax[1].set_title('Degraded Image')

ax[2].imshow(image2.real)
ax[2].axis('off')
ax[2].set_title('After Wiener Filtering')

plt.figure()
plt.imshow(image2.real,cmap='gray')
plt.imsave('gaussian_noise_wiener_filtering_cameraman_new2.png',image2.real,cmap='gray')


#plt.imshow(deconvolved_img.real, cmap='gray')
#plt.imsave('restored_image.png',deconvolved_img.real, cmap='gray')


