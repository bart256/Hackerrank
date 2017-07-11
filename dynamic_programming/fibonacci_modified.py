[t1,t2,n] = list(map(int,input().split(' ')))
k = 2
while k < n:
    t1,t2 = t2,t1+t2**2
    k+=1
print(t2)
