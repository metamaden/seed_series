#!/usr/bin/env python3
"""
Author: Sean Maden
 
Notes:

* Image from: https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/SMPTE_Color_Bars_16x9.svg/1024px-SMPTE_Color_Bars_16x9.svg.png

"""
from PIL import Image
import numpy as np
import random
import time
time.time() # 1642124557.5068347
seednum = 0 
random.seed(seednum)
newimg_fname = "".join(["seed",str(seednum),".jpg"])
rnum_low = -10
rnum_hi = 10
img1 = Image.open('tv.png')
pixels = np.array(img1)
pixels[np.all(pixels == (255, 0, 0), axis=-1)] = (0,0,0)
newimg=pixels
for ii,seqi in enumerate(newimg):
    for jj,seqj in enumerate(seqi):
        for kk,seqk in enumerate(seqj):
            rnum = random.randint(rnum_low, rnum_hi)
            oval = newimg[ii][jj][kk]
            newval = oval+rnum
            #print("original:" + str(oval))
            #print("new:" + str(newval))
            newimg[ii][jj][kk]=newval
img2 = Image.fromarray(newimg)
img2.show()
img2.save(newimg_fname)