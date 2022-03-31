class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        dic = OrderedDict()
        l = 0
        r = 10
        while r<=len(s):
            k = s[l:r]
            if k in dic:
                dic[k]+=1
            else:
                dic[k] = 1
            l+=1
            r+=1
        for i in dic:
            if dic[i]>1:
                ans.append(i)
        return ans