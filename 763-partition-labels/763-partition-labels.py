class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        ans = []
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]] = 1
        stack = []
        for i in s:
            dic[i]-=1
            stack.append(i)
            one = True
            for j in stack:
                if dic[j]>0:
                    one = False
                    break                    
            if one:
                ans.append(len(stack))
                stack = []
        return ans
                    
        