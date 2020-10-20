import time
def form(n,d=1):
    i = 0
    while n.imag**0.5+n.real-i*d>0:
        i+=1
    i-=1
    n = n+i*d-2*n.real
    d = (n.imag-n.real**2)/d
    return  i,n,d

st = time.time()
count = 0
for k in range(10000):
    if int(k**0.5)!=k**0.5:
        t = 1
        m = form(eval(str(k)+'j'))
        while m[2] !=1:
            m = form(*m[1:])
            t+=1
        if t%2 ==1:
            count += 1
print('Answer:',count)      # Answer: 1322
ed = time.time()
print('Time spend :',ed-st)
