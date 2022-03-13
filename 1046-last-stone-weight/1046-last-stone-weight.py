from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        heapify(stones)
        while len(stones)>1:
            v1 = -1*heappop(stones)
            v2 = -1*heappop(stones)
            if v1!=v2:
                new = v2-v1
                heappush(stones, new)
        if len(stones)==0:
            return 0
        return -1*stones[0]