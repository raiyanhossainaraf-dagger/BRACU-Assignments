import sys

input = sys.stdin.readline

N = int(input())

arr =list(map(int, input().strip().split()))
count=0
steps=[]

def reverse_sort(arr, k):
   
   arr[k:k+3]=arr[k:k+3][::-1]
   steps.append((k,k+2)) 
   global count
   count+=1 

sorted_arr=sorted(arr)

even_arr=[arr[i] for i in range(0,N,2)]

even_sorted=[sorted_arr[i] for i in range(0,N,2)]

odd_arr=[arr[i] for i in range(1,N,2)]

odd_sorted=[sorted_arr[i] for i in range(1,N,2)]

from collections import Counter

if Counter(even_arr)!=Counter(even_sorted) or Counter(odd_arr)!=Counter(odd_sorted):

    print("NO")
    sys.exit(0)


a=arr[:]

for i in range(N):

    if a[i] == sorted_arr[i]:
       continue
   
    pos= -1

    for j in range(i+1,N):

        if j%2==i%2 and a[j]==sorted_arr[i]:

            pos=j
            break

    while pos-2 >=i:

        k = pos-2
        reverse_sort(a,k)
        pos-=2
    
    if pos!=i:

       print("NO")
       sys.exit(0)
           
if a!=sorted_arr:

    print("NO")

else:

    print("YES")
    print(len(steps))
    
    for k,l in steps:
        print(k+1, l+1)
    