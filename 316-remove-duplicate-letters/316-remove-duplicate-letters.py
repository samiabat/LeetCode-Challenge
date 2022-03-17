class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        l = list(s)
        dic = {}
        for i in l:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        stack = []
        for i in range(len(l)):
            while stack and l[i] not in stack and stack[-1]>=l[i] and dic[stack[-1]]>=1:
                stack.pop()
            if l[i] not in stack:
                stack.append(l[i])
                dic[stack[-1]]-=1
            else:
                dic[l[i]]-=1
        return "".join(stack)
        