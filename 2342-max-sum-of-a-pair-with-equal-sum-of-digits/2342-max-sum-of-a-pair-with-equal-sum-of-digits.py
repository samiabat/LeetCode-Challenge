class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def dgsum(digit):
            ans = 0
            while digit:
                ans+=digit%10
                digit = digit//10
            return ans
        arr2 = [(dgsum(nums[i]), nums[i], i ) for i in range(len(nums))]
        arr2.sort()
        print(arr2)
        ans = -1
        for i in range(len(arr2)-1):
            if arr2[i][0]==arr2[i+1][0]:
                p1 = arr2[i][2]
                p2 = arr2[i+1][2]
                ans = max(ans, nums[p1] + nums[p2])
        return ans
                
            
            