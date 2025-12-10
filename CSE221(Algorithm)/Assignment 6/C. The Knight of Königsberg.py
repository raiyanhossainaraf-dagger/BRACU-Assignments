import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
x1,y1,x2,y2=map(int,input().strip().split())

x1-=1
y1-=1
x2-=1
y2-=1


if x1==x2 and y1==y2:
    print(0)
    sys.exit()


moves=[(-2,-1),(-2,1),
       (-1,-2),(-1,2),
       (1,-2),(1,2),
       (2,-1),(2,1)]



visited = [False]*(N*N)

def idx(x,y):

    return x*N+y


visited[idx(x1,y1)]=True

q=deque([(x1,y1,0)])



while q:

    x,y,distance= q.popleft()

    for dx,dy in moves:
        
        nx=x+dx
        ny=y+dy
        
        if 0<=nx<N and 0<=ny<N:
            idxy=idx(nx,ny)


            if not visited[idxy]:

                if nx==x2 and ny==y2:

                    print(distance+1)
                    sys.exit()

                visited[idxy]=True
                q.append((nx,ny,distance+1))



print(-1)