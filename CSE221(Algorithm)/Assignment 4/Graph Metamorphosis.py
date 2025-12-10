import sys
input=sys.stdin.readline

N =int(input())
adj =[[0]*N for _ in range(N)]

for i in range(N):

    data=list(map(int, input().split()))
    k=data[0]


    for v in data[1:]:

        adj[i][v]=1


for row in adj:
    print(*row)
