class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        dic = Counter(changed)
        ans = []
        visited = set()
        for num in changed:
            cur = num*2
            if cur in dic and dic[cur] and dic[num]:
                dic[cur]-=1
                dic[num]-=1
                ans.append(num)
        for key in dic:
            if dic[key]:
                return []
        return ans
                
                
            
            