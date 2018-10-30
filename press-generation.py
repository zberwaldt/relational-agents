from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path
import urllib.parse
from textwrap import dedent
import os
import sys
import re
import shutil

publication_url = "https://relationalagents.com/press/index.html"

page = urlopen(publication_url)

soup = BeautifulSoup(page, 'html.parser')

press_name_regex = re.compile(r'- (.*)')

date_regex = re.compile(r'\d+\/\d+(\/\d+)?')

os.chdir('content\\press')

print(os.getcwd())

out_file = open('index.md', 'w')

out_content = '---\ntitle: "Press"\n'

out_content += 'press:\n'

press_list = soup.find('ul', attrs={'class': 'press-list'})

press_items = press_list.find_all('li')

for item in press_items:
    
    link = item.find('a')
    
    link_href = link['href']
    
    item_h3 = link.find('h3').text.strip()
    
    title = press_name_regex.search(item_h3).group(1)
    
    out_content += f'- title: "{title}"\n'
    
    date = date_regex.search(item_h3).group(0)
    
    out_content += f'  date: "{date}"\n'

    out_content += f'  href: "{link_href}"\n'

    description = link.find('p', attrs={'class': 'news-description'})
    
    if description is None:
    
        description = link.find('p')
    
    description_text = description.text.strip()

    description_text = description_text.replace('\"', '')

    out_content += f'  description: "{description_text}"\n'

out_content += '---'

out_file.write(out_content)

out_file.close()