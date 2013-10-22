#!/usr/bin/env python
import mincemeat
from os import walk
mypath = "./hw3data"
data = []

for (dirpath, dirnames, filenames) in walk(mypath):
    for filename in filenames:
        with open(mypath + "/" + filename) as f:
            data = f.readlines()
        data.extend(data)

# The data source can be any dictionary-like object
source = dict(enumerate(data))

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
