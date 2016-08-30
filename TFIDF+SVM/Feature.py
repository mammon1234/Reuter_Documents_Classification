import StringIO
import os,sys
import re,math
import ReadStopword
import nltk
from nltk.corpus import reuters
def cumulate(dict_train):
    #Read the stopwords
    paths="E:/Workspaces/NLP/reuters/stopwords"
    stopset=ReadStopword.ReadStopword(paths)
    wholedict={}
    worddict={}
    docsum=0
    classdict={}
    #caculate the frequency of the word in each category
    for i in range(1,91):
        p=0
        for k in dict_train[i]:
            tempworddict={}
            path_train="E:/Workspaces/NLP/reuters/"+str(k)
            h=str(k).replace('training/', '')
            for word in reuters.words(k):
                if word.isalpha() and word not in stopset:
                    if word.lower() not in tempworddict:
                        tempworddict[word.lower()]=1
                        if word.lower() in wholedict:
                            if i in wholedict[word.lower()]:
                                x=wholedict[word.lower()][i]
                                wholedict[word.lower()][i]=x+1
                            else:
                                wholedict[word.lower()][i]=1
                        else:
                            wholedict[word.lower()]={}
                            wholedict[word.lower()][i]=1
            p=p+1
            docsum=docsum+1
        #store the num of doc in each categories
        classdict[i]=p
    entropy=0.0
    #calculate the entropy of whole datasets
    for cat in classdict:
        re=float(classdict[cat])/float(docsum)
        tem=re*math.log(re,math.e)
        entropy=entropy+tem
    #calculate the entropy of each word
    for word in wholedict:
        wsum=0
        w_entropy=0
        #calculate the num of doc which has certain word
        for cat in wholedict[word]:
            wsum=wsum+wholedict[word][cat]
        w_nosum=docsum-wsum
        for i in range(1,91):
            if i in wholedict[word]:
                wtem1=float(wholedict[word][i])/float(wsum)+0.01
                wtem2=float(wholedict[word][i])/float(docsum)
                w_entropy=w_entropy+wtem2*math.log(wtem1,math.e)
                if classdict[i]>wholedict[word][i]:
                    w_no=classdict[i]-wholedict[word][i]
                    wtem1=float(w_no)/float(w_nosum)+0.01
                    wtem2=float(w_no)/float(docsum)
                    w_entropy=w_entropy+wtem2*math.log(wtem1,math.e)
            else:
                wtem1=float(classdict[i])/float(w_nosum)+0.01
                wtem2=float(classdict[i])/float(docsum)
                w_entropy=w_entropy+wtem2*math.log(wtem1,math.e)
        worddict[word]=w_entropy-entropy
    #calculate the IG of each word and rank them
    worddict2=sorted(worddict.iteritems(),key=lambda asd:asd[1],reverse = True)
    #Choose 20000 big value of entropy as feature
    Feature=20000
    featuredict={}
    #if os.path.exists("E:/Workspaces/NLP/TFIDF/feature"):
    #    os.remove("E:/Workspaces/NLP/TFIDF/feature")
    #fw=open("E:/Workspaces/NLP/TFIDF/feature",'w')
    for word in worddict2:
        if Feature>=0:
            featuredict[str(word[0])]=1
        Feature=Feature-1
        #fw.writelines(str(word[0])+" : "+str(word[1])+'\n')
    #fw.close()
    return featuredict
