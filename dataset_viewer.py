# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import matplotlib.pyplot as plt
from keras.datasets import cifar10

# this creates a training set and test set
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
count = 0
while count < 10:
    count += 1
    image=x_train[count]
    imgplot = plt.imshow(image)
    plt.show()
    print(y_train[count])
    

