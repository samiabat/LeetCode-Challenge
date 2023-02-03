class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = list(s)
        one = []
        while left < right:
            if s[left] != s[right]:
                one = s.copy()
                two = s.copy()
                one.pop(left)
                two.pop(right)
                break
            left += 1
            right -= 1
        return one == one[::-1] or two == two[::-1] or s == s[::-1]
                