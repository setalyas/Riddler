# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:29:05 2019

@author: setat

You are given a fair, unweighted 10-sided die with sides labeled 0 to 9 and a
sheet of paper to record your score. (If the very notion of a fair 10-sided die
bothers you, and you need to know what sort of three-dimensional solid it is,
then forget it — you have a random number generator that gives you an integer
value from 0 to 9 with equal probability. Your loss — the die was a collector’s
item.)

To start the game, you roll the die. Your current “score” is the number shown,
divided by 10. For example, if you were to roll a 7, then your score would be
0.7. Then, you keep rolling the die over and over again. Each time you roll, if
the digit shown by the die is less than or equal to the last digit of your
score, then that roll becomes the new last digit of your score. Otherwise you
just go ahead and roll again. The game ends when you roll a zero.

For example, suppose you roll the following: 6, 2, 5, 1, 8, 1, 0. After your
first roll, your score would be 0.6, After the second, it’s 0.62. You ignore
the third roll, since 5 is greater than the current last digit, 2. After the
fourth roll, your score is 0.621. You ignore the fifth roll, since 8 is greater
than the current last digit, 1. After the sixth roll, your score is 0.6211. And
after the seventh roll, the game is over — 0.6211 is your final score.

What will be your average final score in this game?
"""

import numpy as np; np.random.seed(44321)
import itertools
import matplotlib.pyplot as plt; plt.style.use('ggplot')
import imageio

def isplit(itr,splt):
    _ = [list(g) for k,g in itertools.groupby(itr,lambda x:x in splt) if not k]
    return _

list2str = lambda lst: ''.join([str(x) for x in lst])

roll_count = 11000000
random_rolls = np.random.randint(0,10,roll_count)
goes = isplit(random_rolls,(0,))
scores = []
for rolls in goes:
    _ = [rolls[0]]
    for roll in rolls[1:]:
        if roll <= _[-1]:
            _ += [roll]
    scores.append(float('0.' + list2str(_)))
print(np.mean(scores)) # pi/6??

filenames = []
for i in [9*i for i in [1,2,5,10,20,50,100]]:
    plt.figure(figsize=(10,5))
    plt.hist(scores, bins=i)
    plt.xticks(np.linspace(0.1,1,19))
    ttl = 'Draws=' + str(len(goes)) + ', bins=' + str(i)
    plt.title(ttl)
    png = ttl.replace('=','').replace(',','').replace(' ','').title() + '.png'
    plt.savefig(png)
    filenames.append(png)

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('Riddler_20191115_Histogram.gif', images, duration=0.5)
