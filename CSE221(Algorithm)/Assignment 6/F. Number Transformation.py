import sys
from collections import deque

input=sys.stdin.readline


MAX_T=5000
spf=list(range(MAX_T+1)) 

for i in range(2,int(MAX_T**0.5)+1):

    if spf[i]==i:

        for j in range(i*i, MAX_T+1, i):

            if spf[j]==j:

                spf[j]=i

def prime_factors(n):
    
    pf = set()

    while n>1:

        p = spf[n]
        pf.add(p)

        while n % p == 0:

            n //= p

    return pf

T = int(input().strip())

for _ in range(T):
    s,t=map(int, input().split())

    if s==t:
        print(0)
        continue

    if s>t:
        print(-1)
        continue

    dist=[-1]*(t+1)
    q=deque()
    dist[s] = 0
    q.append(s)

    while q:

        u = q.popleft()
        
        for p in prime_factors(u):
            
            if p==u:
                continue

            v=u+p

            if v<=t and dist[v]==-1:

                dist[v] = dist[u] + 1
                q.append(v)

        
        if dist[t] != -1:
            break

    print(dist[t])
