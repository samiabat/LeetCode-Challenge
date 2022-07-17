# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        ans = 0
        while q:
            size = len(q)
            ans+=1
            for i in range(size):
                top = q.popleft()
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                if not top.right and not top.left:
                    return ans
        return ans
        