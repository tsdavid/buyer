#-*- coding: utf-8 -*-
#크롤러 따라하기
website_url = "https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/"


# parser.py
import requests
from bs4 import BeautifulSoup
import json
import os
import for_loop as test
# python파일의 위치
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#req = requests.get('https://www.waug.com')
#html = req.text
#print(html).encode('cp949')
#soup = BeautifulSoup(html, 'html.parser')
#my_titles = soup.select(
#    'h3 > a'
#    )

#data = {}

#for title in my_titles:
#    data[title.text] = title.get('href')

#with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
 #   json.dump(data, json_file)

for i in range(3):
    print test.waug_url[i]
    print test.myreal_url[i]