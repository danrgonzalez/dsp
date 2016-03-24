import pandas as pd
import collections

faculty = pd.read_csv('faculty.csv',header = 0)

nameList = []
for index, row in faculty.iterrows():
    nameList.append(row['name'])

splitNames = []
for i in range(0,len(nameList)): 
    splitNames.append(nameList[i].split())

firstNames = []
for i in splitNames:
    firstNames.append(i[0])

lastNames = []
for i in splitNames:
    lastNames.append(i[len(i)-1])

lastNamesUnique = sorted(set(lastNames))


faculty_dict = {}
for index, row in faculty.iterrows():
    faculty_dict[row['name']] = [row['degree'],row['title'], row['email'], lastNames[index]]

byLastName = []
for i in range(0,len(lastNamesUnique)):
    temp = []
    for key in faculty_dict:
        if (lastNamesUnique[i] == faculty_dict[key][3]):
            temp.append([faculty_dict[key][0],faculty_dict[key][1],faculty_dict[key][2]])
    byLastName.append(temp)
    
byLastName_dict = {}
for i in range(0,len(byLastName)):
    byLastName_dict[lastNamesUnique[i]] = byLastName[i]

print '######'
for i in range(0,3):
    print byLastName_dict.items()[i]
    
faculty_dict2 = {}
for index, row in faculty.iterrows():
    faculty_dict2[(firstNames[index], lastNames[index])] = [row['degree'],row['title'], row['email']]

print '#######'  
for i in range(0,3):
    print faculty_dict2.items()[i]

print '#######'    
faculty_dict2 = collections.OrderedDict(sorted(faculty_dict2.items(), key=lambda x: x[0][1]))

for i in range(0,3):
    print faculty_dict2.items()[i]




    
    
    
    
    
    
    
    