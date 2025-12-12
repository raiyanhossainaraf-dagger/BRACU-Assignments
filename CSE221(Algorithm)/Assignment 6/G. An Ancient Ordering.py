import sys
import heapq
from collections import defaultdict,deque

input=sys.stdin.readline

N=int(input())
words=[input().strip() for _ in range(N)]

graph=defaultdict(set)
indeg=defaultdict(int)
letters=set()


for word in words:

    for c in word:

        letters.add(c)


impossible = False

for i in range(N-1):

    w1,w2=words[i],words[i+1]
    min_len=min(len(w1),len(w2))
    found_diff=False

    for j in range(min_len):

        if w1[j]!=w2[j]:

            if w2[j] not in graph[w1[j]]:

                graph[w1[j]].add(w2[j])
                indeg[w2[j]]+=1

            found_diff=True
            break

    if not found_diff and len(w1)>len(w2):

        impossible=True
        break

if impossible:

    print(-1)
    sys.exit()


heap=[]

for c in letters:

    if indeg[c]==0:

        heapq.heappush(heap,c)

res=[]


while heap:

    u = heapq.heappop(heap)
    res.append(u)

    for v in graph[u]:

        indeg[v]-=1

        if indeg[v]==0:

            heapq.heappush(heap,v)



if len(res)!=len(letters):

    print(-1)  

else:
    print("".join(res))
