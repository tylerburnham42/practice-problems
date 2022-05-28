# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# DFS Soultion

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        x = 0
        y = 0
        island_count = 0
        while y < len(grid) and x < len(grid[0]):
            if grid[y][x] == '1':
                island_count += 1
                self.findIsland(grid, x, y)
                #print(" ".join([f"{x} \n" for x in grid]))
            
            if x == len(grid[0]) -1:
                x = 0
                y += 1
            else:
                x += 1
            

        
        return island_count
        
        
    def findIsland(self, grid, x, y):
        
        if y < 0 or y > len(grid)-1 or x < 0 or x > len(grid[0])-1 or grid[y][x] == '0':
            return

        grid[y][x] = '0'

        self.findIsland(grid, x-1, y)
        self.findIsland(grid, x+1, y)
        self.findIsland(grid, x, y-1)
        self.findIsland(grid, x, y+1)