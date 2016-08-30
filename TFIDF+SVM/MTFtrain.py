import StringIO
import os,sys
import re,math
import ReadStopword
import nltk
from nltk.corpus import reuters
def cumulate(dict_train,featuredict):
    paths="E:/Workspaces/NLP/reuters/stopwords"
    stopset=ReadStopword.ReadStopword(paths)
    wholedict={}
    docdict={}
    worddict={}
    worddict2={}
    docsum=0
    #caculate the frequency of the word
    for i in range(1,91):
        c=0
        for k in dict_train[i]:
            p=0
            tempworddict={}
            path_train="E:/Workspaces/NLP/reuters/"+str(k)
            h=str(k).replace('training/', '')
            for word in reuters.words(k):
                if word in featuredict:
                    if word.lower() in tempworddict:
                        x=tempworddict[word.lower()]
                        tempworddict[word.lower()]=x+1
                    else:
                        tempworddict[word.lower()]=1
                        if word.lower() in worddict:
                            x=worddict[word.lower()]
                            worddict[word.lower()]=x+1
                        else:
                            worddict[word.lower()]=1
                        #store the num of doc of certain word in categories
                        if word.lower() in worddict2:
                            if i in worddict2[word.lower()]:
                                x=worddict2[word.lower()][i]
                                worddict2[word.lower()][i]=x+1
                            else:
                                worddict2[word.lower()][i]=1
                        else:
                            worddict2[word.lower()]={}
                            worddict2[word.lower()][i]=1
                    p=p+1
                #store the num of words for all docs
                docdict[str(h)]=p
                docsum=docsum+1
                #build the wholedict to store the frequency for all words
                for wdict in tempworddict:
                    if wdict in wholedict:
                        wholedict[wdict][str(h)]=tempworddict[wdict]
                    else:
                        wholedict[wdict]={}
                        wholedict[wdict][str(h)]=tempworddict[wdict]
    # store a part of idf
    for each in worddict:
        res=float(docsum)/float(worddict[each])
        worddict[each]=res
    print "train all"
    if os.path.exists("E:/Workspaces/NLP/TFIDF/Mtrain"):
        os.remove("E:/Workspaces/NLP/TFIDF/Mtrain")
    fw=open("E:/Workspaces/NLP/TFIDF/Mtrain",'w')
    for i in range(1,91):
        for k in dict_train[i]:
            cot=0
            h=str(k).replace('training/', '')
            fw.write(str(i)) 
            for singleword in wholedict:
                cot=cot+1
                if h in wholedict[singleword]:
                    #calculate tf
                    tf=float(wholedict[singleword][h])/float(docdict[h])
                    #calculate new idf
                    te=(worddict2[singleword][i]+0.01)*float(worddict[singleword])
                    idf=math.log(te,math.e)
                    tfidf=tf*idf
                    fw.write(" "+str(cot)+":"+str(tfidf))
            fw.writelines("\n")
    fw.close()
    return worddict
