import sys
from math import gcd


input = sys.stdin.readline

N, Q = map(int,input().split())


adj=[[] for _ in range(N+1)]


for i in range(1,N+1):

    for j in range(1,N+1):

        if i!=j and gcd(i,j)==1:

            adj[i].append(j)


    adj[i].sort()     


out=[]

for _ in range(Q):

    X,K=map(int,input().split())

    if K<=len(adj[X]):

        out.append(str(adj[X][K-1]))

    else:

        out.append("-1")

        

print("\n".join(out))
