from itertools import combinations
from time import time
from fractions import Fraction

def form(n,d=1):
    ''' Helper function to compute continued fraction.'''
    i = 0
    while n.imag**0.5+n.real-i*d>0:
        i+=1
    i-=1
    n = n+i*d-2*n.real
    d = (n.imag-n.real**2)/d
    return  i,n,d

def continuedFraction(n):
    ''' returns the continued fraction for the square root of the given n.
        example: continuedFraction(2) returns [1,2]
                i.e.    2**0.5 = 1+ 1/(2 + 1 / (2 + 1 / ...) )'''
    m = form(eval(str(n) + 'j'))
    cont = [m[0]]
    while m[2] != 1:

        m = form(*m[1:])
        cont.append(m[0])
    cont.append(form(m[1])[0])
    return cont

def computeSolution( d ):
    ''' compute fundamental solution for pell's equation
        it can be,  x**2 - d* y**2 = 1/-1
        returns the x,y values for given d'''
    lst = continuedFraction(d)
    n = 0
    if len(lst) > 2:
        lst = lst [:-1]

    for i in lst[::-1]:
        if n>0:
            n = i + Fraction(1,n)
        else:
            n += i
    return n.numerator, n.denominator

st = time()
maxX = 0
d = 0
for n in range( 2,1000+1):
    if int(n**0.5) == n**0.5 :
        continue
    x,y = computeSolution(n)
    s = "{}**2 - {} * {}**2".format(x,n,y)
    if eval(s) == -1:           # looking for next solution 
        x, y = x**2 + y**2 * n, 2*x*y

    s = "{}**2 - {} * {}**2".format(x, n, y)
    #print(s,'=',eval(s))

    if maxX < x :
        maxX = x
        d = n
print("Answer : ", d)

ed = time()
print('Time Spended : ',ed-st)
