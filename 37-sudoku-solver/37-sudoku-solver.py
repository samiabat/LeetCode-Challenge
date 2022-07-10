class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:  
        def isSafe(self,board,row,col,number):
            for i in range(len(board)):
                if (board[i][col]==str(number)):
                    return False
                if (board[row][i]==str(number)):
                    return False
            sr = int((row/3))*3
            sc = int((col/3))*3
            for i in range(sr,sr+3,1):
                for j in range(sc,sc+3,1):
                    if board[i][j]==str(number):
                        return False
            return True
        def helper(self,board,row,col):
            if row==len(board):
                return True
            nrow=0
            ncol=0
            if(col!=len(board)-1):
                nrow=row
                ncol=col+1
            else:
                nrow=row+1
                ncol=0
            if (board[row][col] != '.'):
                if helper(self,board,nrow,ncol):
                    return True
            else:
                for i in range(1,10):
                    if (isSafe(self,board,row,col,i)):
                        board[row][col] = str(i)
                        if helper(self,board,nrow,ncol):
                            return True
                        else:
                            board[row][col]='.'
            return False
        helper(self,board,0,0)