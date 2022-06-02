# 1275. Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        tt_board = [[None]*3,[None]*3,[None]*3]
        
        is_x = True
        for x, y in moves:
            tt_board[y][x] =  1 if is_x else 0
            is_x = not is_x

        could_be_incomplete = False
        # Check rows
        for row in tt_board:
            try:
                if sum(row) == 3:
                    return "A"
                if sum(row) == 0:
                    return "B"
            except:
                could_be_incomplete = True
        
        for x in range(len(tt_board)):
            col = set()
            for y in range(len(tt_board[0])):
                col.add(tt_board[y][x])
            #print(col)
            if len(col) == 1:
                if 1 in col:
                    return "A"
                if 0 in col:
                    return "B"
                
        left = set()
        right = set()
        for i in range(3):   
            left.add(tt_board[i][i])
            right.add(tt_board[i][abs(2-i)])

        print(tt_board)
        #print(left)
        if len(left) == 1:
            if 1 in left:
                return "A"
            if 0 in left:
                return "B"
            
        #print(right)
        if len(right) == 1:
            if 1 in right:
                return "A"
            if 0 in right:
                return "B"
        
        if could_be_incomplete:
            return "Pending"
        else:
            return "Draw"