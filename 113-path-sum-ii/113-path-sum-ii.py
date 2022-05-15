# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def bt(r, tar, temp = []):
            if tar == 0 and temp and not r:
                ans.append(temp)
                return
            if not r:
                return
            if not r.left and not r.right:
                bt(r.left, tar-r.val, temp+ [r.val])
            if r.left:
                bt(r.left, tar-r.val, temp+ [r.val])
            if r.right:
                bt(r.right, tar-r.val, temp + [r.val])
        bt(root, targetSum)
        return ans
        