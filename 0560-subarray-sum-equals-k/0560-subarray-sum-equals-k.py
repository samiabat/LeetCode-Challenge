class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cntr = Counter()
        cntr[0] = 1
        left = 0
        ans = 0
        for num in nums:
            left += num
            cntr[left] += 1
            if left - k in cntr: 
                if k == 0: ans += (cntr[left - k] - 1)
                else: ans += cntr[left - k]
        return ans
                
            