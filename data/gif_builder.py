# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 01:33:10 2020

@author: Bosec
"""


import glob
import os
from PIL import Image

fp_in = "./imgs_"
fp_out = "gifs_"
dics = {}
for i in os.listdir('./imgs_/'):
    name = i.split("_")
    name = name[1]
    dics[name] = dics.get(name, []) + [i]

for name in dics:
    img, *imgs = [Image.open(os.path.join(fp_in,f)) for f in sorted(dics[name])]
    img.save(fp=os.path.join(fp_out,name+".gif"), format='GIF', append_images=imgs, save_all=True, duration=500, loop=0)