from heapq import heapify, heappush, heappop 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]-=1
            else:
                dic[i]=-1
        l = []
        for i in dic:
            t = (dic[i], i)
            heappush(l, t)
        result = []
        for _ in range(k):
            result.append(heappop(l)[1])
        return result
            