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
datasource = dict(enumerate(data))

def mapfn(k, v):
    for w in v.split():
        yield w, 1

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="titan")
print results
