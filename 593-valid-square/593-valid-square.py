class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distcalc(a, b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2
        def check(tl, tr, bl, br):
            return (distcalc(tl, tr) == 
                    distcalc(bl, tl) == 
                    distcalc(bl, br) == 
                    distcalc(tr, br) and 
                    distcalc(bl, tr)== distcalc(tl, br) and distcalc(bl, tr) and distcalc(tl, br))
        arr = [tuple(p1), tuple(p2), tuple(p3), tuple(p4)]
        dic = Counter(arr)
        
        ans = False
        
        def rec(index, temp = []):
            nonlocal ans
            if len(temp)==4:
                tl, tr, bl, br = temp
                ans = ans or check(tl, tr, bl, br)
                return
            if index>=4:
                return
            for key in dic:
                if dic[key]:
                    dic[key]-=1
                    rec(index+1, temp+[key])
                    dic[key]+=1
        rec(0)
        return ans
        