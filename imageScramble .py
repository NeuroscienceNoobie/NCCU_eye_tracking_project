# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 01:20:03 2022

@author: yu
"""
from PIL import Image
import numpy as np
import os

# Directory
ddir = 'C:\\Users\yu\Desktop\img 2 - Copy'
os.chdir(ddir)
print(os.getcwd())

# get name of all png files in directory 
filelist=os.listdir(ddir)
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)
print(filelist)

# re-arrange pixels
for k in range(len(filelist)):
    orig =  Image.open(filelist[k])
    orig_px = orig.getdata()
    orig_px = np.reshape(orig_px, (orig.height * orig.width, 3))
    np.random.shuffle(orig_px)
    orig_px = np.reshape(orig_px, (orig.height, orig.width, 3))
    res = Image.fromarray(orig_px.astype('uint8'))
    res.save(filelist[k][0:8]+'_'+'shuffled'+'.jpg')# rename and save
    #res.show()


# these are redundent 
orig =  Image.open('DSCF7674.png')
orig_px = orig.getdata()

orig_px = np.reshape(orig_px, (orig.height * orig.width, 3))
np.random.shuffle(orig_px)

orig_px = np.reshape(orig_px, (orig.height, orig.width, 3))

res = Image.fromarray(orig_px.astype('uint8'))
res.save('out.jpg')
res.show()
