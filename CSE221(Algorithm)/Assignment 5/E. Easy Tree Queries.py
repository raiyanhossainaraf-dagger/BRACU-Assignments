import sys
input=sys.stdin.readline

n,r=map(int,input().split())
adj=[[] for _ in range(n+1)]

for _ in range(n-1):

    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

subtree_size=[0]*(n+1)
visited=[False]*(n+1)

stack=[(r,0)]
order=[] 


while stack:

    node,parent=stack.pop()

    if visited[node]:

        continue

    visited[node]=True
    order.append((node, parent))

    for neighbor in adj[node]:

        if neighbor!=parent:

            stack.append((neighbor,node))


subtree_size=[1]*(n+1) 

for node,parent in reversed(order):

    for neighbor in adj[node]:

        if neighbor!=parent:

            subtree_size[node]+=subtree_size[neighbor]


q=int(input())

for _ in range(q):

    x=int(input())
    print(subtree_size[x])
