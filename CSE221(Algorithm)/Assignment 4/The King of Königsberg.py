import sys

input=sys.stdin.readline

N=int(input())
x,y=map(int,input().split())

moves=[
        (x-1,y-1),
        (x-1,  y),
        (x-1,y+1),
        (x,  y-1),
        (x,  y+1),
        (x+1,y-1),
        (x+1,  y),
        (x+1,y+1)
                    ]


valid=[]

for a,b in moves:

    if 1<=a<=N and 1<=b<=N:

        valid.append((a,b))

valid.sort()

print(len(valid))

for a,b in valid:

    print(a,b)
