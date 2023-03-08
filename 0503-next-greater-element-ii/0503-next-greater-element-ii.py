class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums;stack = [];ans = [-1] * (len(nums) // 2)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                if idx < len(nums) // 2:ans[idx] = nums[i]
            stack.append(i)
        return ans
        
                