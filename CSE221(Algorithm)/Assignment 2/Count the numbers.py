import sys
import bisect

input= sys.stdin.readline

n,q = map(int, input().strip().split())

arr=list(map(int,input().strip().split()))

pairs=[]



for i in range(q):

   pair=list(map(int,input().strip().split()))
   pairs.append(pair)


for _ in range(q):

    x, y=map(int, input().strip().split())

    left =bisect.bisect_left(arr, x)
    right =bisect.bisect_right(arr, y)


    print(right - left)