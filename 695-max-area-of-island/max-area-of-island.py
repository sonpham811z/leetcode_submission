class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0
        island=0
        tmp = 0

        def dfs(r,c):
            nonlocal tmp
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 

            grid[r][c] = 0
            tmp +=1

            print(tmp)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            


        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1):
                    island+=1
                    dfs(r,c)
                    max_area = max(max_area, tmp)
                    tmp = 0

        print(island)
        return max_area
        