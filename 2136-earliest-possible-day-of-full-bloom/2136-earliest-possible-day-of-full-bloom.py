class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        pair = list(zip(plantTime, growTime))
        pair.sort(key=lambda x: x[1], reverse=True)
        ans, day = 0, 0
        for i in range(len(pair)):
            day += pair[i][0]
            ans = max(ans, day + pair[i][1])
        return ans
        
        
        
        
        