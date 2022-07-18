class Solution:
    def countAndSay(self, n: int) -> str:
        def count(nums):
            size = 0
            letter = ""
            ans = ""
            for i in nums:
                if not letter or letter==i:
                    size+=1
                    letter = i
                else:
                    ans+=str(size) + letter
                    size = 1
                    letter = i
            if not ans or ans[-1] != letter:
                ans+=str(size) + letter
            return ans
        def rec(s, ans, n):
            if n<2:
                return ans
            ans = count(ans)
            return rec(ans, ans, n-1)
        return rec("1", "1", n)