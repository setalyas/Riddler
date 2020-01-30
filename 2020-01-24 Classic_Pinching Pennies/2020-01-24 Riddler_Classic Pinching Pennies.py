# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 03:19:45 2020

@author: setat

The game starts with somewhere between 20 and 30 pennies, which I then divide
into two piles any way I like. Then we alternate taking turns, with you first,
until someone wins the game. For each turn, a player may take any number of
pennies he or she likes from either pile, or instead take the same number of
pennies from both piles. Each player must also take at least one penny every
turn. The winner of the game is the one who takes the last penny.

If we both play optimally, what starting numbers of pennies (again, between 20
and 30) guarantee that you can win the game?
"""

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import math
import imageio

penny_min = 20
penny_max = 30
pennies = range(penny_min, penny_max+1)

# Calculate the cold spots
golden = (1 + 5 ** 0.5) / 2
cold = set([])
k_max = int(penny_max // (golden**2))
for k in range(k_max+1):
    n = math.floor(k*golden)
    m = n + k
    cold.add((n, m))
    cold.add((m, n))
print(cold)

# Set up the array
data = np.zeros((penny_max+1, penny_max+1))

# Add the hot spots
hot = set([])
for (x, y) in cold:
    up = [(x, y+i) for i in range(1, penny_max-y+1)]
    right = [(x+i, y) for i in range(1, penny_max-x+1)]
    diag = [(x+i, y+i) for i in range(1, penny_max-max(x, y)+1)]
    hot = hot.union(up, right, diag)

print(hot.intersection(cold) == set([]))  # No spots are both hot and cold

# Prepare for colormap plotting
for (x, y) in hot:
    data[x, y] = 1  # red
for (x,y) in cold:
    data[x,y] = 2  # blue

# Print the non-cold non-hot locations
(x_arr, y_arr) = np.where(data==0)
print(max(len(x_arr), len(y_arr)) == 0)
# Print any not cold not hot cells 
for x in zip(x_arr, y_arr):
    print(x)
# All spots are either hot or cold

def showprintgrid(arr, colmap):
    """Set up an array like a Wythoff board, and plot with provided
    colourmap"""
    arr_flip = np.flipud(arr)  # to make it match normal graph orientation
    fig, ax = plt.subplots(figsize=(6,6))
    ax.matshow(arr_flip, cmap=colmap)
    ax.grid(which='major', axis='both', linestyle='-', color='k')
    # draw gridlines
    ax.set_xticks(np.arange(-0.5, penny_max+1, 1))
    ax.set_yticks(np.arange(-0.5, penny_max+1, 1))
    ax.set_xticklabels(np.arange(penny_max+1))
    ax.set_yticklabels(np.arange(penny_max+1)[::-1])


# Create discrete colormap
col_rb = colors.ListedColormap(['red', 'blue'])
showprintgrid(data, col_rb)
plt.savefig('20200124_Classic_{}.png'.format('AllHotCold'))

# Which n would be best to pick if you wanted to win?
best_n = set([])
for (x, y) in cold:
    if penny_min <= x+y <= penny_max:
        best_n.add(x+y)
        print((x,y))
print(best_n)

# grid with only viable colours, for each n combo
col_wrb = colors.ListedColormap(['white', 'red', 'blue'])
for n in range(penny_min, penny_max+1):
    data_n = np.copy(data)
    for x in range(penny_max+1):
        for y in range(penny_max+1):
            if x+y > n:
                data_n[x,y] = 0  # white
    txt = "Win"
    txtcol = "green"
    if n in best_n:
        txt = "Lose"
        txtcol = "black"
    txt += '\nn={}'.format(n)
    showprintgrid(data_n, col_wrb)
    t = plt.text(23, 5, txt, fontweight='bold', color='white', fontsize=20)
    t.set_bbox(dict(facecolor=txtcol))
    plt.savefig('20200124_Classic_HotCold{}.png'.format(n))

# GIFify
fps = ['20200124_Classic_HotCold{}.png'.format(n) for n
       in range(penny_min, penny_max + 1)]
images = []
for fp in fps:
    images.append(imageio.imread(fp))
imageio.mimsave('20200124_Classic_HotCold.gif', images, duration=1)

# What numbers do you want "I" to pick so "you" can win the game?
print([i for i in range(penny_min, penny_max+1) if i not in best_n])