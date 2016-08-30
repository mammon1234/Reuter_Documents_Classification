import StringIO
import os,sys
import re
def ReadStopword(objpath):
    try:
        file_object=open(objpath)
    except IOError:
        print "The file don't exist,Please check!!"
        exit()
    Alllines=file_object.readlines()
    stopset=set()
    for eachline in Alllines:
        eachline=eachline.replace('\n','')
        stopset.add(str(eachline))
    file_object.close()
    return stopset
