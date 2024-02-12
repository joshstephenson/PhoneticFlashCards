import re
import urllib
import os.path
import time
from urllib.request import urlretrieve

with open('foo2.html', 'r') as f:
    lines = f.readlines()

for line in lines:
    for match in re.finditer(r'(\/\/.+mp3)', line):
        url = match.groups()[0]
        filename = "/".join(['ipa_audio', 'consonants', url.split('/')[-1]])

        if not os.path.isfile(filename):
            print(f'Downloading {filename}')
            urlretrieve(f'https:{url}', filename)
            time.sleep(3)
        else:
            print(f'Already have {filename}')

