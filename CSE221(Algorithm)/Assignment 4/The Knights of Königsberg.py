import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())


knights=set()

positions=[]

for _ in range(K):

    x,y=map(int,input().split())
    positions.append((x,y))
    knights.add((x,y))


moves = [

            (2,1),(2,-1),(-2,1),(-2,-1),
            (1,2),(1,-2),(-1,2),(-1,-2)
                                            ]



for x,y in positions:

    for dx,dy in moves:

        nx,ny= x+dx,y+dy

        if (nx,ny) in knights:

            print("YES")

            sys.exit()

print("NO")
