import csv
import pandas as pd
import re


'''parsed_data = []

def read_data(data):
   with open(data, 'rb') as csvfile:
       reader = csv.reader(csvfile)
       for row in reader:
          print row
          parsed_data.append(row)
          
#read_data('faculty.csv')'''

faculty = pd.read_csv('faculty.csv',header = 0)

print faculty
#print faculty.head()

#degrees = faculty.degree

degreeList = []
for index, row in faculty.iterrows():
    #print index, row['degree']
    degreeList.append(row['degree'])

udegreeList = set(degreeList)

#print degreeList

splits = []
for i in udegreeList:
    #print re.sub("[^\w]", " ",  i).split()
    splits.extend(i.split())

uniqueDegrees = sorted(set(splits))

#print uniqueDegrees

splits = []
for i in degreeList:
    #print re.sub("[^\w]", " ",  i).split()
    splits.extend(i.split())

allDegrees = splits

count = [0]*len(uniqueDegrees)
for i in range(0,len(uniqueDegrees)):
    for j in allDegrees:
        if (uniqueDegrees[i] == j):
            count[i] += 1

for i in range(0,len(uniqueDegrees)):
    print uniqueDegrees[i], count[i]




titleList = []
for index, row in faculty.iterrows():
    #print index, row['title']
    titleList.append(row['title'])

titleListSet = sorted(set(titleList))

titleCount = [0]*len(titleListSet)

for i in range(0,len(titleListSet)):
    for j in titleList:
        if (titleListSet[i] == j):
            titleCount[i] += 1

for i in range(0,len(titleListSet)):
    print titleListSet[i], titleCount[i]




emailList = []
for index, row in faculty.iterrows():
    #print index, row['email']
    emailList.append(row['email'])

domainList = []
for i in emailList:
    for c in range(0,len(i)):
        if(i[c] == '@'):
            domainList.append(i[c+1:])
            
domainListSet = sorted(set(domainList))

domainListCount = [0]*len(domainListSet)
for i in range(0,len(domainListSet)):
    for j in domainList:
        if(domainListSet[i] == j):
            domainListCount[i] += 1
            
for i in range(0,len(domainListSet)):
    print domainListSet[i], domainListCount[i]
            



