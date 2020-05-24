# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:02:16 2020

@author: setat

Over the course of three days, suppose the probability of any spammer making a
new comment on this week’s Riddler column over a very short time interval is
proportional to the length of that time interval. (For those in the know, I’m
saying that spammers follow a Poisson process.) On average, the column gets one
brand-new comment of spam per day that is not a reply to any previous comments.
Each spam comment or reply also gets its own spam reply at an average rate of
one per day.

For example, after three days, I might have four comments that were not replies
to any previous comments, and each of them might have a few replies (and their
replies might have replies, which might have further replies, etc.).

After the three days are up, how many total spam posts (comments plus replies)
can I expect to have?
"""

import math

# =============================================================================
# Resolution = 1 day at a time
# =============================================================================

# P(k events in interval} = rate^k * e^-k / k!

daily_comments = lambda k: 1 / (math.factorial(k) * math.e)

for k in range(10):
    print('{} spam comments per day: {}'.format(k, daily_comments(k)))
    
daily_replies = lambda k, r: (k ** r) * (math.e ** (-k)) / (math.factorial(r))

# 
for k in range(10):
    for r in range(10):
        day1comments = daily_comments(k)
        day2replies = daily_replies(day1comments, r)
        print('{} prev comments, {} replies: {}'.format(k, r, day2replies))
# If k is zero, then 
        
MOVED TO JUPYTER NOTEBOOK