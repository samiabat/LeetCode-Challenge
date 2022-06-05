class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negDiag = set() ## row - column is constant
        posDiag = set() ## row + column is constant
        
        board = [['.']*n for _ in range(n)]
        ans = 0
        
        def backtrack(r):
            nonlocal ans
            if r == n:
                ans += 1
                return
            for c in range(n):
                if c not in col and (r+c) not in posDiag and (r-c) not in negDiag:
                    col.add(c)
                    negDiag.add(r-c)
                    posDiag.add(r+c)
                    board[r][c] = 'Q'
                    
                    backtrack(r+1)
                    
                    col.remove(c)
                    negDiag.remove(r-c)
                    posDiag.remove(r+c)
                    board[r][c] = '.'
        
        backtrack(0)
        return ans