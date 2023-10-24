class Solution(object):
    def exist(self, board, wrd):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def solve(row,col,board,k,wrd):
            # if not safe
            if (row<0 )|( row>=len(board)): # out of the board
                return False
            if (col<0 )| (col>=len(board[0])): # out of the board
                return False
            if board[row][col] == '*' : # visited so cant go here
                return False
            if board[row][col] != wrd[k] : # next char in word not here
                return False
            # Base case 
            if k == len(wrd)-1:
                return True
            ch = board[row][col]
            # print(ch)
            # mark visited
            board[row][col] = '*'
            # traverse LRUD
            left = solve(row,col-1,board,k+1,wrd)
            # print('left : ',left)
            right = solve(row,col+1,board,k+1,wrd)
            # print('right : ',right)
            up = solve(row-1,col,board,k+1,wrd)
            # print('up : ',up)
            down = solve(row+1,col,board,k+1,wrd)
            # print('down : ',down)
            # backtrack
            board[row][col] = ch
            return left|right|up|down

        for i in range(len(board)):
            for j in range(len(board[0])):
                if solve(i,j,board,0,wrd):
                    return True
        return False