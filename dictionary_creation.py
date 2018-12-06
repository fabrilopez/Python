'''
dictionary creation
'''
#1 load a variable with sentences
sentence='Pablito clavo un clavito que clavito clavo palblito'

'''
Peter Piper picked a peck of pickled peppers A peck of pickledpeppers\
Peter Piper picked If Peter Piper picked a peck of pickled \
peppers Wheres the peck of pickled peppers Peter Piper picked
'''

#2 Initianilize a dictionary objetc
word_dict={}

#3 Perform the word count
for word in sentence.split():
    if word not in word_dict:
        word_dict[word]=1   #si la palabra no está en el diccionario, la agrega y le pone 1
    else:
        word_dict[word]+=1  #si la palabra está en el diccionario le suma 1 al valor

#4 print the outputprint (word_dict)
print (word_dict)
for key, value in word_dict.items():
    print(key,value)
        