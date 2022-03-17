# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        
        while q:
            size = len(q)
            arr = []
            for i in range(size):
                top = q.popleft()
                arr.append(top.val)
                if top.right:
                    q.append(top.right)
                if top.left:
                    q.append(top.left)
            ans.append(arr)
        mels = []
        for i in ans[::-1]:
            mels.append(i[::-1])
        return mels
            