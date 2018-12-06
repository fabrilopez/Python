# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:42:32 2018

@author: Fabricio

Lista de listas

"""
# 1. Let us define a simple list with some positive and negative numbers.
a = [1,2,-1,-2,3,4,-3,-4]
# 2. Now let us write our list comprehension.
# pow() a power function takes two input and
# its output is the first variable raised to the power of the second.
b = [pow(x,2) for x in a if x < 0]
# 3. Finally let us see the output, i.e. the newly created list b.
print (b)


