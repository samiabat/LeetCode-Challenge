class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        sums=0
        see=Counter()
        see[0]=1
        for n in nums:
            sums+=n
            diff=sums-k
            c+=see[diff]
            see[sums]+=1
        print(see)
        return c
                
            