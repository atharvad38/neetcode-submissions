class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for _ in range(m)]for _ in range(n)]

        def solve(i,j):
            if i<0 or j<0 or i>n-1 or j>m-1 or grid[i][j]==0 or visited[i][j]==1:
                return 0
            visited[i][j] = 1
            top = solve(i-1,j)
            bottom = solve(i+1,j)
            left = solve(i,j-1)
            right = solve(i,j+1)
            return 1+top+bottom+left+right
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and visited[i][j]==0:
                    cur = solve(i,j)
                    ans=max(ans,cur)
        return ans
        