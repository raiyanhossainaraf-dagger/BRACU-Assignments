import sys

input = sys.stdin.readline

N= int(input())
arr= list(map(int, input().strip().split()))

count=0


def mergeSort(arr):

    if len(arr)<=1:

        return arr
    
    mid=len(arr)//2
    left=mergeSort(arr[:mid])
    right=mergeSort(arr[mid:])

    merg=merging(left,right)

    return merg

def merging(left,right):

    global count 
    
    i,j=0,0
    merged=[]

    while i<len(left) and j<len(right):

       

        if left[i]<right[j]:

            merged.append(left[i])
            i+=1
            

        else:

            merged.append(right[j])
            j+=1
            count+=len(left)-i
        
        
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


mergeSort(arr)
print(count)
print(*mergeSort(arr))
