# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:02:11 2019

@author: setat

You have a playlist with exactly 100 tracks (i.e., songs), numbered 1 to 100.
To go to another track, there are two buttons you can press: (1) “Next,” which
will take you to the next track in the list or back to song 1 if you are
currently on track 100, and (2) “Random,” which will take you to a track chosen
uniformly from among the 100 tracks. Pressing “Random” can restart the track
you’re already listening to — this will happen 1 percent of the time you press
the “Random” button.

For example, if you started on track 73, and you pressed the buttons in the
sequence “Random, Next, Random, Random, Next, Next, Random, Next,” you might
get the following sequence of track numbers:
    73, 30, 31, 67, 12, 13, 14, 89, 90.
You always know the number of the track you’re currently listening to.

Your goal is to get to your favorite song (on track 42, of course) with as
few button presses as possible. What should your general strategy be? Assuming
you start on a random track, what is the average number of button presses you
would need to make to reach your favorite song?
"""

import numpy as np; np.random.seed(44321)
import matplotlib.pyplot as plt; plt.style.use('ggplot')
import pandas as pd

# Thoughts: good strategy is "random til within X of 42, then repeated next"

# Set parameters
mn = 1
mx = 100
target = 42
proximity = 10

# Trial a while loop
counter = 1
place = np.random.randint(mn, mx+1)
print(place, counter)
while (target - place) > proximity or (place > target):
    place = np.random.randint(mn, mx+1)
    counter += 1
    print(place,counter)
while place != target:
    place += 1
    counter += 1
    print(place, counter)
print(place, counter)

# Do 1000 times
repts = 1000
clicks = []
for i in range(repts):
    counter = 1
    place = np.random.randint(mn, mx+1)
    while (target - place) > proximity or (place > target):
        place = np.random.randint(mn, mx+1)
        counter += 1
    while place != target:
        place += 1
        counter += 1
    clicks.append(counter)
plt.hist(clicks)
np.mean(clicks)

# Do 1000 times per proximity
repts = 10000
results = pd.DataFrame(index=range(mn, mx+1), columns=['avg clicks'])
for proximity in range(mn, mx+1):
    clicks = []
    for i in range(repts):
        counter = 1
        place = np.random.randint(mn, mx+1)
        while (target - place) > proximity or (place > target):
            place = np.random.randint(mn, mx+1)
            counter += 1
        while place != target:
            place += 1
            counter += 1
        clicks.append(counter)
    results.loc[proximity] = np.mean(clicks)

results.plot()
plt.xlabel('Stopping gap')
plt.ylabel('avg clicks')
plt.show()

print(results.loc[results['avg clicks'] == min(results['avg clicks'])])