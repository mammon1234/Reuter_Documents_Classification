import StringIO
import os,sys
import re,math
import ReadStopword
import nltk
from nltk.corpus import reuters
def Tfidftest(path_test,dict_traincate,dict_train,featuredict):
    paths="E:/Workspaces/NLP/reuters/stopwords"
    stopset=ReadStopword.ReadStopword(paths)
    wholedict={}
    docdict={}
    worddict={}
    docsum=0
    #caculate the frequency of the word
    for i in range(1,91):
        for k in dict_train[i]:
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
            docsum=docsum+1
#build the wholedict to store the frequency for all words in training dataset
            for wdict in tempworddict:
                if wdict in wholedict:
                    wholedict[wdict][str(h)]=tempworddict[wdict]
                else:
                    wholedict[wdict]={}
                    wholedict[wdict][str(h)]=tempworddict[wdict]
    #calculate the idf for each word
    for each in worddict:
        res=float(docsum)/float(worddict[each])
        worddict[each]=math.log(res,math.e)
    #Read the categories of test dataset
    try:
        file_object_resul=open(path_test)
    except IOError:
        print "The file don't exist,Please check!!"
        exit()
    Alllines_resul=file_object_resul.readlines()
    if os.path.exists("E:/Workspaces/NLP/TFIDF/cat"):
        os.remove("E:/Workspaces/NLP/TFIDF/cat")
    fw=open("E:/Workspaces/NLP/TFIDF/cat",'w')
    for eachline in Alllines_resul:
        p=0
        line=eachline.split(' ')
        title=line[0]
        h=str(title).replace('test/', '')
        fw.write(title)
        for part in line:
            if p>=1:
                testcat=str(part)
                testcat=testcat.replace('\n', '')
                fw.write(" "+str(dict_traincate[testcat]))
            p=p+1
        fw.write('\n')
        tem=0
        tempworddict={}
        #read the content of test dataset
        for word in reuters.words(title):
            if word in wholedict:
                if word.lower() in tempworddict:
                    x=tempworddict[word.lower()]
                    tempworddict[word.lower()]=x+1
                else:
                    tempworddict[word.lower()]=1
                tem=tem+1
        docdict[str(h)]=tem
#build the wholedict to store the frequency for all words in testing dataset
        for wdict in tempworddict:
            if wdict in wholedict:
                wholedict[wdict][str(h)]=tempworddict[wdict]
            else:
                wholedict[wdict]={}
                wholedict[wdict][str(h)]=tempworddict[wdict]
    fw.close()
    if os.path.exists("E:/Workspaces/NLP/TFIDF/test"):
        os.remove("E:/Workspaces/NLP/TFIDF/test")
    fw=open("E:/Workspaces/NLP/TFIDF/test",'w')
    for eachline in Alllines_resul:
        p=0
        line=eachline.split(' ')
        title=line[0]
        h=str(title).replace('test/', '')
        for part in line:
            if p==1:
                testcat=str(part)
                testcat=testcat.replace('\n', '')
                fw.write(str(dict_traincate[testcat])+" ")
            p=p+1
        cot=0
        for singleword in wholedict:
            cot=cot+1
            if h in wholedict[singleword]:
                #calculate the TF
                tf=float(wholedict[singleword][h])/float(docdict[h])
                tfidf=tf*worddict[singleword]
                fw.write(str(cot)+":"+str(tfidf)+" ")
        fw.writelines("\n")
    fw.close()
                

