import os
from pathlib import Path
import shutil

os.chdir('content\\publication')

for filename in os.listdir('.'):

    current_file = Path(os.path.realpath(filename))
    
    if os.path.isdir(current_file):
        os.chdir(current_file)
        for pub in os.listdir(current_file):
            print(pub)
        os.chdir('..')
        