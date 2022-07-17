# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        @lru_cache(maxsize=None)
        def dp(root):
            if not root.left and not root.right:
                return 1
            if not root.left:
                return  1+dp(root.right)
            if not root.right:
                return  1+dp(root.left)
            return min(1+dp(root.right), 1+dp(root.left))
        return dp(root)
        