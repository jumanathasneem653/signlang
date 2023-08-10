# coding: utf-8

# In[ ]:
import os

import tensorflow as tf

import keras
from keras.engine.saving import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers import Dense, Activation, Dropout, Flatten

from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np

#------------------------------
# sess = tf.Session()
# keras.backend.set_session(sess)
#------------------------------
#variables
num_classes =35
batch_size = 40
epochs = 15

import pywt.data

import  cv2
import numpy as np
from skimage import io
from skimage.feature import greycomatrix, greycoprops

def glcm_feat(path):
    x = io.imread(path)
    # print(x.shape)
    if(len(x.shape)==3):
        x= x[:, : ,2]
    nir = x[:, : ]
    glcm = greycomatrix(x, [1], [np.pi/2], levels=256, normed=True, symmetric=True)
    # print(glcm)
    li=[];
    # contrast’, ‘dissimilarity’, ‘homogeneity’, ‘energy’, ‘correlation’, ‘ASM’},
    li.append(greycoprops(glcm,prop='contrast')[0][0])
    li.append(greycoprops(glcm,prop='dissimilarity')[0][0])
    li.append(greycoprops(glcm,prop='homogeneity')[0][0])
    li.append(greycoprops(glcm,prop='energy')[0][0])
    li.append(greycoprops(glcm,prop='correlation')[0][0])
    li.append(greycoprops(glcm,prop='ASM')[0][0])
    return li
#------------------------------

import os, cv2, keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.engine.saving import load_model
# manipulate with numpy,load with panda
import numpy as np
# import pandas as pd

# data visualization
import cv2
import matplotlib
import matplotlib.pyplot as plt
# import seaborn as sns

# get_ipython().run_line_magic('matplotlib', 'inline')


# Data Import
def read_dataset(path):
    data_list = []
    label_list = []
    my_list = os.listdir(r'E:\django\signlanguage\static\data')
    i=-1
    ii=0
    for pa in my_list:

        print(pa,"==================")
        i=i+1
        for root, dirs, files in os.walk(r'E:\django\signlanguage\static\data\\' + pa):

         for f in files:


             file_path = os.path.join(r'E:\django\signlanguage\static\data\\'+pa, f)


             res=glcm_feat(file_path)
             data_list.append(res)
             # label = dirPath.split('/')[-1]
             label = i
             label_list.append(label)
             # label_list.remove("./training")
             ii+=1
             if ii>=1000:
                ii=0
                break
    return data_list,label_list

# #
from sklearn.model_selection import train_test_split
# load dataset
x_dataset, y_dataset = read_dataset(r"E:\django\signlanguage\static\data")
X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.2, random_state=0)

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(X_train, y_train)

# making predictions on the testing set
y_pred = gnb.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics

print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred) * 100)