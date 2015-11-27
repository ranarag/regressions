import sys
import itertools
import numpy as np

################################################################
## Definition of h theta
################################################################
def h_theta(Theta,x):
  value = 0.0
  for i,theta in enumerate(Theta):
    #value += Theta[i]*x_pow(x,po)
    value += theta*x[i]
  return value


def x_pow(x,power):
  val = 1.0
  for i,p in enumerate(power):
    val*=pow(x[i],p)
  return val

################################################################
## Calculate the theta values
################################################################
def calculate_theta_values(Theta,X,thres,alpha,pows):
  while True:
    tmp_Theta = Theta - np.array([alpha*(1.0/len(X))*np.sum((X.dot(Theta)-Y.T)*X,axis=0)]).T
    if np.max(np.abs(Theta-tmp_Theta)) < thres:
      return tmp_Theta
    Theta = tmp_Theta

def generate_new_X(X,powers):
  new_X = []
  for x in X:
    tmp = []
    for pows in powers:
      tmp.append(x_pow(x,pows))
    new_X.append(tmp)
  return new_X

#################################################################
## Initlise variables
#################################################################
tmp = sys.stdin.readline()
vals = tmp.strip().split(' ')
f,m = int(vals[0]),int(vals[1])
X = []
Y = []
alpha = 0.1
thres = 0.001
Theta = [0.0]*(f+1)

################################################################
## Populate the X and Y matrices
################################################################
for i in xrange(0,m):
  x = []
  vals = sys.stdin.readline().strip().split(' ')
  Y.append(float(vals[-1]))
  for j,val in enumerate(vals[:-1]):
    x.append(float(val))
  X.append(x)

################################################################
## Read in test cases
################################################################
test_cases = []
t = int(sys.stdin.readline())
for i in xrange(0,t):
  tmp = []
  vals = sys.stdin.readline().strip().split(' ')
  for j,val in enumerate(vals):
    tmp.append(float(val))
  test_cases.append(tmp)

powers = [x for x in itertools.product([0,1,2,3],repeat=f) if sum(x) < 4] # <======== max degree of polynomial is taken to be 4 
X = np.array(generate_new_X(X,powers))
Theta = np.array([[0.0]]*len(powers))
Y = np.array([Y])
Theta = calculate_theta_values(Theta,X,thres,alpha,powers)
test_cases = np.array(generate_new_X(test_cases,powers))
thres
ans = test_cases.dot(Theta)
for a in ans:
  print a[0],
