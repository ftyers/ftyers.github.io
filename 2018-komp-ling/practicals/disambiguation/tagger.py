# -*- coding: utf-8 -*-
###############################################################################
import sys
import random
from collections import defaultdict
import pickle

from perceptron import AveragedPerceptron

def _pc(n, d):
	return (float(n) / d) * 100

class PerceptronTagger():

	'''Greedy Averaged Perceptron tagger, as implemented by Matthew Honnibal.

	See more implementation details here:
		http://honnibal.wordpress.com/2013/09/11/a-good-part-of-speechpos-tagger-in-about-200-lines-of-python/

	:param load: Load the pickled model upon instantiation.
	'''

	START = ['-START-', '-START2-']
	END = ['-END-', '-END2-']

	def __init__(self, fname, load=True):
		self.model = AveragedPerceptron()
		self.tagdict = {}
		self.classes = set()
		self.model_file = fname
		if load:
			self.load(self.model_file)

	def tag(self, corpus, tokenise=False):
		'''Tags a string `corpus`.'''
		# Assume untokenised corpus has \n between sentences and ' ' between words
		#s_split = SentenceTokenizer().tokenise if tokenise else lambda t: t.split('\n')
		#w_split = WordTokenizer().tokenise if tokenise else lambda s: s.split()

		reading = True
		sentence = []
		line = corpus.readline()
		while reading:
			if line == '\n':
				# sentence boundary
				prev, prev2 = self.START
#				print('s:',sentence)
				for words in sentence:	
					context = self.START + [self._normalise(w[1]) for w in sentence] + self.END
					for i, token in enumerate(sentence):
						tag = self.tagdict.get(token[1])
						if not tag:
							# if the word isn't "unambiguous", extract features
							features = self._get_features(i, token[1], context, prev, prev2)
							# make the prediction
							tag = self.model.predict(features)
						sentence[i][3] = tag
						prev2 = prev
						prev = tag
				# print out the tokens and their tags
				for words in sentence:	
					print('\t'.join(words))
				print()
				sentence = []	
			elif line == '':
				# we reached the end of the input
				reading = False
			elif line[0] == '#':
				# line is a comment line
				print(line.strip())
				line = corpus.readline()
				continue
			else:
				# normal conllu line
				row = line.strip().split('\t')
				sentence.append(row)
				
			# read the next line
			line = corpus.readline()

		return 

	def train(self, sentences, save_loc=None, nr_iter=5):
		'''Train a model from sentences, and save it at ``save_loc``. ``nr_iter``
		controls the number of Perceptron training iterations.

		:param sentences: A list of 10-value tuples
		:param save_loc: If not ``None``, saves a pickled model in this location.
		:param nr_iter: Number of training iterations.
		'''
		self._make_tagdict(sentences)
		self.model.classes = self.classes
		for iter_ in range(nr_iter):
			c = 0
			n = 0
#			for words,tags in sentences:
			for sentence in sentences:
