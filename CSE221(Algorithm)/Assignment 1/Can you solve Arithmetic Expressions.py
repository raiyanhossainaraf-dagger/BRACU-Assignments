import sys
input = sys.stdin.readline

operators ={
    '+':lambda x,y: x+y,
    '-':lambda x,y: x-y,
    '*':lambda x,y: x*y,
    '/':lambda x,y: x/y
    }

T = int(input())

for _ in range(T):

    N=[n for n in input().split() if n]

    for i,n in enumerate(N):
        if n in operators:
            op = n
            a=float(N[i-1])

            b=float(N[i+1])
            break

    result = operators[op](a,b)

    print(result)

    #N=[n for n in input().split() if n]
    #N=list(input().strip().split())