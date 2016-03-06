#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import csv

parsed_data = []

def read_data(data):
   with open(data, 'rb') as csvfile:
       reader = csv.reader(csvfile)
       for row in reader:
          print row
          parsed_data.append(row)

def get_min_score_difference(parsed_data):
    #print parsed_data[0][5], parsed_data[0][6]
    
    diff = []
    for i in range(1,len(parsed_data)):
        #print int(parsed_data[i][5]), int(parsed_data[i][6])
        d = int(parsed_data[i][5]) - int(parsed_data[i][6])
        #print d
        diff.append(d)        
        #print diff
    
    print min(diff)
    

def get_team(parsed_data):
    diff = []
    
    for i in range(1,len(parsed_data)):
        #print int(parsed_data[i][5]), int(parsed_data[i][6])
        d = int(parsed_data[i][5]) - int(parsed_data[i][6])
        #print d
        diff.append(d)        
        #print diff
    
    print diff.index(min(diff))+1
    print parsed_data[diff.index(min(diff))+1][0]
    


read_data('football.csv')

get_min_score_difference(parsed_data)

get_team(parsed_data)
