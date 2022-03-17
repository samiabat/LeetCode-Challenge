# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return  True
        check = self.do(root.left, root.right)
        print(check)
        return check
    def do(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val==q.val:
            return self.do(p.left, q.right) and self.do(p.right, q.left)
        else:
            return False