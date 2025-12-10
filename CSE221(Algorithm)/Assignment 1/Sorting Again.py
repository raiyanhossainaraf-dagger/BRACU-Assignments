import sys

input = sys.stdin.readline

T = int(input())



def selection_sorting(arr,id):

        n = len(arr)
        arr1=list(enumerate(zip(arr,id)))
        arr1.sort(key=lambda x: (-x[1][0], x[1][1]))
        visited = [False]*n


        for i in range(n):

            if visited[i] or arr1[i][0]==i:
                continue
         
            cycle_size=0
            j = i

            while not visited[j]:

                visited[j] = True
                j = arr1[j][0]
                cycle_size += 1
        
            if cycle_size > 1:
                
                global count
                count += (cycle_size - 1)
             
        return arr

for _ in range(T):

    count=0

    N = int(input())

    id = list(map(int, input().strip().split()))  
    marks = list(map(int, input().strip().split())) 

    dict_marks = {id[j]: marks[j] for j in range(N) }

    sorted_marks = selection_sorting(marks.copy(),id)

    dict_marks_sorted = dict(sorted(dict_marks.items(), key=lambda item:(-item[1], item[0])))      

    print(f"Minimum swaps: {count}")

    for key,value in dict_marks_sorted.items():
         
         print(f"ID: {key} Mark: {value}")
         

       






