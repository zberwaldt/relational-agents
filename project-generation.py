from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path
import urllib.parse
from textwrap import dedent
import os
import sys
import re
import shutil

publication_url = "https://relationalagents.com/projects/index.html"

page = urlopen(publication_url)

soup = BeautifulSoup(page, 'html.parser')

os.chdir('content\\project')

project_nav = soup.find('nav', attrs={'class': 'project-nav'})

project_link_list = project_nav.find('ul')

link_list_items = project_link_list.find_all('li')

for item in link_list_items:

    if item.find('a'):

        link = item.find('a')
        
        link_text = link.contents[0]
        
        processed_link = link_text.replace(' ', '-').lower()
        
        if not os.path.exists(processed_link):
            os.makedirs(processed_link)
            os.chdir(processed_link)

        project_index_file = open('index.md', 'w')

        href = link['href']
        
        project_url = f'https://relationalagents.com/projects/{href}'
        
        project_page = urlopen(project_url)
        
        project_soup = BeautifulSoup(project_page, 'html.parser')
        
        out_content = '---\n'
        
        project_content = project_soup.find('article', attrs={'class': 'project'})

        if project_content.find('h2'):
        
            project_title = project_content.find('h2').text.strip()
        
        else: 
        
            project_title = project_content.find('h3').text.strip()
        
        if project_content.find_all('img'):
        
            project_images = project_content.find_all('img')
        
        out_content += f'title: {project_title}\n'
        
        out_content += f'url: {processed_link}\n'
        
        out_content += f'resources:\n'
        
        for img in project_images: 
            src = img['src']
        
            out_content += f'- name: main image\n'
        
            out_content += f'  src: {src}\n'
        
        out_content += f'draft: false\n'

        project_articles = project_content.find_all('p')
        
        out_content += '---\n\n'
        
        for article in project_articles:

            out_content += f'{article.text.strip()}\n\n'

        project_index_file.write(out_content)
        
        project_index_file.close()
        
        # output a file on the related publications for later
        
        if project_content.find('ul'):
            related_pubs = open('related-text.txt', 'w')
            pub_content = ''
            pub_list = project_content.find('ul').find_all('li')
            for pub in pub_list:
                pub_content += f'{pub.text.strip()}\n\n'
            related_pubs.write(pub_content)
            related_pubs.close()

        os.chdir('..')
        


