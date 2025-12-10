import sys
input = sys.stdin.readline

N= list(map(int,input().strip().split()))

arr=list(map(int,input().strip().split()))

target=N[1]

j=0
count= 0
distinct_elements={}

for i in range(len(arr)):

   distinct_elements[arr[i]]= distinct_elements.get(arr[i],0)+1


   while len(distinct_elements)>target:
      
      y=arr[j]
      distinct_elements[y]-=1


      if distinct_elements[y]==0:
         
         del distinct_elements[y]
    
      j+=1


    
   count=max(count, i-j+1)
   
print(count)
    
