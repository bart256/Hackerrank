import sys


def number_components(L,n):
    V,C = [0 for i in range(n+1)],0
    for v in range(1,n+1):
        if V[v] == 0:
            Q,V[v] = [v],1
            while Q != []:
                v = Q.pop()
                for vert in L[v]:
                    if V[vert] == 0:
                        V[vert] = 1
                        Q.insert(0,vert)
            C +=1
    return C            
    
    
    
    

q = int(input().strip())
for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]
    L = [[] for i in range(n+1)]
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        L[city_1].append(city_2),L[city_2].append(city_1)
    if x <y :
        print(x*n)
    else:
        C = number_components(L,n)
        print(C*x +(n-C)*y)
