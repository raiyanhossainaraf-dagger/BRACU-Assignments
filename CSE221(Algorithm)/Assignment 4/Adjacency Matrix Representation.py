import sys

input=sys.stdin.readline

N,M=map(int,input().strip().split())

arr=[[0]*N for _ in range(N)]

for i in range(M):

    u,v,w=map(int,input().strip().split())
    
    arr[u-1][v-1]=w

for row in arr:

    print (*row)