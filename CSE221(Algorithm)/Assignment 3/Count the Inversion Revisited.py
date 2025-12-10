import sys,bisect
input= sys.stdin.readline

N=int(input())
arr=list(map(int,input().strip().split()))

count=0
squares= []


for i in range(N-1,-1,-1):

   position=bisect.bisect_left(squares,arr[i])
   
   count+=position

   bisect.insort(squares,arr[i]*arr[i])
        


print(count)