import sys
input= sys.stdin.readline

T=int(input())
answers=[]

for i in range(T):

    a,n,m=map(int,input().strip().split())

    if a==1:

        calc2=n%m

    
    else:

        calc1=(a*(pow(a,n,m*(a-1))-1))%(m*(a-1))
        calc2=(calc1//(a-1))%m

    answers.append(calc2)

    



for answer in answers:
    print(answer)