import sys

data=list(map(int, sys.stdin.buffer.read().split()))

if not data:
    
    sys.exit()

index=0
N=data[index]; index+=1
M=data[index]; index+=1


outdeg=[0]*(N+1)
indeg=[0]*(N+1)


u=data[index:index+M]
index+=M


v=data[index: index +M]
index+=M


for i in range(M):

    outdeg[u[i]]+=1
    indeg[v[i]]+=1



result=[]

for i in range(1, N + 1):

    result.append(indeg[i]-outdeg[i])



print(*result)
