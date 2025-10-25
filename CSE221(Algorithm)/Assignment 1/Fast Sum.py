import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    sum = N*(N + 1)/2
    print(int(sum))
   
