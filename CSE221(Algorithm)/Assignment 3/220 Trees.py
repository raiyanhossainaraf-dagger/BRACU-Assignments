import sys

input=sys.stdin.readline

N=int(input())

inOrder=list(map(int,input().strip().split()))
preOrder=list(map(int,input().strip().split()))

postOrder=[]

inOrder_index={val:idx for idx,val in enumerate(inOrder)}



def build_PostOrder(inOrder_left, inOrder_right, preOrder_left,preOrder_right):


    if inOrder_left>inOrder_right or preOrder_left>preOrder_right:

        return
    
    root =preOrder[preOrder_left]
    root_index =inOrder_index[root]
    
    
    left_size =root_index-inOrder_left
    
    
    build_PostOrder(inOrder_left,root_index-1,preOrder_left+1,preOrder_left+left_size)
    build_PostOrder(root_index+1,inOrder_right,preOrder_left+left_size+1,preOrder_right)
    

    postOrder.append(root)



build_PostOrder(0, N - 1, 0, N - 1)

print(*postOrder)