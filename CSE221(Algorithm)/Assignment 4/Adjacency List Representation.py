import sys

input=sys.stdin.readline

N,M=map(int,input().strip().split())
adjList=[None]*(N+1)


u=list(map(int,input().strip().split()))
v=list(map(int,input().strip().split()))
w=list(map(int,input().strip().split()))



class graphUtils:

    @staticmethod
    def addEdge(adjList,From,to,wieght):
        
        newNode= EdgeNode(to,wieght)

        if adjList[From] is None:

            adjList[From]=newNode

        else:

            graphUtils.appendLL(adjList[From],newNode)

    @staticmethod
    def appendLL(head,newNode):

        while head.next is not None:

            head=head.next

        head.next=newNode

    @staticmethod
    def showAdjList(adjList):

        for i in range(1,len(adjList)):

            print(f"{i}:", end=" ")
            node = adjList[i]

            while node is not None:
                print(f"({node.toV},{node.weight}) ",end=" ")
                node = node.next
            print()



class EdgeNode:

    def __init__(self,toV,weight):

        self.toV= toV
        self.weight= weight
        self.next=None
        


for i in range(M):

    graphUtils.addEdge(adjList, u[i], v[i], w[i])

graphUtils.showAdjList(adjList)
    