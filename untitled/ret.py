# -*- coding: utf-8 -*-
import nltk
from nltk import tree
from nltk.corpus import treebank


text= open('rat.txt').read()
tokens = nltk.word_tokenize(text)

tagged = nltk.pos_tag(tokens)

tree = nltk.tree.Tree.fromstring(tagged)
def traverseTree(tree):
    print("tree:", tree)
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            traverseTree(subtree)
traverseTree(tree)