from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path
import urllib.parse
from textwrap import dedent
import os
import sys
import re
import shutil

publication_url = "https://relationalagents.com/publications/"

page = urlopen(publication_url)

soup = BeautifulSoup(page, 'html.parser')