#				print(c, n, '|||', sentence);
				print(n, end='', file=sys.stderr)
				prev, prev2 = self.START
				context = self.START + [self._normalise(w[1]) for w in sentence] + self.END
				tags = [w[3] for w in sentence];
				for i, token in enumerate(sentence):
					word = token[1]
					guess = self.tagdict.get(word)
					if not guess:
						feats = self._get_features(i, word, context, prev, prev2)
						guess = self.model.predict(feats)
						self.model.update(tags[i], guess, feats)
					prev2 = prev
					prev = guess
					c += guess == tags[i]
					n += 1
				print('\r', end='', file=sys.stderr)
			random.shuffle(sentences)
			print()
			print("Iter {0}: {1}/{2}={3}".format(iter_, c, n, _pc(c, n)), file=sys.stderr)
		self.model.average_weights()
		# Pickle as a binary file
		if save_loc is not None:
			pickle.dump((self.model.weights, self.tagdict, self.classes),
						 open(save_loc, 'wb'), -1)
		return None

	def load(self, loc):
		'''Load a pickled model.'''
		try:
			w_td_c = pickle.load(open(loc, 'rb'))
		except IOError:
			print("Missing " +loc+" file.")
			sys.exit(-1)
		self.model.weights, self.tagdict, self.classes = w_td_c
		self.model.classes = self.classes
		return None

	def _normalise(self, word):
		'''Normalisation used in pre-processing.

		- All words are lower cased
		- Digits in the range 0000-2100 are represented as !YEAR;
		- Other digits are represented as !DIGITS

		:rtype: str
		'''
		if '-' in word and word[0] != '-':
			return '!HYPHEN'
		elif word.isdigit() and len(word) == 4:
			return '!YEAR'
		elif word[0].isdigit():
			return '!DIGITS'
		else:
			return word.lower()

	def _get_features(self, i, word: str, context, prev, prev2):
		'''Map tokens into a feature representation, implemented as a
		{hashable: float} dict. If the features change, a new model must be
		trained.
		'''
		def add(name, *args):
			features[' '.join((name,) + tuple(args))] += 1

		i += len(self.START)
		features = defaultdict(int)
		# It's useful to have a constant feature, which acts sort of like a prior
		add('bias')
		add('i suffix', word[-3:])
		add('i pref1', word[0])
		add('i-1 tag', prev)
		add('i-2 tag', prev2)
		add('i tag+i-2 tag', prev, prev2)
		add('i word', context[i])
		add('i-1 tag+i word', prev, context[i])
		add('i-1 word', context[i-1])
		add('i-1 suffix', context[i-1][-3:])
		add('i-2 word', context[i-2])
		add('i+1 word', context[i+1])
		add('i+1 suffix', context[i+1][-3:])
		add('i+2 word', context[i+2])

		add('i prefix', word[:3])
		add("i-1 pref1", context[i-1][-3:])
		add("i-1 prefix", context[i-1][:3])
		add("i+1 pref1", context[i+1][-3:])
		add("i+1 prefix", context[i +1][:3])
		add("i-2 pref1", context[i-2][-3:])
		add("i+1 prefix", context[i+2][:3])
		add("i+2 suffix", context[i+2][-3:])
		add("i+2 pref1", context[i+2][0])
		add("i+2 prefix", context[i+2][:3])

		add('upper register', str(int(word.isupper())))
		add('lower register', str(int(word.islower())))
		add('capitalized', str(int(word[0].isupper())))
		add('numeric', str(int(word.isnumeric())))
		add('alpha', str(int(word.isalpha())))

		add("length", str(len(word)))
		#print(word, '|||', features)
		return features

	def _make_tagdict(self, sentences):
		'''Make a tag dictionary for single-tag words.'''
		counts = defaultdict(lambda: defaultdict(int))
#		for words, tags in sentences:
		for sentence in sentences:
			for token in sentence:
				word = token[1]
				tag = token[3]
				counts[word][tag] += 1
				self.classes.add(tag)
		freq_thresh = 20
		ambiguity_thresh = 0.97
		for word, tag_freqs in counts.items():
			tag, mode = max(tag_freqs.items(), key=lambda item: item[1])
			n = sum(tag_freqs.values())
			# Don't add rare words to the tag dictionary
			# Only add quite unambiguous words
			if n >= freq_thresh and (float(mode) / n) >= ambiguity_thresh:
				self.tagdict[word] = tag

###############################################################################

def tagger(corpus_file, model_file):
	''' tag some text. 
	:param corpus_file is a file handle
	:param model_file is a saved model file
	'''
	t = PerceptronTagger(model_file)
	t.tag(corpus_file)

def trainer(corpus_file, model_file):
	''' train a model 
	:param corpus_file is a file handle
	:param model_file is a saved model file
	'''
	t = PerceptronTagger(model_file, load=False)
	sentences = [];
	for sent in corpus_file.read().split('\n\n'):
		sentence = []
		for token in sent.split('\n'):
			if token.strip() == '':
				continue
			if token[0] == '#':
				continue
			sentence.append(tuple(token.strip().split('\t')))
		sentences.append(sentence)

	t.train(sentences, save_loc=model_file, nr_iter=5)

if len(sys.argv) == 3 and sys.argv[1] == '-t':
	trainer(sys.stdin, sys.argv[2])	
elif len(sys.argv) == 2:
	tagger(sys.stdin, sys.argv[1])
else:
	print('tagger.py [-t] model.dat');
	sys.exit(-1)
