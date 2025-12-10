import sys
import queue

input=sys.stdin.readline

N,M=map(int,input().strip().split())

adjList=[[] for _ in range(N + 1)]

color=[0]*(N+1)
group1_total=0
group2_total=0

def addEdgetoMatrix(source,destination):

    adjList[source].append(destination)
    adjList[destination].append(source)


for _ in range(M):

    u, v = map(int, input().strip().split())
    addEdgetoMatrix(u,v)



for start in range(1,N+1):

    if color[start]==0: 
        
        q=queue.Queue()
        q.put(start)
        color[start]=1
        group1_count=0
        group2_count=0
        
        while not q.empty():

            node=q.get()
            
            if color[node]==1:

                group1_count+=1

            else:

                group2_count += 1
            
            for neighbor in adjList[node]:

                if color[neighbor]==0:

                    
                    color[neighbor]=3-color[node]
                    q.put(neighbor)
        
        
        group1_total+=max(group1_count, group2_count)


isolated = sum(1 for i in range(1,N+1) if color[i]==0)
print(group1_total+isolated)