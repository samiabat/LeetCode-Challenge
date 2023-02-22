class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = Counter()
        ans = 0
        
        for i in range(len(time)):
            rem = 60 - time[i] % 60
            if rem == 60:
                rem = 0
            if rem in cnt: 
                ans += cnt[rem]
            cnt[time[i]%60] += 1
        return ans
            