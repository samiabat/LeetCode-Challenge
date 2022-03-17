# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root, level):
            if not root:
                return level
            left = helper(root.left, level)
            right = helper(root.right, level)
            return 1 + max(left, right)
        return helper(root, 0)