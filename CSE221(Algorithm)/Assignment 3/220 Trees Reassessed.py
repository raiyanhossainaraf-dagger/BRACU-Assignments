import sys

input=sys.stdin.readline

N=int(input())

inOrder=list(map(int,input().strip().split()))
postOrder=list(map(int,input().strip().split()))

preOrder=[]

inOrder_index={val:idx for idx,val in enumerate(inOrder)}

postOrder_index=[N-1]


def build_preOrder(inOrder_left,inOrder_right):

    if inOrder_left>inOrder_right:

        return []
    
    root=postOrder[postOrder_index[0]]
    postOrder_index[0]-=1

    root_index=inOrder_index[root]


    preOrder.append(root)


    right_subTree=build_preOrder(root_index+1,inOrder_right)
    left_subTree=build_preOrder(inOrder_left,root_index-1)


    return [root]+left_subTree+right_subTree 



preOrder=build_preOrder(0,N-1)

print(*preOrder)