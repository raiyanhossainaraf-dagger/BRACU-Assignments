import sys
import heapq

input=sys.stdin.readline

N,M,S,T=map(int,input().strip().split())
adjList=[[] for _ in range (N+1)]

def addEdges(adj,u,v,w):
    adj[u].append((v,w))


for _ in range(M):

    u,v,w=map(int,input().strip().split())

    addEdges(adjList,u,v,w)

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

distA,parentA=dijkstra(N,adjList,S)
distB,parentB=dijkstra(N,adjList,T)

bestTime=float('inf')
bestNode=-1
INF=float('inf')

for i in range(1,N+1):

    if distA[i]<INF and distB[i]<INF:
        
        meetTime=max(distA[i],distB[i])

        if meetTime<bestTime or (meetTime==bestTime and i<bestNode):
            bestTime=meetTime
            bestNode=i


if bestNode==-1:
    print(-1)

else:
    print(bestTime, bestNode)