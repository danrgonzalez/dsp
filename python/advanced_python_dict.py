import pandas as pd

faculty = pd.read_csv('faculty.csv',header = 0)

#print faculty

faculty_dict = {}
for index, row in faculty.iterrows():
    faculty_dict[row['name']] = [row['degree'],row['title'], row['email']]

#print faculty_dict


