#!/usr/bin/env python
import mincemeat
import glob

filePath = './hw3data/*'
text_files = glob.glob(filePath)

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))
        for file_name in text_files)


def mapfn(key, value):
    from stopwords import allStopWords
    for line in value.splitlines():
        word=line.split(':::')  
        authors=word[1].split('::')  
        title=word[2]
        for author in authors:  
            for term in title.split():  
                if term not in allStopWords:  
                    if term.isalnum():  
                        yield author,term.lower()  
                    elif len(term)>1:  
                        temp=''  
                        for ichar in term:  
                            if ichar.isalpha() or ichar.isdigit():  
                                temp+=ichar  
                            elif ichar=='-':  
                                temp+=' '  
                        yield author,temp.lower()  
        
def reducefn(k, vs):
    terms = vs
    result={}
    for term in terms:
        if term in result:
            result[term] += 1
        else:
            result[term] = 1
    return result

s = mincemeat.Server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="titan")
print results
