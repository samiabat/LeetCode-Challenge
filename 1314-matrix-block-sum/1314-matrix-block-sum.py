class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        '''
        1,2,3
        4,5,6
        7,8,9
        
        '''
        
        '''
        r = (max(0, i - k), min(i+k, len(mat)))
        c = (max(0, j - k), min(j+k, len(mat)))
        
        ''' 
        
        ans = [[0] * len(mat[0]) for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp = 0
                for r in range(max(0, i - k), min(i+k+1, len(mat))):
                    for c in range(max(0, j - k), min(j+k+1, len(mat[0]))):
                        temp += mat[r][c]
                ans[i][j] = temp
        return ans