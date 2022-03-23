# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        q = deque()
        q.append(root)
        ans = []
        while q:
            size = len(q)
            maxi = float("-inf")
            for i in range(size):
                top = q.popleft()
                if top.val>maxi:
                    maxi = top.val
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            ans.append(maxi)
        return ans
                