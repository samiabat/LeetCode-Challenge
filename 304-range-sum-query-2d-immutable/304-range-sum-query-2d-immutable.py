class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.ans = self.matrix
        self.psa = []
        self.calculate()
    def prefixSum2D(self, matrix) :
        R,C = len(matrix),len(matrix[0])
        self.psa = [[0 for x in range(C)] for y in range(R)]
        self.psa[0][0] = matrix[0][0]
        for i in range(1, C) :
            self.psa[0][i] = (self.psa[0][i - 1] +matrix[0][i])
        for i in range(0, R) :
            if i:
                self.psa[i][0] = (self.psa[i - 1][0] +matrix[i][0])
            else:
                self.psa[i][0] = matrix[i][0]
        for i in range(1, R) :
            for j in range(1, C) :
                self.psa[i][j] = (self.psa[i - 1][j] +self.psa[i][j - 1] -self.psa[i - 1][j - 1] +matrix[i][j])
    def calculate(self):
        self.prefixSum2D(self.matrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.psa[row2][col2]
        elif col1==0:
            return self.psa[row2][col2] - self.psa[row1-1][col2]
        elif row1 == 0:
            return self.psa[row2][col2] - self.psa[row2][col1-1]
        return self.psa[row2][col2] - self.psa[row1-1][col2]-self.psa[row2][col1-1] + self.psa[row1-1][col1-1]
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)