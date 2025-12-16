import sys
import heapq

input=sys.stdin.readline

N,M,S,D=map(int,input().strip().split())

adjList=[[] for _ in range(N+1)]
u=list(map(int, input().strip().split()))
v=list(map(int, input().strip().split()))
w=list(map(int, input().strip().split()))

for _ in range(M):
    adjList[u[_]].append((v[_],w[_]))


def dijkstra(N, adj, source):

    INF=float('inf')
    dist=[INF]*(N+1)
    parent=[-1]*(N+1)  

    dist[source]=0
    pq=[(0, source)]

    while pq:

        curr_dist,u=heapq.heappop(pq)

        if curr_dist>dist[u]:

            continue

        for v, w in adj[u]:

            if dist[u]+w<dist[v]:

                dist[v]=dist[u]+w
                parent[v]=u
                heapq.heappush(pq,(dist[v],v))

    return dist, parent

distance,parent=dijkstra(N,adjList,S)
INF=float('inf')

if distance[D]!=INF:

    print(distance[D])
  
    path=[]
    cur=D

    while cur!=-1:

        path.append(cur)
        cur=parent[cur]

    path.reverse()
    print(*path)

else:
    print(-1)