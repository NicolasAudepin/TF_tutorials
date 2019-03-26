from __future__ import absolute_import, division, print_function
import sys
print(sys.version)


import tensorflow as tf
import tensorflow.keras as keras

import numpy as np 
import matplotlib as plt

print(tf.__version__)

"""dataset = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = dataset.load_data()
"""
print(len(train_images))
print(len(train_labels))
print(len(test_images))
print(len(test_labels))


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
