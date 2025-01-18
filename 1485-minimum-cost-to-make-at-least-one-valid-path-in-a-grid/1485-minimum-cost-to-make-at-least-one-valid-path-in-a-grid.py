from collections import deque

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        n, m = len(grid), len(grid[0])
        
        cost = [[float('inf')] * m for _ in range(n)]
        cost[0][0] = 0
        
        q = deque([(0, 0)])
        
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        while q:
            i, j = q.popleft()
                        
            cur_direction = grid[i][j]
            cur_cost = cost[i][j]
            
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < n and 0 <= nj < m:
                    new_cost = cur_cost + (0 if (di, dj) == directions[cur_direction] else 1)
                    
                    if new_cost < cost[ni][nj]:
                        cost[ni][nj] = new_cost
                        q.append((ni, nj))
        
        return cost[n-1][m-1]
