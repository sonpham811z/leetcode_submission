class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                i, j = queue.popleft()

                if i - 1 >= 0 and grid[i-1][j] == '1' and (i-1,j) not in visited:
                    queue.append((i-1,j))
                    visited.add((i-1, j))
                if i + 1 < rows and grid[i+1][j] == '1' and (i+1,j) not in visited:
                    queue.append((i+1,j))
                    visited.add((i+1, j))
                if j - 1 >= 0 and grid[i][j-1] == '1' and (i,j-1) not in visited:
                    queue.append((i,j-1))
                    visited.add((i, j-1))
                if j + 1 < cols and grid[i][j+1] == '1' and (i,j+1) not in visited:
                    queue.append((i,j+1))
                    visited.add((i, j+1))
        
        
        
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == '1' and (r,c) not in visited):
                    island+=1
                    bfs(r,c)

        return island        
        
        
        # =============== DFS =====================
        # rows = len(grid)
        # cols = len(grid[0])

        # island = 0

        # def dfs(r, c):
        #     if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
        #         return
            
        #     grid[r][c] = '0'

        #     dfs(r-1,c)
        #     dfs(r+1,c)
        #     dfs(r, c-1)
        #     dfs(r, c+1)

        # for r in range(rows):
        #     for c in range(cols):
        #         if (grid[r][c] == '1'):
        #             island+=1
        #             dfs(r,c)
        
        # return island