# Cinema Seat Allocation #1386
# https://leetcode.com/problems/cinema-seat-allocation/submissions/
# Solved 5-25-2022

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reservedSeats.sort(key=lambda x :x[0])
        
        current_row = 1
        current_row_left = True
        current_row_right = True
        current_row_middle = True
        
        count = 0
        for row, col in reservedSeats:
            if current_row > row:
                continue
                
            elif row > current_row:
                count += self.getCout(current_row_left, current_row_right, current_row_middle)
                
                if row - current_row != 1:
                    count += 2 * (row - current_row - 1)
                    
                current_row = row
                current_row_left = True
                current_row_right = True
                current_row_middle = True

            if col in [2, 3, 4, 5]:
                current_row_left = False
            elif col in [6, 7, 8, 9]:
                current_row_right = False
            if col in [4, 5, 6, 7]:
                current_row_middle = False
                
            #print(row, col, current_row, [current_row_left, current_row_middle, current_row_right], count)
        
                
        if n+1 > current_row:
            count += self.getCout(current_row_left, current_row_right, current_row_middle)

            if n+1 - current_row != 1:
                count += 2 * (n+1 - current_row - 1)
                
        #print(row, col, current_row, [current_row_left, current_row_middle, current_row_right], count)
        
        
        return count
    
    def getCout(self, left: bool, right: bool, middle: bool) -> int:
        """
            Gets the count from the left right and middle
        """
        count = 0
        if left and right:
            count = 2
        elif middle or left or right:
            count = 1

        return count