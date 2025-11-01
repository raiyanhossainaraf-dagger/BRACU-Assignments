import sys
input = sys.stdin.readline

N= list(map(int,input().strip().split()))
arr=list(map(int,input().strip().split()))

allowed_sum =N[1]

    
i=0
sum=0
max_count=0

for j in range(len(arr)):
    sum+=arr[j]

    while sum >allowed_sum and i<=j: 
        sum-=arr[i]
        i+=1

    max_count=max(max_count, j-i+1)

print(max_count)


