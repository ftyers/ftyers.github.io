import requests
from bs4 import BeautifulSoup
import os
#from os import listdir
#from os.path import isfile, join, dirname
import io
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()

req = requests.get(args.url).text
soup = BeautifulSoup(req,"lxml")
text_items = soup.findAll('p')
save_to_file = []
for item in text_items:
	save_to_file.append(item.text)
	
index = -1
name = args.url.split('/')[index] 
if (name ==''):
	name =  args.url.split('/')[index - 1] + '.txt'
else:
	name += '.txt'
	
dirname = os.path.dirname(__file__)
onlyfiles = [f for f in os.listdir(os.path.join(dirname, "test_output")) if os.path.isfile(join(os.path.join(dirname, "test_output"), f))]
if (name in onlyfiles):
	name = 'new_' + name
file_name = os.path.join(dirname, "test_output", name)   
with io.open(file_name, "w+") as newsfile:
	for line in save_to_file:
		newsfile.write(line + '\n')
print('saved with name = ', name)