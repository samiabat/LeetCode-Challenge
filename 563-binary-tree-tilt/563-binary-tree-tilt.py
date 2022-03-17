# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        rootSum, rootTilt = self.dfs(root)
        return rootTilt
    
    def dfs(self, node):
        if not node:
            return 0, 0
        
        leftSum, leftTilt = self.dfs(node.left)
        rightSum, rightTilt = self.dfs(node.right)
        
        return node.val + leftSum + rightSum, abs(rightSum - leftSum) + leftTilt + rightTilt
    