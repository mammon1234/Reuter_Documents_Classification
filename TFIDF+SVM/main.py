import StringIO
import os,sys
import Readcat,ReadStopword,TFtrain,MTFtrain,Tfidftest,Feature
import nltk
from nltk.corpus import reuters
path_train="E:/Workspaces/NLP/reuters/train.txt"
#Read the class of training data and the path of each doc
(dict_train,dict_traincate,dict_traincate_anti)=Readcat.Readcat(path_train)
#calulate the information gain and select feature
(featuredict)=Feature.cumulate(dict_train)
#1.TFIDF vector generate for train dataset
(worddict1)=TFtrain.cumulate(dict_train,featuredict)
#2.M_TFIDF vector generate for train dataset
#(worddict2)=MTFtrain.cumulate(dict_train,featuredict)
#3.1
#path_test="E:/Workspaces/NLP/reuters/test.txt"
#3.2.TFIDF vector genrate for test dataset
#Tfidftest.Tfidftest(path_test,dict_traincate,dict_train,featuredict)


