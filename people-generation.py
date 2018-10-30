from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path
import urllib.parse
from textwrap import dedent
import os
import sys
import re
import shutil

publication_url = "https://relationalagents.com/publications/index.html"

page = urlopen(publication_url)

soup = BeautifulSoup(page, 'html.parser')

regex = re.compile('[.,;:*^%$#@!~`]', flags=0)
author_search = re.compile(r'\w+, \w{1}\.?')

pub_years = [
    "2001", 
    "2004", 
    "2005", 
    "2006", 
    "2007", 
    "2008", 
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    ]

os.chdir('content\\publication')

for year in pub_years:
    if not os.path.exists(year):
        os.makedirs(year)
        os.chdir(year)
        list_index = open('_index.md', 'w')
        list_index_content=f'---\ntitle: "{year}"\nlayout: years/list\n---\n'
        list_index.write(list_index_content)
        list_index.close()
        
    year_of_pubs = soup.find('ul', attrs={'id': year})
    publications = year_of_pubs.find_all('li', attrs={'class': 'publication'})

    for publication in publications:       
        
        #get the title of the publication
        title = publication.find('h3').text.strip()
        
        # add the name to the name field
        processed_title = regex.sub("", title)
        processed_title = '-'.join(processed_title.split(" ")[:6]).lower()
        processed_title = processed_title.replace('?', '')

        # create a directory with the prcessed_title
        # then change into it.
        if not os.path.exists(processed_title):
            os.makedirs(processed_title)
            os.chdir(processed_title)
        else:
            os.makedirs(processed_title + "2")
            os.chdir(processed_title + "2")
                
        # create an index file for the project
        content_file = open('index.md', 'w')
        
        # add the front matter
        content_to_write = '---\n'
        
        content_to_write += f'name: "{processed_title.replace("-", " ").title()}"\n'

        # add the full paper title
        content_to_write += f'title: "{title}"\n'
        
        # add null project
        content_to_write += 'project: null\n'
        
        journal = publication.find('p', attrs={'class', 'journal'}).text.strip()
        content_to_write += f'event: "{journal}"\n'
        # add author list to
        content_to_write += 'authors:\n'
        
        # get the authors of the paper and split them into an array
        if publication.find('p', attrs={'class', 'authors'}) is not None:
            authors = publication.find('p', attrs={'class', 'authors'}).text.strip()
            authors = re.findall(author_search, authors)
            for author in authors:
                content_to_write += f'- name: "{author}."\n'
        
        # I made a mistake on the old site, so below is to compensate for the error.
        if publication.find('p', attrs={'class', 'authos'}) is not None:
            authos = publication.find('p', attrs={'class', 'authos'}).text.strip()
            authos = re.findall(author_search, authos)
            for autho in authos:
                content_to_write += f'- name: "{autho}."\n'

        content_to_write += f'year: {year}\n'

        #now check if there is a url
        if publication.find('a') is not None:
    
            link = publication.find('a')
    
            if re.search(r'\.pdf', link['href']) is not None:
    
                pdf_link = re.search(r'.+\.pdf', link['href']).group(0)
    
                content_to_write += 'resources:\n'
    
                content_to_write += f'- name: "{pdf_link[:-4].replace(".", " ")}"\n'
    
                content_to_write += f'  src: "{pdf_link}"\n'
    
                project_dir = os.getcwd()
    
                os.chdir('..\\..')
    
                if Path(os.path.realpath(pdf_link)).exists():
                    project_pdf_loc = os.path.realpath(pdf_link)
                    shutil.move(project_pdf_loc, f'{project_dir}\\{pdf_link}')
                else:
                    print(f"this file: {pdf_link}, does not exist. go download it and place it in the {project_dir}")
                os.chdir(project_dir)
            else: 
                content_to_write += 'resources: null\n'

            if re.search('https?://.+', link['href']) is not None:
                external_link = re.search('https?://.+', link['href']).group(0)
                content_to_write += f'external_url: {external_link}\n'
            else:
                content_to_write += 'external_url: null\n'        
                # if re.match('https://'):
        else:
            content_to_write += 'resources: null\nexternal_url: null\n'
        
        content_to_write += 'draft: false\n'

        # finally add the closing dashes for the front matter
        content_to_write += '---'

        # now write the contents to the the index file
        content_file.write(content_to_write)

        # now close the index file.
        content_file.close()    
    
        # now return to the parent directory, which should be the year of publication
        os.chdir('..')
  
    # return to the root content directory
    os.chdir('..')
