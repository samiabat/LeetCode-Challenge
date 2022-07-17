class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(deque)
        for i in range(len(nums)):
            self.dic[nums[i]].append(i)
        print(self.dic)

    def pick(self, target: int) -> int:
        indx = self.dic[target][0]
        rm = self.dic[target].popleft()
        self.dic[target].append(rm)
        return indx


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)