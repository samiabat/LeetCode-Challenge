class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return sorted(set(nums))[-3] if len(sorted(set(nums))) >= 3 else max(nums) 