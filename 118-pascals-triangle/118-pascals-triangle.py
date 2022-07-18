class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        prev = [1]
        while len(ans)<numRows:
            temp = []
            temp.append(1)
            for i in range(len(prev)-1):
                temp.append(prev[i]+prev[i+1])
            temp.append(1)
            prev = temp
            ans.append(temp)
        return ans