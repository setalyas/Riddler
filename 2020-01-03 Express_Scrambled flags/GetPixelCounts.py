# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:05:57 2020

@author: setat
"""

import numpy as np
from PIL import Image
from os import listdir
from os.path import isfile, join
import pickle

fldr = 'Flags'
onlyfiles = [f for f in listdir(fldr) if isfile(join(fldr, f))]
flags = {}
for fp in onlyfiles:
    flags[fp[:2]] = ""
    
# =============================================================================
# Attempt 1: get counts from palettised form
# =============================================================================

# Palettised img explainer https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil/52307690#52307690

for cntry in flags.keys():
    fp = fldr + '\\' + cntry + '-flag.gif'
    img = Image.open(fp)
    pxls = np.array(img.getdata()).flatten()  # in palettised form
    counts = np.unique(pxls, return_counts=True)[1]
    flags[cntry] = counts

with open('Outputs\\pixelcounts.pickle', 'wb') as handle:
    pickle.dump(flags, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
"""Upside = quick!
Downside = no idea how useful it is, if palette refs even transfer across imgs
"""

# =============================================================================
# Attempt 2: kdtree to group against known colours
# =============================================================================

# https://stackoverflow.com/questions/50545192/count-different-colour-pixels-python

from matplotlib import colors
from scipy.spatial import cKDTree as KDTree

REDUCED_COLOR_SPACE = True

# borrow a list of named colors from matplotlib
if REDUCED_COLOR_SPACE:
    use_colors = {k: colors.cnames[k] for k in ['red', 'green', 'blue', 'black', 'yellow', 'purple']}
else:
    use_colors = colors.cnames

# translate hexstring to RGB tuple
named_colors = {k: tuple(map(int, (v[1:3], v[3:5], v[5:7]), 3*(16,)))
                for k, v in use_colors.items()}
named_colors['white'] = (255, 255, 255)
ncol = len(named_colors)

if REDUCED_COLOR_SPACE:
    ncol -= 1
    no_match = named_colors.pop('purple')
else:
    no_match = named_colors['purple']

# make an array containing the RGB values 
color_tuples = list(named_colors.values())
color_tuples.append(no_match)
color_tuples = np.array(color_tuples)

color_names = list(named_colors)
color_names.append('no match')

# get example picture
im = img.getdata().convert('RGB')

# build tree
tree = KDTree(color_tuples[:-1])
# tolerance for color match `inf` means use best match no matter how
# bad it may be
tolerance = np.inf
# find closest color in tree for each pixel in picture
dist, idx = tree.query(im, distance_upper_bound=tolerance)
# count and reattach names
counts = dict(zip(color_names, np.bincount(idx.ravel(), None, ncol+1)))
print(counts)

for cntry in flags.keys():
    fp = fldr + '\\' + cntry + '-flag.gif'
    img = Image.open(fp)
    width, height = img.size
    im = img.getdata().convert('RGB')
    dist, idx = tree.query(im, distance_upper_bound=tolerance)
    counts = dict(zip(color_names, np.bincount(idx.ravel(), None, ncol+1)))
    flags[cntry] = {'colours': counts, 'W': width, 'H': height}

"""Cons = lower fidelity, slower. Pros = basically know what it's doing"""

with open('Outputs\\colourcounts.pickle', 'wb') as handle:
    pickle.dump(flags, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
# =============================================================================
# Put comparison flags in a similar layout
# =============================================================================

# As RGB
to_compare = dict()
for i in range(1,4):
    fp = 'Scrambled\\flag_' + str(i) + '.png'
    img = Image.open(fp)
    width, height = img.size
    im = img.getdata().convert('RGB')
    dist, idx = tree.query(im, distance_upper_bound=tolerance)
    counts = dict(zip(color_names, np.bincount(idx.ravel(), None, ncol+1)))
    to_compare[i] = {'colours': counts, 'W': width, 'H': height}

with open('Outputs\\comparecolourcounts.pickle', 'wb') as handle:
    pickle.dump(to_compare, handle, protocol=pickle.HIGHEST_PROTOCOL)