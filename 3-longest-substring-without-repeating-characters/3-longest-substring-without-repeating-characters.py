class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        for i in range(len(s)):
            stack = []
            while i<len(s) and s[i] not in stack:
                stack.append(s[i])
                i+=1
            if len(stack)>best:
                best = len(stack)
        return best
        