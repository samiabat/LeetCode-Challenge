# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ff(n):
            if n in (None, p, q): return n
            l, r = ff(n.left), ff(n.right)
            if l and r: return n
            else: return l or r
        return ff(root)