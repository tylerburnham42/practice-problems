# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/solution/
# Solved 6-2-2022

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        down = True
        emptied = False
        y = 0
        out_matrix = []
        
        if len(matrix) == 1:
            return matrix[0]
        
        while matrix:
            #print(matrix)
            #print(out_matrix, y)
            if len(matrix) == 1:
                #print("LENGTH IS ONE")
                if down:
                    out_matrix.extend(matrix[0][::-1])
                else:
                    out_matrix.extend(matrix[0])
                break
                                      
            if y == 0 and not emptied:
                #print("First Row")
                out_matrix.extend(matrix[0])
                del matrix[0]
                down = True
                emptied = True
            elif y == len(matrix) -1 and not emptied:
                #print("Last Row")
                out_matrix.extend(matrix[y][::-1])
                del matrix[y]
                down = False
                y -= 1
                emptied = True
            else:
                #print("Direction:", down, " Y:", y)
                
                if down:
                    out_matrix.append(matrix[y].pop(-1))
                else:
                    out_matrix.append(matrix[y].pop(0))
                if not len(matrix[y]):
                    del matrix[y]
                    if y > len(matrix) -1:
                        y = len(matrix) -1
                else:
                    y += 1 if down else -1
                    emptied = False
                
        return out_matrix