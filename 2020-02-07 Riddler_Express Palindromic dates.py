# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:46:03 2020

@author: setat
"""

import datetime as dt

start = dt.date(2020, 2, 2)

reverse = lambda st: st[::-1]

start = dt.datetime(2020, 2, 2)
end = dt.datetime(2099, 12, 31)
remaining = (end-start).days

date = start
dttypes = {'UK': {'counter': 0, 'fmt': '%d%m%Y',
                  'printfmt': '%d-%m-%Y', 'matches': []},
           'US': {'counter': 0, 'fmt': '%m%d%Y',
                  'printfmt': '%m-%d-%Y', 'matches': []}}

for i in range(remaining): 
    date += dt.timedelta(days=1)
    for region in dttypes.keys():
        fmt = dttypes[region]['fmt']
        if date.strftime(fmt) == reverse(date.strftime(fmt)):
            dttypes[region]['matches'].append(date)
            dttypes[region]['counter'] += 1

for region in dttypes.keys():
    counter = dttypes[region]['counter']
    print('\n{} palindrome dates this century after 02/02/2020: {}'.format(
            region, counter
            ))
    for i in dttypes[region]['matches']:
        print(i.strftime(dttypes[region]['printfmt']))