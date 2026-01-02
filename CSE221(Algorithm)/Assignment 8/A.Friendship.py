import sys

input=sys.stdin.readline
write=sys.stdout.write

N,K=map(int,input().strip().split())

parent=[i for i in range(N+1)]
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
        
        if size[ra] < size[rb]:

            ra,rb=rb,ra
        parent[rb]=ra
        size[ra]+=size[rb]
    
    return size[find(a)]

for _ in range(K):

    a,b=map(int, input().split())

    write(str(union(a,b))+"\n")
