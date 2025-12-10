import sys
import numpy as np

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())
    num = input()
    arr= np.array(num.split(), dtype=int)
    
    if is_sorted := np.all(arr[:-1] <= arr[1:]):
        print("YES")
    else:
        print("NO")



