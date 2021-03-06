# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 22:06:28 2018

@author: IIST
"""


from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import skimage.util as skp
import math
from scipy import signal
from scipy.misc import imsave
def get_image():
    img = Image.open('lenabw.jpg').convert('L')      
    img.load()
    data = np.asarray( img, dtype="uint8" )
    noise_creation_gaussian(data)
    
def noise_creation_gaussian(data):
    noise=skp.random_noise(data,mode='gaussian',var=0.08 )
    imsave('gaussian_noise_lena.png',noise)

get_image()