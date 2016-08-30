import StringIO
import os,sys
import re
import ReadStopword
import nltk
from nltk.corpus import reuters
def compute_testcat(path_test,whole_dict,dictcat,dict_traincate,featuredict):
    paths="E:/Workspaces/NLP/reuters/stopwords"
    stopset=ReadStopword.ReadStopword(paths)
    try:
        file_object_resul=open(path_test)
    except IOError:
        print "The file don't exist,Please check!!"
        exit()
    Alllines_resul=file_object_resul.readlines()
    file_object_resul.close()
    # determine the path of the written file
    if os.path.exists("E:/Workspaces/NLP/NBresult"):
        os.remove("E:/Workspaces/NLP/NBresult")
    fw=open("E:/Workspaces/NLP/NBresult",'w')
    sumtr=0
    sumall=0
    dict_doc={}
    for eachline in Alllines_resul:
        line=eachline.split(' ')
        k=line[0]
        path_test="E:/Workspaces/NLP/reuters/"+str(k)
        maxvalue=0.0
        maxcat=''
        #get the probability of each class
        for i in range(1,91):
            dict_doc[i]=float(dictcat[i])
        testcatlist=[]
        p=0
        #get the standard result of test file
        for part in line:
            if p>=1:
                testcat=str(part)
                testcat=testcat.replace('\n', '')
                testcatlist.append(str(dict_traincate[testcat]))
            p=p+1
        #count the feature of each test doc.give 100 to each probabilty to avoid the extreme small result 
        for word in reuters.words(k):
            if word.lower() not in stopset and word.lower() in whole_dict:
                wordsingle_cat=whole_dict[word.lower()]
                for i in range(1,91):
                    if str(i) in whole_dict[word.lower()]:
                        dict_doc[i]=dict_doc[i]*float(whole_dict[word.lower()][str(i)])*100.0
                    else:
                        #for the feature that the word do not have ,give a small value of 0.002
                        dict_doc[i]=float(dict_doc[i])*100.0*0.002
        for i in range(1,91):
            if maxvalue<float(dict_doc[i]):
                maxvalue=float(dict_doc[i])
                maxcat=str(i)
        fw.writelines(str(k)+" "+str(maxcat)+" "+str(maxvalue)+"\n")
        if str(maxcat) in testcatlist:
            sumtr=sumtr+1
        sumall=sumall+1
    fw.close()
    return float(sumtr)/float(sumall)

