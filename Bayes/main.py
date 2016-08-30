import StringIO
import os,sys
import Readcat,ReadStopword,NBtrain,NBmae,Feature
import nltk
from nltk.corpus import reuters
path_train="E:/Workspaces/NLP/reuters/train.txt"
#Read the class of training data and the path of each doc
(dict_train,dict_traincate,dict_traincate_anti)=Readcat.Readcat(path_train)
#dict_train represents the path of each doc of classes;
#dict_traincate,dict_traincate_anti represent the class and its number
(featuredict)=Feature.cumulate(dict_train)
#caculate the probability of each class and each word
(whole_dict,dictcat)=NBtrain.cumulate(dict_train,featuredict)
path_test="E:/Workspaces/NLP/reuters/test.txt"
#caculate the accuracy 
MAE=NBmae.compute_testcat(path_test,whole_dict,dictcat,dict_traincate,featuredict)
print MAE

