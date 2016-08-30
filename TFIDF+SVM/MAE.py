import StringIO
import os,sys
import re,math
import ReadStopword
import nltk
from nltk.corpus import reuters
#read the prediction from SVM
path="E:\Workspaces\NLP\TFIDF\liblinear\output"
try:
    file_object_resul=open(path)
except IOError:
    print '1'
    print "The file don't exist,Please check!!"
    exit()
k=[]
Alllines_resul=file_object_resul.readlines()
i=0
for eachline in Alllines_resul:
    eachline=eachline.replace('\n', '')
    k.append(eachline)
#read the standard answers
path2="E:\Workspaces\NLP\TFIDF\liblinear\cat"
file_object_result=open(path2)
Alllines_resul=file_object_result.readlines()
i=0
right=0
sumall=0
for eachline in Alllines_resul:
    line=eachline.split(' ')
    p=0
    testcatlist=[]
    for part in line:
        if p>=1:
            testcat=str(part)
            testcat=testcat.replace('\n', '')
            testcatlist.append(testcat)
        p=p+1
    if k[i] in testcatlist:
        right=right+1
    sumall=sumall+1
    i=i+1
#calculate the MAE
print float(right)/sumall
