import sys
import heapq

input=sys.stdin.readline

N,M,S,D=map(int,input().strip().split())

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
    lastDist=[INF]*(N+1)

    dist[source]=0
    pq=[(0,source)]

    while pq:
        d,u=heapq.heappop(pq)

        for v,w in adj[u]:

            nd=d+w

            if nd<dist[v]:

                lastDist[v]=dist[v]
                dist[v]=nd
                heapq.heappush(pq,(nd,v))

            elif dist[v]<nd<lastDist[v]:

                lastDist[v]=nd
                heapq.heappush(pq,(nd,v))

    return lastDist

dist=dijkstra(N,adjList,S)

print(dist[D] if dist[D] != float('inf') else -1)