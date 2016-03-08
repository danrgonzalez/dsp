# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:16:52 2016

@author: dgonzalez
"""

#Section 5a - Datetime
from datetime import datetime

date_start = '01-02-2013'    
date_stop = '07-28-2015'

d1 = datetime.strptime(date_start, '%m-%d-%Y')
d2 = datetime.strptime(date_stop, '%m-%d-%Y')

diff = d2 - d1
print diff

date_start = '12312013'  
date_stop = '05282015'

d1 = datetime.strptime(date_start, '%m%d%Y')
d2 = datetime.strptime(date_stop, '%m%d%Y')

diff = d2 - d1
print diff

date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'

d1 = datetime.strptime(date_start, '%d-%b-%Y')
d2 = datetime.strptime(date_stop, '%d-%b-%Y')

diff = d2 - d1
print diff


#Section 5a - Strings
def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    
    if count > 9:
        print 'many'
    elif count < 10:
        print 'Number of donuts: ', count
    else:
        raise NotImplementedError

donuts(8)

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    
    c = list(s)
    l = len(c)
    if (l < 2):
        print ""
    else:
        newc = c[0:2] + c[l-2:l]
        newS = ''.join(newc)
        print newS
    
    #raise NotImplementedError

both_ends('Daniel')


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """

    c = list(s)
    first = c[0]
    
    for i in range(1,len(c)):
        if c[i] == first:
            c[i] = '*'
    
    print ''.join(c)
    
    #raise NotImplementedError

fix_start('babble')


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
        
    alist = list(a)
    blist = list(b)
    
    #first 2 letters
    a2 = alist[0:2]
    b2 = blist[0:2]
    
    #lengths of strings
    la = len(alist)
    lb = len(blist)
    
    new1 = b2+alist[2:la]
    new2 = a2+blist[2:lb]
    
    f=''.join(new1)
    l=''.join(new2)
    print f+" "+l
    
    #raise NotImplementedError

mix_up('gnash', 'sport')

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    l = len(s)
    if (len(s) > 2):
        if (s[l-3:l] == 'ing'):
            ly = s[0:l-3]+'ly'
            print ly
        else:
            ing = s+'ing'
            print ing
    else:
        print s
    
    #raise NotImplementedError

verbing('swim')

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    
    if(s.index('bad')>s.index('not')):
        print s[0:s.index('not')]+'good'
    else:
        print s
    
    #raise NotImplementedError

not_bad('This movie is not so bad')

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    
    if(len(a)%2 == 0):
        a_front = a[0:len(a)/2]
        a_back = a[len(a)/2:len(a)]
    else:
        a_front = a[0:(len(a)/2)+1]
        a_back = a[(len(a)/2)+1:len(a)]
        
    if(len(b)%2 == 0):
        b_front = b[0:len(b)/2]
        b_back = b[len(b)/2:len(b)]
    else:
        b_front = b[0:(len(b)/2)+1]
        b_back = b[(len(b)/2)+1:len(b)]
    
    print a_front + b_front + a_back + b_back
    
    #raise NotImplementedError
    
front_back('Kitten','Donut')


#Section 5a - Lists

def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.
    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    
    count = 0
    for s in words:
        if (len(s) > 2 and s[0] == s[len(s)-1]):
            count += 1
            
    print count
    
    #raise NotImplementedError

match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    
    xWords = []
    for word in words:
        if(word[0] == 'x'):
            xWords.append(word)
    
    noXwords = []
    for i in range(0,len(words)):
        temp = words[i]
        if(temp[0] != 'x'):
            noXwords.append(temp)

    sortednoxWords = sorted(noXwords)
    print xWords+sortednoxWords
    
    #raise NotImplementedError


front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    
    print sorted(tuples, key=lambda tup: tup[len(tup)-1])

    
    #raise NotImplementedError

sort_last([(1, 3), (3, 2), (2, 1)])
sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    
    index = []
    for i in range(0,len(nums)-1):
        #print nums[i], nums[i+1]
        if (nums[i] == nums[i+1]):
            index.append(i+1)
     
    for j in range(len(nums)-1,-1,-1):
        for k in index:
            if (j == k):
                del nums[j]
    
    print nums
    #raise NotImplementedError

remove_adjacent([1, 2, 2, 3])
remove_adjacent([2, 2, 3, 3, 3])
remove_adjacent([3, 2, 3, 3, 3])

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.
    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    
    new = sorted(list1+list2)

    print new    
    
    #raise NotImplementedError
    
linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])


#Section 5a - Parsing

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






















