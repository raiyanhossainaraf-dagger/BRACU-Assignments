import sys

input = sys.stdin.readline

N= list(map(int,input().strip().split()))

target= N[2]

arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))

i=0
j=len(arr2)-1

min_diff= float('inf')

best_i,best_j=1,1

while i<len(arr1) and j>=0:


    sum=arr1[i]+arr2[j]
    diff= abs(sum - target)

    if diff<min_diff:

        min_diff=diff
        best_i,best_j=i+1,j+1
   
    if(arr1[i]+arr2[j]>target):
            j-=1
    else:
            i+=1


print(f"{best_i} {best_j}")