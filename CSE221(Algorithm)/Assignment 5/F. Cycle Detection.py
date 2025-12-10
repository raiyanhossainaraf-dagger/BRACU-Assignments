import sys

input=sys.stdin.readline

n,m=map(int,input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):

    u,v=map(int,input().split())
    adj[u].append(v)


visited=[False]*(n+1)
in_stack=[False]*(n+1)

def has_cycle(start):

    stack=[(start,0)] 
    path_stack=[]  


    while stack:

        node,idx=stack.pop()

        if idx==0:

           
            visited[node]=True
            in_stack[node]=True
            path_stack.append(node)

        if idx < len(adj[node]):

            neighbor=adj[node][idx]
            stack.append((node,idx+1))

            if not visited[neighbor]:

                stack.append((neighbor,0))

            elif in_stack[neighbor]:

                
                return True
            
        else:
           
            in_stack[node]=False
            path_stack.pop()


    return False

cycle_found=False

for node in range(1,n+1):

    if not visited[node]:

        if has_cycle(node):

            cycle_found=True

            break



print("YES" if cycle_found else "NO")
