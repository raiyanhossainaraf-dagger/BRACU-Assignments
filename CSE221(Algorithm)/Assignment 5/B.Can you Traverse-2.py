import sys

input=sys.stdin.readline

n,m=map(int, input().split())
u_list=list(map(int, input().split()))
v_list=list(map(int, input().split()))


adj=[[] for _ in range(n+1)]
for u, v in zip(u_list,v_list):

    adj[u].append(v)
    adj[v].append(u)


for neighbors in adj:

    neighbors.sort()

visited=[False]*(n+1)
result=[]


stack=[1]

while stack:

    node=stack.pop()

    if not visited[node]:

        visited[node]=True
        result.append(node)
      
        for neighbor in reversed(adj[node]):

            if not visited[neighbor]:

                stack.append(neighbor)



print(*result)
