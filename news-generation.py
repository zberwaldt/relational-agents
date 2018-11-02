from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path
import urllib.parse
from textwrap import dedent
import os
import sys
import re
import shutil

publication_url = "https://relationalagents.com/"

page = urlopen(publication_url)

soup = BeautifulSoup(page, 'html.parser')

news_items = soup.find('section', attrs={'class': 'whats-new'}).find_all('li')

for item in news_items:
    links = item.find_all('a')
    for link in links:
        match = re.sub(link.text, item.text).group(0)
        print(match)
        mdLinkText = f'bloop'
        linkHref = f'({link['href']})'
