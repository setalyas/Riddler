# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:14:09 2020

@author: setat
"""

from bs4 import BeautifulSoup
import requests
from PIL import Image

url = "https://www.cia.gov/library/publications/the-world-factbook/docs/flags\
oftheworld.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

url_parent = '/'.join(url.split('/')[:-2])  # url folder above docs

img_url = ""

for item in soup.select(".flag-image img"):
    img_url = url_parent+item['src'][2:]
    img_name = 'Flags\\' + img_url.split('/')[-1]
    img = Image.open(requests.get(img_url, stream = True).raw)
    img.save(img_name)