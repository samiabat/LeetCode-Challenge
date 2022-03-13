from heapq import heapify, heappop, heappush
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = []
        for i in matrix:
            for j in i:
                n.append(j)
        n = sorted(n)
        return n[k-1]