from heapq import heappush, heappop
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heap = []
        for i in points:
            heappush(heap, [i[1], i[0]])
        count = 0
        while heap:
            top = heappop(heap)[0]
            count+=1
            while heap and top>=heap[0][1] and top<=heap[0][0]:
                heappop(heap)
        return count
                