class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(maxsize=None)
        def move(curRow, curColumn, maxMove):
            if curRow<0 or curColumn<0 or curRow>=m or curColumn>=n:
                return 1
            if maxMove<=0:
                return 0
            return (move(curRow-1, curColumn, maxMove-1) + 
                    move(curRow+1, curColumn, maxMove-1) + 
                    move(curRow, curColumn-1, maxMove-1) + 
                    move(curRow, curColumn+1, maxMove-1) )
                    
        
        return move(startRow, startColumn, maxMove)%(10**9 + 7)