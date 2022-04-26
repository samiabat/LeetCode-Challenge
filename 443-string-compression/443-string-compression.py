class Solution:
    def compress(self, chars: List[str]) -> int:
        p1 = 0
        p2 = 0
        ans = ""
        while p2<len(chars):
            while p2<len(chars) and (chars[p1]==chars[p2]):
                p2+=1
            ans+=chars[p1]
            if p2-p1>1:
                ans+=str(p2-p1)
            p1 = p2
        for i in range(len(ans)):
            chars[i]=ans[i]
        return len(ans)