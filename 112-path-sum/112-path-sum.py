# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum)
    def dfs(self,node, targetSum):
        if not node:
            return False
        if node.right==None and node.left==None and targetSum==node.val:
            return True
        return self.dfs(node.right, targetSum-node.val) or self.dfs(node.left, targetSum-node.val)
            