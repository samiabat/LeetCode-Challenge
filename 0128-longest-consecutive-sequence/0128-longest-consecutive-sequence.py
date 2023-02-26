class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        root = {num:num for num in nums}
        size = {num:1 for num in nums}
        if not nums:
            return 0
        def f(x):
            if x == root[x]:
                return x
            root[x] = f(root[x])
            return root[x]
        
        def u(a, b):
            ap = f(a)
            bp = f(b)
            
            if (ap != bp):
                if size[ap] > size[bp]:
                    size[ap] += size[bp]
                    root[bp] = ap
                else:
                    size[bp] += size[ap]
                    root[ap] = bp
        visit = set()
        for num in nums:
            if num-1 in visit:
                u(num, num-1)
            if num+1 in visit:
                u(num, num+1)
            visit.add(num)
        return max(size.values())