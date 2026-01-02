import sys
input=sys.stdin.readline

N,M=map(int,input().split())
edges=[]

for _ in range(M):

    u,v,w=map(int,input().split())
    edges.append((w,u,v))


edges.sort()

parent=list(range(N+1))
size=[1]*(N+1)

def find(x):

    while parent[x]!=x:

        parent[x]=parent[parent[x]]
        x=parent[x]

    return x

def union(a,b):

    ra=find(a)
    rb=find(b)

    if ra!=rb:

        if size[ra]<size[rb]:

            ra,rb=rb,ra
        parent[rb]=ra
        size[ra]+=size[rb]

        return True
    
    return False

mst_cost=0
edges_used=0

for w,u,v in edges:

    if union(u, v):
        
        mst_cost+=w
        edges_used+=1

        if edges_used==N-1:

            break

print(mst_cost)
