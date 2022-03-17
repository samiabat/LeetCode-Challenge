# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        if not root:
            return arr
        if root.left:
            arr.extend(self.postorderTraversal(root.left))
        if root.right:
            arr.extend(self.postorderTraversal(root.right))
        arr.append(root.val)
        return arr