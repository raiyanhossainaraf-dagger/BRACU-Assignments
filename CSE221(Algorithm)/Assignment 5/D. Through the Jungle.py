import sys
from collections import deque

input=sys.stdin.readline

n,m,s,d,k=map(int,input().split())


adj=[[] for _ in range(n+1)]

for _ in range(m):
    
    u,v=map(int,input().split())
    adj[u].append(v)

def bfs(start,end):

    visited=[False]*(n+1)
    parent=[-1]*(n+1)
    queue=deque([start])
    visited[start]=True

    while queue:

        node=queue.popleft()

        if node==end:

            break

        for neighbor in adj[node]:

            if not visited[neighbor]:

                visited[neighbor]=True
                parent[neighbor]=node
                queue.append(neighbor)


    if not visited[end]:

        return None  



    path=[]
    curr=end

    while curr!=-1:

        path.append(curr)
        curr=parent[curr]

    path.reverse()
    return path



if s==d and s==k:

    print(0)
    print(s)

    sys.exit()


path1=bfs(s,k)

if path1 is None:

    print(-1)

    sys.exit()


path2=bfs(k,d)

if path2 is None:

    print(-1)

    sys.exit()


full_path=path1+path2[1:]

print(len(full_path)-1)

print(*full_path)
