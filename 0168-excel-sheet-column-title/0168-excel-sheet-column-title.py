class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mp = {i: chr(i + ord('A')-1) for i in range(1, 27)}
        column = []
        while columnNumber > 26:
            column.append(mp[26 if columnNumber % 26 == 0 else columnNumber % 26])
            if columnNumber % 26 == 0:
                columnNumber = (columnNumber - 26) // 26
            else:
                columnNumber //= 26
        column.append(mp[columnNumber])
        
        return ''.join(column[::-1])