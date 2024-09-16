import re
import statistics
from os import listdir, remove
from os.path import isfile, join
from nltk import sent_tokenize

import argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-p", help = "path to processed files")
parser.add_argument("-o", help = "path to output")
parser.add_argument("-l", help = "level of processed data")
args = parser.parse_args()

text = []
onlyfiles = [f for f in listdir(args.p) if isfile(join(args.p, f))]

for filename in onlyfiles:
	with open(join(args.p,filename),"r", encoding = "utf-8") as f:
		try:
			paragraphs = re.split('\n',f.read())
		except:
			paragraphs = [line.rstrip('\n') for line in open(join(args.p,filename))]
		paragraphs = list(filter(None, paragraphs))
		current_unit = []
		current_unit_length = 0
		for par in paragraphs:
			sent_text = sent_tokenize(par) # this gives us a list of sentences
			
			if current_unit_length < 10:
				current_unit.append(par)
				current_unit_length += len(sent_text)
			elif current_unit_length >= 10:
				text.append(current_unit)
				
				current_unit = []
				current_unit_length = len(sent_text)
				
				current_unit.append(par)

	unit_index = 0
for unit in text:
	name = str(unit_index) + "_" + str(args.l) + ".txt"
	with open(join(args.o, name),"w+", encoding = "utf-8") as edited_file:
		for u in unit:
			edited_file.write(u + ' ')
	unit_index += 1