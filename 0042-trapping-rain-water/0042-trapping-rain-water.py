class Solution:
    def trap(self, a: List[int]) -> int:
        l_ = 0;ok = 0;r_ = [0] * len(a);r_[-1] = a[-1]
        for i in range(len(a)-2, -1, -1):
            r_[i] = max(r_[i+1], a[i])
        for i in range(len(a)-1):
            if a[i] < l_ and a[i] < r_[i+1]:
                ok += min(l_, r_[i+1]) - a[i]
            l_ = max(a[i], l_)
        return ok
                
        
                