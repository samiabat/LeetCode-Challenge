# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        if not root:
            return arr
        arr.append(root.val)
        if root.left:
            arr.extend(self.preorderTraversal(root.left))
        if root.right:
            arr.extend(self.preorderTraversal(root.right))
        return arr