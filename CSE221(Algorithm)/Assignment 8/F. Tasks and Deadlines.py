import sys

def main():


    input=sys.stdin.readline

    n=int(input())
    tasks=[]

    for _ in range(n):

        a,d =map(int, input().split())
        tasks.append((a,d))

    
    tasks.sort()

    time=0
    reward =0

    for a,d in tasks:

        time+=a
        reward+=d-time

    print(reward)



if __name__ =="__main__":
    main()
