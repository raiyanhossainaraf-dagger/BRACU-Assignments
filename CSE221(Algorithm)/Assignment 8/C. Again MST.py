import sys
from collections import deque

def find(parent, x):

    while parent[x] != x:

        parent[x] = parent[parent[x]]
        x = parent[x]
        
    return x

def union(parent, rank,a,b):

    a=find(parent,a)
    b=find(parent,b)

    if a == b:

        return False
    
    if rank[a]<rank[b]:

        parent[a]=b

    else:

        parent[b]=a

        if rank[a]==rank[b]:

            rank[a] += 1

    return True


def max_two_edges_on_path(start, end, adj, n):

    visited = [False]*n
    q=deque()
    q.append((start, -1, -1))  
    visited[start] = True

    while q:

        u, mx1, mx2 =q.popleft()

        if u == end:
            return mx1, mx2

        for v,w in adj[u]:

            if not visited[v]:

                visited[v] = True

                a, b = mx1, mx2

                if w>a:

                    a, b = w, a

                elif w>b:
                

                    b=w
                q.append((v,a,b))

    return -1,-1 


def main():

    input = sys.stdin.readline
    n, m = map(int, input().split())

    edges=[]

    for _ in range(m):

        u, v, w = map(int, input().split())
        edges.append((w,u-1,v-1))


    edges.sort()


    parent =list(range(n))
    rank = [0]*n

    mst_cost= 0
    used =[False]*m
    mst_edges = []

    

    for i, (w, u, v) in enumerate(edges):

        if union(parent, rank, u, v):

            mst_cost+= w
            used[i] =True
            mst_edges.append((u,v,w))

    if len(mst_edges) != n - 1:

        print(-1)

        return

    
    adj = [[] for _ in range(n)]

    for u, v, w in mst_edges:

        adj[u].append((v,w))
        adj[v].append((u,w))

    INF =10**30
    ans =INF

    for i, (w, u, v) in enumerate(edges):

        if used[i]:

            continue

        mx1,mx2=max_two_edges_on_path(u, v, adj, n)

        if w>mx1:

            ans = min(ans,mst_cost+w-mx1)
        elif w > mx2:

            ans = min(ans,mst_cost+w-mx2)

    print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
