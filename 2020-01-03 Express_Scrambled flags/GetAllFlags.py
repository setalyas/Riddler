# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:14:09 2020

@author: setat
"""

from bs4 import BeautifulSoup
import requests
from PIL import Image
import pandas as pd

url = "https://www.cia.gov/library/publications/the-world-factbook/docs/flags\
oftheworld.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

url_parent = '/'.join(url.split('/')[:-2])  # url folder above docs

names = {}
img_url = ""

for item in soup.select(".flag-image img"):
    img_url = url_parent+item['src'][2:]
    fn = img_url.split('/')[-1]
    country_code = fn[:2]
    img_name = 'Flags\\' + fn
    img = Image.open(requests.get(img_url, stream = True).raw)
    img.save(img_name)
    names[country_code] = item['alt']

names = {key: value.replace(' Flag', '') for key, value in names.items()}
names = pd.DataFrame.from_dict(names, orient='index', columns=['name'])
names.to_csv('Outputs\\names.csv')
