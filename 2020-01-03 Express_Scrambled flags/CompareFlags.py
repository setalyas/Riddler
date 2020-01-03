# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:58:54 2020

@author: setat
"""

import pickle
import numpy as np
import shutil

# =============================================================================
# Compare the images to the dict
# =============================================================================

main_fp = open('Outputs\\colourcounts.pickle', 'rb')
flags = pickle.load(main_fp)
compare_fp = open('Outputs\\comparecolourcounts.pickle', 'rb')
to_compare = pickle.load(compare_fp)
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

# Check exact matches
for i, check in to_compare.items():
    matches = {key: value['colours']
                for key, value in flags.items()
                if value['colours']==check['colours'] and
                value['aspect']==check['aspect']}
    print(i, matches)
# Hm, only the Brazilian flag matches exactly

# Check closest match
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
print(res)

"""Results:
['FR', 'FS', 'IP', 'NC', 'RN', 'TB'] - all the French flag!
['BR']
['WA']
"""

# Copy matching flags to new folder
for k, v in res.items():
    base = 'Outputs\\' + str(k)
    scrambled = 'Scrambled\\flag_' + str(k) + '.png'
    scrambledcp = base + '.png'
    shutil.copy(scrambled, scrambledcp)
    for c in v:
        src = 'Flags\\' + c + '-flag.gif'
        dest = base + c + '.gif'
        shutil.copy(src, dest)