import sys 
from collections import deque


input=sys.stdin.readline
N=int(input())

adjList=[[] for _ in range(N+1)]
maxCount=0


def addEdge(u,v):
    adjList[u].append(v)
    adjList[v].append(u)



def bfs(adjList, start):

    n=len(adjList)          
    visited=[False]*n
    dist = [-1]*n           
    parent = [-1]*n         

    q = deque()
    q.append(start)
    visited[start] = True
    dist[start] = 0

    while q:
        u = q.popleft()

        for v in adjList[u]:

            if not visited[v]:
                
                visited[v]=True
                dist[v]=dist[u] + 1
                parent[v]=u
                q.append(v)

    count=max(dist)
    idx=dist.index(count)
        

    return count, idx



for _ in range(1,N):

    u,v=map(int,input().strip().split())
    addEdge(u,v)

    
count1,idx1=bfs(adjList,1)
count2,idx2=bfs(adjList,idx1)

maxCount=max(count1,count2)

print(maxCount)
print(f"{idx1} {idx2}")