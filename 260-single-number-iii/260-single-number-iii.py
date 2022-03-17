class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        arr = []
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]==1:
                arr.append(i)
        return arr