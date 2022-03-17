# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        if not root:
            return root
        if root.left:
            arr.extend(self.inorderTraversal(root.left))
        arr.append(root.val)      
        if root.right:
            arr.extend(self.inorderTraversal(root.right))  
        return arr