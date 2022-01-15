#!/usr/bin/env python3
"""
Author: Sean Maden

Code to generate images for the SMPTE seed series.
 
Notes:

* Image from: https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/SMPTE_Color_Bars_16x9.svg/1024px-SMPTE_Color_Bars_16x9.svg.png

"""
from PIL import Image
import numpy as np
import random
import os
# import time

def new_smpte_image(seednum = 1, rnum_low = -10, rnum_hi = 10, 
    img_base_fpath = os.path.join("img","tv.png"), save_dirname = "img"):
    """ new_smpte_image

    Make a new SMPTE seed series image.

    Arguments:
    * seednum = Seed number for random pixel value offset (int, 1).
    * rnum_low = Lower bounds for random pixel value offset (int, -10).
    * rnum_hi = Upper bounds for random pixel value offset (int, 10).
    * img_base_fpath = File path for base image (valid path).
    
    Returns:
    True, saves new image with file name pattern:
    "img_new_fname = "".join(["seed",str(seednum),".jpg"])" 


    """
    # timestamp = time.time() # 1642124557.5068347
    random.seed(seednum)
    img_new_fname = "".join(["smpte_seed_",str(seednum),".jpg"])
    img_new_fpath = os.path.join(save_dirname, img_new_fname)
    # read base image pixels into np array
    img_base = Image.open(img_base_fpath)
    pixels = np.array(img_base)
    pixels[np.all(pixels == (255, 0, 0), axis=-1)] = (0,0,0)
    pixels_new=pixels
    # assign pixel offsets
    for ii,seqi in enumerate(pixels_new):
        for jj,seqj in enumerate(seqi):
            for kk,seqk in enumerate(seqj):
                rnum = random.randint(rnum_low, rnum_hi)
                oval = pixels_new[ii][jj][kk]
                newval = oval+rnum
                pixels_new[ii][jj][kk]=newval
    # save new image
    img_new = Image.fromarray(pixels_new)
    img_new.save(img_new_fpath)
    return True

if __name__ == "__main__":
    """ make_new_smpte_seed.py
        
        Make a new image in the SMPTE seed series.
    
    """
    import argparse
    parser = argparse.ArgumentParser(description="Arguments for SMPTE seed series")
    parser.add_argument("--seednum", type = int, required = True, default = 0,
        help = "Seed integer number for new image.")
    args = parser.parse_args()
    new_smpte_image(seednum=args.seednum)
