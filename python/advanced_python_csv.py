import pandas as pd

faculty = pd.read_csv('faculty.csv',header = 0)

#print faculty

emailList = []
for index, row in faculty.iterrows():
    #print index, row['email']
    emailList.append(row['email'])
    
print type(faculty.email)

'''domainList = []
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
    print domainListSet[i], domainListCount[i]'''
    
faculty.email.to_csv('emails.csv')