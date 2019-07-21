# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 00:32:19 2019

@author: setat
"""

# =============================================================================
# 2019-03-01 https://fivethirtyeight.com/features/youre-home-alone-you-can-buy-zillions-of-video-game-cigarettes-or-beat-yourself-at-bananagrams/
# In the video game “Red Dead Redemption 2,” there is a side quest where the
# main character is supposed to collect 12 sets of cigarette cards, each
# consisting of 12 unique cards.
# 
# Some cards can be found lying around in the open world, but the easiest way to
# collect the cards is to buy cigarettes at the store and collect the single
# random card included in each pack. Suppose Arthur is too lazy to look for cards
# in the open world and tries to complete the set only by buying packs at the store.
# 
# At $5 a pack, how much money do we expect Arthur to spend to complete all 12 sets?
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

letts = ['a','b','c','d','e','f','g','h','i','j','k','l']
numbs = range(1,13)
cards = []
for a in letts:
    for i in numbs:
        cards.append(a + '_' + str(i).zfill(2))
cards.sort()

total_tries = []
    
while len(total_tries) < 10000:
    found = set([])
    tries = 0
    while len(found) < 144:
        x = np.random.randint(0,144)
        found.add(cards[x])
        tries = tries + 1
    total_tries.append(tries)
    
print('Arthur should expect to spend','$'+str(np.median(total_tries)*5),'on cigs')

plt.style.use('seaborn-notebook')
plt.hist(total_tries, 20, alpha=0.5)
plt.show()
