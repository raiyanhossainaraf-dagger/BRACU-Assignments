import sys
input = sys.stdin.readline

N= int(input())
arr1= list(map(int, input().strip().split()))

M=int(input())
arr2= list(map(int, input().strip().split()))

i=0
j=0

merged=[]

while True:

    if i<N and j<M:
        if arr1[i]==arr2[j]:
            merged.append(arr1[i])
            merged.append(arr2[j])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1

    elif i<N:
        merged.append(arr1[i])
        i+=1
    
    elif j<M:
        merged.append(arr2[j])
        j+=1

    else:
        break

print(*merged)