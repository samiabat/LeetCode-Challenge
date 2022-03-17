class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_cap = max(weights)
        total_cap = sum(weights)
        lo, hi= max_cap, total_cap
        while lo < hi:
            assumed_cap = lo + (hi - lo) // 2
            total, res = 0, 1
            for w in weights:
                if total + w > assumed_cap:
                    res += 1
                    total = w
                else:
                    total += w

            if res <= days:
                hi = assumed_cap
            else:
                lo = assumed_cap + 1
        return hi