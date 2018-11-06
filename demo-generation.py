from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path
import urllib.parse
from textwrap import dedent
import os
import sys
import re
import shutil


urls = {
    'litebody' : 'https://relationalagents.com/litebody.html',
    'dtask': 'https://relationalagents.com/dtask.html',
    'hbco' : 'https://relationalagents.com/hbco.html'
}

os.chdir('content\\demo')

for key, url in urls.items():
    frontmatter = dedent(f"""---
title: "{key}"
draft: false
---

    """)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    demo_title = soup.find('article', attrs={'id': 'download-mainbody'}).find('h2').text.strip()
    content = f"{demo_title}\n=======\n\n"
    demo_paras = soup.find('article', attrs={'id': 'download-mainbody'}).find_all('p')
    for p in demo_paras:
        text = p.text.strip()
        p_links = p.find_all('a')
        formatted = ""
        for link in p_links:
            link_text = link.text.strip()
            formatted = re.sub(f'{link_text}', f'[{link_text}]({link["href"]})', text)

        content += f"{formatted}\n\n"

    with open(f'{key}.md', 'w') as demo_file:
        demo_file.write(frontmatter)
        demo_file.write(content)
        
        


