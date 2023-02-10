class Solution(object):
    def largestOverlap(self, A, B):
        oneA, oneB = [], []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    oneA.append([i, j])
                if B[i][j] == 1:
                    oneB.append([i, j])
        
        maxOverlap = 0
        vectorOverlap = defaultdict(int)
        for coordA in oneA:
            for coordB in oneB:
                vector = (coordB[0] - coordA[0], coordA[1] - coordB[1])
                vectorOverlap[vector] += 1
                maxOverlap = max(maxOverlap, vectorOverlap[vector])
        
        return maxOverlap