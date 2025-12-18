import sys
import heapq

input=sys.stdin.readline

N,M=map(int,input().strip().split())
INF=10**18

adjList=[[] for _ in range(N+1)]
u=list(map(int, input().strip().split()))
v=list(map(int, input().strip().split()))
w=list(map(int, input().strip().split()))

for _ in range(M):
    adjList[u[_]].append((v[_],w[_]))


def dijkstra(N, adj, source):

    dist=[[INF,INF] for _ in range(N+1)]

    dist[source][0]=0
    dist[source][1]=0

    pq=[]

    heapq.heappush(pq,(0, source, 0))
    heapq.heappush(pq,(0, source, 1))

    while pq:

        d,u,lastParity=heapq.heappop(pq)

        if d>dist[u][lastParity]:

            continue

        for v, weight in adj[u]:

            currParity=weight%2

            if currParity!=lastParity:

                nd=d+weight
                if nd<dist[v][currParity]:

                    dist[v][currParity]=nd
                    heapq.heappush(pq,(nd,v,currParity))


    return dist

dist=dijkstra(N,adjList,1)

finalDist=min(dist[N][0],dist[N][1])

print(finalDist if finalDist != INF else -1)