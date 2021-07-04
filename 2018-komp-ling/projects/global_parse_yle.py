import requests
from bs4 import BeautifulSoup
import os
import io
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()

#print(args.url)
yle_url = requests.get(args.url).text
y_soup = BeautifulSoup(yle_url,"lxml")

def read_article(url):
    #print("current url is", url)
	req = requests.get(url).text
	soup = BeautifulSoup(req,"lxml")
	text_items = soup.findAll('p')
	save_to_file = []
	for item in text_items:
		save_to_file.append(item.text)
		
	index = -1
	name = url.split('/')[index] 
	if (name ==''):
		name =  url.split('/')[index - 1] + '.txt'
	else:
		name += '.txt'
		
	dirname = os.path.dirname(__file__)
	onlyfiles = [f for f in os.listdir(os.path.join(dirname, "test_output")) if os.path.isfile(os.path.join(os.path.join(dirname, "test_output_yle_parser"), f))]
	if (name in onlyfiles):
		print("Such text has already been parsed")
		return
		#name = 'new_' + name
	file_name = os.path.join(dirname, "test_output", name)   
	with io.open(file_name, "w+") as newsfile:
		for line in save_to_file:
			try:
				newsfile.write(line + '\n')
			except:
				print("failed to write output data")
				return
	print('saved with name = ', name)

except_list =["https://yle.fi/", "https://yle.fi/urheilu/"]
	
a = y_soup.find_all('a')	
for i in a:
    if "https://yle.fi/" in i.get('href') and i.get('href') not in except_list :
        #print(i.get('href'))
        read_article(i.get('href'))