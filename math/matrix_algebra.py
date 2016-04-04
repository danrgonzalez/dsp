# Matrix Algebra

import numpy as np
from numpy import linalg as LA

A = np.matrix([[1, 2, 3], [2, 7, 4]])

B = np.matrix([[1, -1],[0, 1]])

C = np.matrix([[5,-1],[9,1],[6,0]])

D = np.matrix([[3,-2,-1],[1,2,3]])

u = np.matrix([6,2,-3,5])

v = np.matrix([3,5,-1,4])

w = np.matrix([[1],[8],[0],[5]])

print A.shape
print B.shape
print C.shape
print D.shape
print u.shape
print w.shape

print u+v
print u-v
print 6*u
print u.dot(v.T)
print LA.norm(u)

#print A+C
print A-C.T
print C.T+3*D
print B*A
#print B*A.T

print C*B
print B^4
print A*A.T
print D.T*D

#Answers
#1.1 (2, 3)
#1.2 (2, 2)
#1.3 (3, 2)
#1.4 (2, 3)
#1.5 (1, 4)
#1.6 (4, 1)
#2.1 [[ 9  7 -4  9]]
#2.2 [[ 3 -3 -2  1]]
#2.3 [[ 36  12 -18  30]]
#2.4 [[51]]
#2.5 [[74]]
#3.1 Not dedined

#3.2 [[-4 -7 -3]
#### [ 3  6  4]]

#3.3 [[14  3  3]
#### [ 2  7  9]]

#3.4 [[-1 -5 -1]
#### [ 2  7  4]]

#3.5 Not Defined
