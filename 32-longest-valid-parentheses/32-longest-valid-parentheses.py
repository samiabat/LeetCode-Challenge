class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stck=[-1] 
        for i in range(len(s)):
            if s[i] == '(':
                stck.append(i)
            else:
                stck.pop()
                if not stck:
                    stck.append(i)
                else:
                    max_length=max(max_length, i-stck[-1])
        return max_length
        