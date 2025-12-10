import sys

data = list(map(int, sys.stdin.buffer.read().split()))

if not data:

    sys.exit()


it=iter(data)
N=next(it)
M=next(it)

deg=[0]*(N + 1)

u=[next(it) for _ in range(M)]
v=[next(it) for _ in range(M)]

for i in range(M):

    deg[u[i]]+=1
    deg[v[i]]+=1

odd=sum(1 for x in range(1,N+1) if deg[x]%2==1)

print("YES" if odd==0 or odd==2 else "NO")
