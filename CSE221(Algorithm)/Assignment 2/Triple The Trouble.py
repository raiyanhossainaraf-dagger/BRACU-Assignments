import sys

input = sys.stdin.readline

N= list(map(int,input().strip().split()))

arr= list(map(int, input().strip().split()))

nums=[(arr[idx], idx) for idx in range(len(arr))]
nums.sort(key=lambda x: x[0])

target= N[1]

found=False

for i in range(len(nums)-2):

    left=i+1
    right=len(nums)-1

    while left<right:

        current_sum= nums[i][0]+nums[left][0]+nums[right][0]

        if current_sum==target:

            indices= sorted([nums[i][1]+1, nums[left][1]+1, nums[right][1]+1])

            print(f"{indices[0]} {indices[1]} {indices[2]}")

            found=True
            break

        elif current_sum<target:
            left+=1
        else:
            right-=1
    
    if found:
        break
        
    

if not found:
    print('-1')