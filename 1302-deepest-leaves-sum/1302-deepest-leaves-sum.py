# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            size = len(q)
            ans = 0
            for _ in range(size):
                top = q.popleft()
                ans+=top.val
                if top.right:
                    q.append(top.right)
                if top.left:
                    q.append(top.left)
        return ans
                