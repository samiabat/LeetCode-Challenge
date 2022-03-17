# Definition for a binary tree node.
# from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = None
        self.max_depth = 0
        
    def traversal(self, node, cur_depth):
        if not node:
            return cur_depth
        
        l_depth = self.traversal(node.left, cur_depth + 1)
        r_depth = self.traversal(node.right, cur_depth + 1)
        
        self.max_depth = max(self.max_depth, l_depth, r_depth)

        if l_depth == r_depth == self.max_depth:
            self.res = node
        
        return max(l_depth, r_depth)
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root, 0)
        
        return self.res

