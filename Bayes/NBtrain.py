import StringIO
import os,sys
import re
import ReadStopword
import nltk
from nltk.corpus import reuters
def cumulate(dict_train,featuredict):
    paths="E:/Workspaces/NLP/reuters/stopwords"
    stopset=ReadStopword.ReadStopword(paths)
    worddict={}
    wholedict={}
    dictcat={}
    p=0
    sumwords=0
    sumsingle_word=0
    #caculate the frequency of the word
    for i in range(1,91):
        for k in dict_train[i]:
            path_train="E:/Workspaces/NLP/reuters/"+str(k)
            for word in reuters.words(k):
                if word.isalpha() and word not in stopset:
                #if word.lower() in featuredict:
                    if word.lower() in worddict:
                        k=worddict[word.lower()]
                        worddict[word.lower()]=k+1
                    else:
                        worddict[word.lower()]=1
                    p=p+1
                    sumwords=sumwords+1
        for wdict in worddict:
            if wdict in wholedict:
                wholedict[wdict][str(i)]=str(worddict[wdict])
            else:
                wholedict[wdict]={}
                wholedict[wdict][str(i)]=str(worddict[wdict])
        worddict={}
        dictcat[i]=p
        p=0
    #caculate the probability of the class
    for i in dictcat:
        dictcat[i]=float(dictcat[i])/float(sumwords)
    #caculate the probability of the word    
    for word in wholedict:
        for wordcat in wholedict[word]:
            sumsingle_word=sumsingle_word+float(wholedict[word][str(wordcat)])
        for wordcat in wholedict[word]:
            wholedict[word][wordcat]=float(wholedict[word][str(wordcat)])/sumsingle_word
        sumsingle_word=0
    return wholedict,dictcat
