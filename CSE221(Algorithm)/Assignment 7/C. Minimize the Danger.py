import sys
import heapq

input=sys.stdin.readline

N,M=map(int,input().strip().split())

adjList=[[] for _ in range(N+1)]

def addEdge(adjL,u,v,w):

    adjL[u].append((v,w))
    adjL[v].append((u,w))

for _ in range(M):

    u,v,w=map(int,input().strip().split())

    addEdge(adjList,u,v,w)

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

            newDanger=max(dist[u],w)

            if newDanger<dist[v]:

                dist[v]=newDanger
                parent[v]=u
                heapq.heappush(pq,(dist[v],v))

    return dist, parent


dist,parent=dijkstra(N,adjList,1)

for i in range(1,len(dist)):

    print(dist[i] if dist[i] != float('inf') else -1)