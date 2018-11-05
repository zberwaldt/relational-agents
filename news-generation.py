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

news_file = open('news.txt', 'w')

news_content = ""

for item in news_items:
    links = item.find_all('a')
    item_text = item.text
    match = dedent(item.text)
    for link in links:
        link_text = link.text.strip()
        link_href = link['href']
        match = re.sub(f'{link_text}', f'[{link_text}]({link_href})', match)
    news_content += f"NEWS: \n\n {match} \n\n"

news_file.write(news_content)
news_file.close()
        



