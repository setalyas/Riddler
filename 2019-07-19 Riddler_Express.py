# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:43:51 2019

@author: setat
"""

"""You are given an empty 4-by-4 square and one marker. You can color in the
individual squares or leave them untouched. After you color as many or as few
squares as you’d like, I will secretly cut out a 2-by-2 piece of it and then
show it to you without rotating it. You then have to tell me where it was
(e.g., “top middle” or “bottom right,” etc.) in the original 4-by-4 square.

Can you design a square for which you’ll always know where the piece came from?"""

import numpy as np

gridsize = 4

# All 4-len binary numbers
binInts = []
for bit in range(2**gridsize):
    binInts.append(np.binary_repr(bit))
for i in range(len(binInts)):
    _ = "0"*(gridsize-len(binInts[i]))
    binInts[i] = _ + binInts[i]

# Make them into grid rows
binRow = []
for i in range(len(binInts)):
    binRow.append(["".join(binInts[i][j]) for j in range(gridsize)])

# To array
binRow = np.array(binRow) # turned into ints, but then just turned back later so removed

# Merge rows into 4x4 grid arrays
grids = []
for i in range(len(binRow)):
    for j in range(len(binRow)):
        for k in range(len(binRow)):
            for l in range(len(binRow)):
                _ = np.append(np.append(np.append(binRow[i],binRow[j]),binRow[k]),binRow[l])
                grids.append(_.reshape(gridsize,gridsize))

# Merge rows into 3x3 grid arrays
#grids = []
#for i in range(len(binRow)):
#    for j in range(len(binRow)):
#        for k in range(len(binRow)):
#                _ = np.append(np.append(binRow[i],binRow[j]),binRow[k])
#                grids.append(_.reshape(gridsize,gridsize))

#65536 gridsx9 subgrids = 589824 choices => can just iterate over then
slicesize = 2
steps = gridsize-slicesize+1 # how many steps across the grid the slice can take

goodGrids = []
for grid in grids:
    slices = []
    # take slices of the grid
    for i in range(steps):
        for j in range(steps):
            paper = grid[i:i+slicesize,j:j+slicesize]
            slices.append(paper)
    sliceStr = []
    for paper in slices:
        line = ""
        for i in range(slicesize):
            for j in range(slicesize):
                line += paper[0:slicesize,0:slicesize][i][j]
        sliceStr.append(line)
    sliceClean = np.unique(sliceStr)
    if len(sliceClean) == len(sliceStr):
        goodGrids.append(grid)
        
import matplotlib.pyplot as plt
import matplotlib.cm as cm
gridBig = goodGrids[123].repeat(10, axis=0).repeat(10, axis=1).astype(int)
plt.imsave('grid'+str(123)+'.png', gridBig, cmap=cm.gray)

for i in range(10,len(goodGrids)):
    for_exp = goodGrids[i].repeat(10, axis=0).repeat(10, axis=1).astype(int)
    num = "0"*(4-len(str(i))) + str(i)
    plt.imsave('grid'+num+'.png', for_exp, cmap=cm.gray)

import glob
files = glob.glob(r"C:\Users\setat\Documents\Python Scripts\WhereInTheSquare\*.png")

import imageio
images = []
for filename in files:
    images.append(imageio.imread(filename))
imageio.mimsave(r'C:\Users\setat\Documents\Python Scripts\grids2.gif', images)