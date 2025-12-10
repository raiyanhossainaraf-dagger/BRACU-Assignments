import sys

input = sys.stdin.readline

N = int(input())

arr =list(map(int, input().strip().split()))


def sort(arr):
    for i in range(N-1):


            if (arr[i]%2==0 and arr[i+1]%2==0)  and arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                
            
            elif (arr[i]%2!=0 and arr[i+1]%2!=0)  and arr[i] > arr[i+1]:

                arr[i], arr[i+1] = arr[i+1], arr[i]
                
               
    return arr

for i in range(1000):

    sorted_arr=sort(arr)

print(*sorted_arr)