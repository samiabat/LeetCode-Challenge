# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = []
        tot = 0
        stack.append(root)
        while stack:
            val = stack.pop()
            if val.left:
                stack.append(val.left)
                if val.val%2==0:
                    tr = val.left.left
                    if tr:
                        tot+=tr.val
                    tr = val.left.right
                    if tr:
                        tot+=tr.val
            if val.right:
                stack.append(val.right)
                if val.val%2==0:
                    tr = val.right.right
                    if tr:
                        tot+=tr.val
                    tr = val.right.left
                    if tr:
                        tot+=tr.val
        return tot
            
            
        