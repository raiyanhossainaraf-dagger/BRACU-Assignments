import sys

input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().strip().split()))

rslt=[]

def array_to_bst(arr):

    return helper(0,N-1)
    
    

def helper(l,r):

        if l>r:
            return
        
        mid=(l+r)//2
        rslt.append(arr[mid])

        helper(l,mid-1)
        helper(mid+1,r)

        return rslt

print(*array_to_bst(arr))