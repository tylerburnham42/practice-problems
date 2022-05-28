# 1267. Count Servers that Communicate
# https://leetcode.com/problems/count-servers-that-communicate/
# Solved 5-28-2022

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        #Do the rows
        row_set = set()
        for y in range(len(grid)):
            total = sum(grid[y])
            if total >= 2:
                count += total
                for x in range(len(grid[0])):
                    if grid[y][x] == 1:
                        row_set.add(x)
                grid[y] = [0] * len(grid[y])
            
        
        #print(count, grid)
        #print(row_set)

        #Do the columns
        tmp = []
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                tmp.append(grid[y][x])
            
            total = sum(tmp)
            #print(tmp, total)
            if total >= 2 or x in row_set:
                count += total
            tmp = []
        
        #print(count, grid)
        return count