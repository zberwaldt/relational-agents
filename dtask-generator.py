from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path
import urllib.parse
from textwrap import dedent
import os
import sys
import re
import shutil


url = 'https://relationalagents.com/dtask.html'

page = urlopen(url)

os.chdir('content\\demo')

soup = BeautifulSoup(page, 'html.parser')
        
dtask_body = soup.find('article', attrs={'id': 'download-mainbody'})

with open('dtask2.md', 'w') as file:
    file.write(f"{dtask_body}")

