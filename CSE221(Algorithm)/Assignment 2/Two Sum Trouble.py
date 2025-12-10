import sys

input = sys.stdin.readline

N= list(map(int,input().strip().split()))

target= N[1]

nums= list(map(int, input().strip().split()))

i=0
j=len(nums)-1

found=False

while i<j:

   

    if(nums[i]+nums[j]==target):

        print(f"{i+1} {j+1}")

        found=True
        break

    else:
        if(nums[i]+nums[j]>target):
            j-=1
        else:
            i+=1

if  found==False:
    print('-1')