# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        c = False
        if root.val==subRoot.val:
            c = self.do(root, subRoot)
        if c:
            return c
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree (root.right, subRoot)
    def do(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val==q.val:
            return self.do(p.left, q.left) and self.do(p.right, q.right)
        else:
            return False