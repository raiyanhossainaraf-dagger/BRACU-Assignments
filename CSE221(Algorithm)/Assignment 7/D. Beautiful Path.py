import sys
import heapq

input=sys.stdin.readline

N,M,S,D=map(int,input().strip().split())
w=[0]+list(map(int,input().strip().split()))

adjList=[[] for _ in range(N+1)]


def addEdge(adjL,u,v):

    adjL[u].append(v)

for _ in range(M):

    u,v=map(int,input().strip().split())
    addEdge(adjList,u,v)

def dijkstra(N, adj, source):

    INF=float('inf')
    dist=[INF]*(N+1)
    parent=[-1]*(N+1)  

    dist[source]=w[source]
    pq=[(dist[source], source)]

    while pq:

        curr_dist,u=heapq.heappop(pq)

        if curr_dist>dist[u]:

            continue

        for v in adj[u]:
            
            newCost=dist[u]+w[v]
            if newCost<dist[v]:

                dist[v]=newCost
                parent[v]=u
                heapq.heappush(pq,(dist[v],v))

    return dist, parent


dist,parent=dijkstra(N,adjList,1)

print(dist[D] if dist[D]!=float('inf') else -1)