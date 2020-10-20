from time import *
# using (s**2+t**2)**2 = (2*s*t)**2 + (s**2 - t**2)**2

st = time()

memo = {}

for t in range(1, 613):         # all numbers beyond 612 don't satisfy t*(t+s) <= 750_000

    print(t)
    s = t + 1
    while t*(t+s) <= 750_000:               # by simlifying a+b+c<= 1_500_000
        a = (s ** 2 - t ** 2)
        b = (2 * s * t)
        c = (s ** 2 + t ** 2)

        p = a + b + c

        i = 1
        while p*i<= 1_500_000:
            memo[p*i] = memo.get(p*i,set())|{tuple(sorted([a*i,b*i,c*i]))}
            i+=1

        s += 1

ed = time()

print(len(list(filter( lambda x:len(x[1]) == 1, memo.items()))))        # Answer : 161667
print("Time spend :", ed-st)       
