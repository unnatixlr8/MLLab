# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:09:49 2019

@author: CSE
"""
import csv
#! usr/bin/python
#list creation
hypo=['%','%','%','%','%','%']
with open('p1.csv') as csv_file:
    readcsv=csv.reader(csv_file,delimiter=',')
    print(readcsv)
    data=[]
    print("\n the given training examples are:")
    for row in readcsv:
        print(row)
        if row[len(row)-1].upper()=="YES":
            data.append(row)
print("\n the positive examples are:")
for x in data:
    print(x)
print("\n")
TotalExamples=len(data)
i=0
j=0
k=0
print("the step of the find s algorithm are\n",hypo)
list1=[]
p=0
d=len(data[p])-1
for j in range(d):
    list1.append(data[i][j])
hypo=list1
i=1
for i in range(TotalExamples):
    for k in range(d):
        if hypo[k]!=data[i][k]:
            hypo[k]='?'
            #k=k+1
        else:
            hypo[k]
    print(hypo)
#i=i+1
print("\n the maximally specific find s hypothesis for the given training examples is")
list1=[]
for i in range(d):
    list1.append(hypo[i])
print(list1)