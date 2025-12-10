import sys
from collections import deque

input=sys.stdin.readline

n,m,s,d=map(int,input().split())
u_list=list(map(int,input().split()))
v_list=list(map(int,input().split()))


adj=[[] for _ in range(n+1)]

for u,v in zip(u_list,v_list):

    adj[u].append(v)
    adj[v].append(u)



for neighbors in adj:

    neighbors.sort()


visited=[False]*(n+1)
dist=[-1]*(n+1)
parent=[-1]*(n+1)

queue=deque([s])
visited[s]=True
dist[s]=0

while queue:

    node=queue.popleft()

    for neighbor in adj[node]:

        if not visited[neighbor]:

            visited[neighbor]=True
            dist[neighbor]=dist[node]+1
            parent[neighbor]=node
            queue.append(neighbor)


if not visited[d]:

    print(-1)

else:

    path=[]
    curr=d


    while curr!=-1:

        path.append(curr)
        curr = parent[curr]

    path.reverse()
    

    
    print(dist[d])
    print(*path)
