# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:42:04 2020

@author: setat

During a break at a music festival, the crew is launching T-shirts into the
audience using a T-shirt cannon. And you’re in luck — your seat happens to be
in the line of flight for one of the T-shirts! In other words, if the cannon
is strong enough and the shirt is launched at the right angle, it will land in
your arms.

The rows of seats in the audience are all on the same level (i.e., there is no
incline), they are numbered 1, 2, 3, etc., and the T-shirts are being launched
from directly in front of Row 1. Assume also that there is no air resistance
(yes, I know, that’s a big assumption). You also happen to know quite a bit
about the particular model of T-shirt cannon being used — with no air
resistance, it can launch T-shirts to the very back of Row 100 in the audience,
but no farther.

The crew member aiming in your direction is still figuring out the angle for
the launch, which you figure will be a random angle between zero degrees
(straight at the unfortunate person seated in Row 1) and 90 degrees (straight
up). Which row should you be sitting in to maximize your chances of nabbing the
T-shirt?
"""

import math
import matplotlib.pyplot as plt; plt.style.use('ggplot')

# https://en.wikipedia.org/wiki/Range_of_a_projectile
dist = lambda theta: 100 * math.sin(2*theta)
dist(math.pi/4)

ang = lambda d: math.degrees(0.5 * math.asin(d/100))
ang(100)

seats = {}
for seat in range(1, 100+1):
    seats[seat] = ang(seat) - ang(seat - 1)

plt.plot(seats.values())
plt.xlabel('Seat')
plt.ylabel('Angle range to get seat')