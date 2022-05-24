# Reshape the Matrix #566
# https://leetcode.com/problems/reshape-the-matrix/
# Solved 5-22-2022
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        r_counter = 1
        c_counter = 0
        out_row = []
        output = []
        
        for row in mat:
            for num in row:
                #print(out_row, output, r_counter, c_counter)
                if c_counter < c:
                    c_counter += 1
                    out_row.append(num)
                else:
                    r_counter += 1
                    c_counter = 1
                    output.append(out_row)
                    out_row = [num]

        if(len(out_row) != 0):
            output.append(out_row)
        
        #print("end", out_row, output, r_counter, c_counter)
        if (r_counter != r or c_counter != c):
            return mat
                    
        return output