class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        tot = 0
        see=Counter()
        see[0] = 1
        for i in nums:
            tot+=i
            diff=tot-k
            counter+=see[diff]
            see[tot]+=1
        return counter
                
            