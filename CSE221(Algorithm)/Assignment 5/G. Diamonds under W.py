import sys

input = sys.stdin.readline

R,H=map(int,input().split())
grid=[list(input().strip()) for _ in range(R)]
visited=[[False]*H for _ in range(R)]


dirs=[(-1,0),(1,0),(0,-1),(0,1)]


def dfs(sr,sc):

    stack=[(sr,sc)]
    visited[sr][sc]=True
    diamonds=1 if grid[sr][sc]=='D' else 0

    while stack:

        r,c=stack.pop()

        for dr, dc in dirs:

            nr,nc=r+dr,c+dc

            if 0<=nr<R and 0<=nc<H:

                if not visited[nr][nc] and grid[nr][nc]!='#':

                    visited[nr][nc]=True
                    stack.append((nr,nc))

                    if grid[nr][nc]=='D':

                        diamonds+=1

    return diamonds



max_diamonds=0

for i in range(R):
    
    for j in range(H):


        if not visited[i][j] and grid[i][j]!='#':

            max_diamonds = max(max_diamonds, dfs(i,j))



print(max_diamonds)
