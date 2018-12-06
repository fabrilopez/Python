# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:09:53 2018

@author: Fabricio

dict_dict

We will create the user_movie_rating dictionary using an anonymous 
function to demonstrate the concept of a dictionary of dictionaries.
We will fill it with data to show the effective use of a 
dictionary of dictionaries:

"""

from collections import defaultdict
user_movie_rating = defaultdict(lambda :defaultdict(int))
# Initialize ratings for Alice
user_movie_rating["Alice"]["LOR1"] = 4
user_movie_rating["Alice"]["LOR2"] = 5
user_movie_rating["Alice"]["LOR3"] = 3
user_movie_rating["Alice"]["SW1"] = 5
user_movie_rating["Alice"]["SW2"] = 3
print (user_movie_rating)