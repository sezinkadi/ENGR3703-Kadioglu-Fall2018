import math
def f(x):
    return 8-4.5*(x-math.sin(x))
a=2
b=3
tol=0.001     #tolerance
imax=50       #maximum number of iterations
Xns=(a+b)/2

if f(a)*f(b)>0:
    print('No root in the given interval')
else:
    for i in range(1,imax):
        

