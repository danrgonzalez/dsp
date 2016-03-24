import pandas as pd

faculty = pd.read_csv('faculty.csv',header = 0)

#print faculty

'''emailList = []
for index, row in faculty.iterrows():
    #print index, row['email']
    emailList.append(row['email'])
    
#print type(faculty.email)'''
    
faculty.email.to_csv('emails.csv', index=False)