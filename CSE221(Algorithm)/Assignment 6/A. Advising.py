import sys
import queue

input=sys.stdin.readline

N,M=map(int,input().strip().split())

adjList=[[] for _ in range(N + 1)]
indeg=[0]*(N+1)
q=queue.Queue()


def addEdgetoMatrix(source, destination):

    adjList[source].append(destination)


for _ in range(M):

    u,v= map(int, input().split())
    addEdgetoMatrix(u,v)

    indeg[v] += 1
  

for  i in range(1,len(indeg)):
      
        if indeg[i]==0:
           q.put(i)


if q.empty()==True:

    print(-1)

else:
    while  not q.empty():

        i=q.get()
        print(i)
        
        for j in adjList[i]:

            indeg[j]-=1

            if indeg[j]==0:

                q.put(j)
        
        
