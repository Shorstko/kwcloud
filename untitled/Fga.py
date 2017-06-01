# -*- coding: utf-8 -*-
from nltk.tree import Tree
import nltk
from nltk import tree
from nltk.corpus import treebank

text= open('rat.txt').read()
tokens = nltk.word_tokenize(text)

tagged = nltk.pos_tag(tokens)

tree.__all__pretty_print(unicodelines=True, nodedist=4)

#t = treebank.parsed_sents()[0]
#t.draw()
#print(tagged)
