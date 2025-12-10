import sys

input = sys.stdin.readline

T = int(input())

pairs=[list(map(int,input().strip().split())) for _ in range(T)]

answers=[]

for k,x in pairs:
    
    full_blocks= k//(x - 1)
    remainder= k%(x - 1)
    

    if remainder==0:

        ans=full_blocks*x-1


    else:
        ans=full_blocks*x+remainder
    
    answers.append(ans)


for answer in answers:

    print(answer)