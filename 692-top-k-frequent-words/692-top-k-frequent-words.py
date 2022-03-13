from heapq import heappop, heapify, heappush
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for word in words:
            if word in dic:
                dic[word]-=1
            else:
                dic[word]=-1
        l = []
        for i in dic:
            t = (dic[i], i)
            heappush(l, t)
        result = []
        for _ in range(k):
            result.append(heappop(l)[1])
        return result
        
        