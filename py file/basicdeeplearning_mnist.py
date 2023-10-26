# -*- coding: utf-8 -*-
"""BasicDeepLearning_Mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1izHV9u2GB9nR_qiuyy78SDtOLeS8tJjq
"""

import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train.shape
#입력 모양새 : (60000, 28, 28) --> 입력 (28, 28) 이미지 60000장

y_train.shape

set(y_train)
#유니크한 인티저는 몇 개인지

x_train = x_train.reshape(60000, (28*28))
x_train.shape
# Dense layer : 1차원 데이터만 받을 수 있음
# 이미지를 1차원 데이터로 바꿔야함

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_train.shape

from tensorflow import keras
from tensorflow.keras import layers
model = keras.Sequential()
model.add( layers.Dense(512, activation='relu', input_shape=(28*28,)))
model.add( layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs = 5)