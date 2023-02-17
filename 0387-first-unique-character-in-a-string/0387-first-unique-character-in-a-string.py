class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict()
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
            
            
        for i in range(len(s)):
            if dic[s[i]]==1:
                return i
        return -1