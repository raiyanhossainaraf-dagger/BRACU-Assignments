import sys
from collections import deque

input=sys.stdin.readline

N,M,S,Q=map(int,input().strip().split())

adjList=[[] for _ in range(N+1)]

def addedge(u,v):

    adjList[u].append(v)
    adjList[v].append(u)

    

for i in range(M):

    u,v=map(int,input().strip().split())

    addedge(u,v)

Sources=list(map(int,input().strip().split()))
destinations=list(map(int,input().strip().split()))


n=len(adjList)          
dist = [-1]*n                   
q = deque()

for s in Sources:

    q.append(s)
    dist[s] = 0

while q:

    u = q.popleft()

    for v in adjList[u]:

        if dist[v]==-1:
            
            dist[v]=dist[u]+1
            q.append(v)

ans=[]
for d in destinations:
    ans.append(str(dist[d]))


print(" ".join(ans))
