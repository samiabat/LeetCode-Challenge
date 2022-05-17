# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        arr = []
        def bt(root, t, memo = {}):
            if not root:
                return False
            if root.val in memo:
                return memo[root.val]
            if root.val == t.val:
                arr.append(root)
                return True
            right = bt(root.right, t)
            left = bt(root.left, t)
            memo[root.val] = right or left
            return memo[root.val]
        bt(cloned, target)
        if arr:
            return arr[0]
        return 
            