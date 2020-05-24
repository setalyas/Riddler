# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:44:12 2020

@author: setat
"""

#import pickle
from matplotlib import colors
from scipy.spatial import cKDTree as KDTree
import numpy as np
from PIL import Image

# =============================================================================
# High fidelity colour check on matching flags
# =============================================================================

flags = {'FR': "", 'BR': "", 'WA': ""}

REDUCED_COLOR_SPACE = False
use_colors = colors.cnames
named_colors = {k: tuple(map(int, (v[1:3], v[3:5], v[5:7]), 3*(16,)))
                for k, v in use_colors.items()}
ncol = len(named_colors)
no_match = named_colors['purple']

# make an array containing the RGB values 
color_tuples = list(named_colors.values())
color_tuples.append(no_match)
color_tuples = np.array(color_tuples)

color_names = list(named_colors)
color_names.append('no match')

# build tree
tree = KDTree(color_tuples[:-1])
# tolerance for color match `inf` => use best match no matter how bad it may be
tolerance = np.inf
    
for cntry in flags.keys():
    fp = 'Flags\\' + cntry + '-flag.gif'
    img = Image.open(fp)
    width, height = img.size
    im = img.getdata().convert('RGB')
    # find closest color in tree for each pixel in picture
    dist, idx = tree.query(im, distance_upper_bound=tolerance)
    # count and reattach names
    counts = dict(zip(color_names, np.bincount(idx.ravel(), None, ncol+1)))
    flags[cntry] = {'colours': counts, 'W': width, 'H': height}

# =============================================================================
# Put comparison flags in a similar layout
# =============================================================================

to_compare = dict()
for i in range(1,4):
    fp = 'Scrambled\\flag_' + str(i) + '.png'
    img = Image.open(fp)
    width, height = img.size
    im = img.getdata().convert('RGB')
    dist, idx = tree.query(im, distance_upper_bound=tolerance)
    counts = dict(zip(color_names, np.bincount(idx.ravel(), None, ncol+1)))
    to_compare[i] = {'colours': counts, 'W': width, 'H': height}

# =============================================================================
# See the distance between scrambled flag and real flag
# =============================================================================

flag_data = [flags, to_compare]

# normalise pixel counts for comparisons
for dt in flag_data:
    for flag in dt.keys():
        width = dt[flag]['W']
        height = dt[flag]['H']
        aspect = round(width / height,1)
        dt[flag]['aspect'] = aspect
        pixelcount = width * height
        for c, n in dt[flag]['colours'].items():    
            dt[flag]['colours'][c] = round(n / pixelcount, 2)

# Check close matches
res = {}
for i in range(1,4):
    arr = np.array(list(to_compare[i]['colours'].values()))
    matches = {key: np.array(list(value['colours'].values()))
                for key, value in flags.items()
                if value['aspect'] == to_compare[i]['aspect']}
    diffs = {key: np.linalg.norm(value - arr)
                for key, value in matches.items()}
    minnorm = min(diffs.values())
    res[i] = [k for k, v in diffs.items() if v==minnorm]
    print(i, minnorm)
# All pretty close!
    
""" Results:
1 0.0
2 0.0
3 0.017320508075688783
"""