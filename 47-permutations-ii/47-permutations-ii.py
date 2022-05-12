class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        dic = Counter(nums)
        def backTrak(res = []):
            if len(res)==len(nums):
                ans.append(res)
            for key in dic:
                if dic[key]:
                    dic[key]-=1
                    backTrak(res + [key])
                    dic[key]+=1
        backTrak()
        return ans