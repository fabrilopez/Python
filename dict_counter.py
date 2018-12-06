# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:00:01 2018

@author: Fabricio
"""

'''
dictionary creation whith counter json
'''

from collections import Counter

sentence='Pablito clavo un clavito que clavito clavo palblito'

'''
Peter Piper picked a peck of pickled peppers A peck of pickledpeppers\
Peter Piper picked If Peter Piper picked a peck of pickled \
peppers Wheres the peck of pickled peppers Peter Piper picked
'''

words=sentence.split()
word_count=Counter(words)
word_dict={}
print(word_count['Pablito'])
print(word_dict)
