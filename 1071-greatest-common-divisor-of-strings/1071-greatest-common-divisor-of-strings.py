class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        for i in range(len(str2)):
            if (not len(str2)% (i + 1) and not len(str1) %(i + 1)):
                div = len(str2) // (i + 1)
                cur = str2[:i+1]
                if cur * div != str2: 
                    continue
                div = len(str1) // (i + 1)
                if cur * div != str1:
                    continue
                ans = cur
                
        return ans
                