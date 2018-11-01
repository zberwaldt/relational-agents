from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path
import urllib.parse
from textwrap import dedent
import os
import sys
import re
import shutil

publication_url = "https://relationalagents.com/humans/"

page = urlopen(publication_url)

soup = BeautifulSoup(page, 'html.parser')

os.chdir('content\\people')

people = soup.find_all('a', attrs={'class': 'people'})

detail_regex = re.compile(r'#(.*)$')

person_index = open('team.yaml', 'w')
team_content = "---\n"

for person in people:
    
    if person['href'] is not '#':
        detail_id = detail_regex.search(person['href']).group(1)
        person_detail = soup.find('form', attrs={'id': f'{detail_id}'})
    else:
        print(f"This is a new person. {person.find('p', attrs={'class': 'name'}).text.strip()}")
    
    bio = person_detail.find('p').text.strip()
    img = person.find('img')['src']
    name = person.find('p', attrs={'class': 'name'}).text.strip()
    role = person.find('p', attrs={'class': 'role'}).text.strip()
    alumni = "alumni: false\n"
    
    team_content += f'- name: "{name}"\n'
    team_content += '   params:\n'
    team_content += '    alumni: false\n'
    team_content += f'    role: "{role}"\n'
    team_content += f'    bio: | \n"{bio}"\n'
    team_content += f'  src: {img}\n'
    
team_content += "---\n"
person_index.write(team_content)
person_index.close()


alumni = soup.find_all('div', attrs={'class': 'people'})
alum_index = open('alumni.yaml', 'w')
alum_content = "---\n"

for alum in alumni:
    img = alum.find('img')['src']
    name = alum.find('p', attrs={'class': 'name'}).text.strip()
    role = alum.find('p', attrs={'class': 'role'}).text.strip()
    current = "alumni: true\n"
    
    alum_content += f'- name: "{name}"\n'
    alum_content += '   params:\n'
    alum_content += '    alumni: true\n'
    alum_content += f'    role: "{role}"\n'
    alum_content += f'  src: {img}\n'
    
alum_content += "---\n"
alum_index.write(alum_content)
alum_index.close()