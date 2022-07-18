class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        ans = [1]
        j = 1
        while j<=rowIndex:
            temp = []
            temp.append(1)
            for i in range(len(prev)-1):
                temp.append(prev[i]+prev[i+1])
            temp.append(1)
            prev = temp
            ans = temp 
            j+=1
        return ans
        
   