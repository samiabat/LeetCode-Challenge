class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        num = float('-inf')
        for n in nums[::-1]:
            if n < num:
                return True
            while stack and stack[-1] < n:
                num = stack.pop()
            stack.append(n)
        return False

            
            