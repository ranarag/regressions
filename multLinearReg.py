import sys
import itertools
import numpy as np

################################################################
## Calculate the theta values
################################################################
def calculate_theta_values(X, Y):
    Theta = (np.linalg.inv(X.T.dot(X)).dot(X.T)).dot(Y)
    return Theta

################################################################
## Calculate test results
################################################################
def calcResults(Theta, testCase):
    result = Theta[0, 0]
    for i in range(len(testCase)):
        result += Theta[i+1, 0]* testCase[i]
    return result


################################################################
## Populate the X and Y matrices
################################################################
lx = []
v = sys.stdin.readline().strip().split(' ')
v = map(int, v)
ly = []
for i in xrange(0,v[1]):
    x = []
    vals = sys.stdin.readline().strip().split(' ')
    vals = map(float, vals)
    ly.append([vals[-1]])
    x.append(1.0)
    for i in range(len(vals)-1):
            x.append(vals[i])
    lx.append(x)
Y = np.array(ly)
X = np.array(lx)
Theta = calculate_theta_values(X, Y)

################################################################
## Read in test cases
################################################################
t = int(sys.stdin.readline())
for i in xrange(0,t):
    tmp = []
    vals = sys.stdin.readline().strip().split(' ')
    for j,val in enumerate(vals):
        tmp.append(float(val))
    print str(calcResults(Theta, tmp))

