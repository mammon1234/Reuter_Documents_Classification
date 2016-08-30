import StringIO
import os,sys
import re
def Readcat(objpath):
    try:
        file_object_resul=open(objpath)
    except IOError:
        print "The file don't exist,Please check!!"
        exit()
    Alllines_resul=file_object_resul.readlines()
    dict_train={}
    dict_cate={}
    dict_cate_anti={}
    cate_num=1
    for eachline in Alllines_resul:
        line=eachline.split(' ')
        i=0
        train_name=line[0]
        for part in line:
            if i>=1:
                cat=str(part)
                cat=cat.replace('\n', '')
                if cat in dict_cate:
                    txt_cat=dict_cate[cat]
                else:
                    dict_cate[cat]=cate_num
                    dict_cate_anti[cate_num]=cat
                    txt_cat=cate_num
                    cate_num=cate_num+1
                dict_train.setdefault(txt_cat,[]).append(train_name)
            i=i+1
    file_object_resul.close()
    return (dict_train,dict_cate,dict_cate_anti)
