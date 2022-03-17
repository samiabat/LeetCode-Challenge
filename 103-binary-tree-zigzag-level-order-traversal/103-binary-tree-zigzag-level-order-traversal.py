from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        ans=[]
        count = 0
        while que:
            temp = []
            size = len(que)
            for i in range(size):
                top = que.popleft()
                temp.append(top.val)
                if top:
                    if top.right:
                        que.append(top.right)
                    if top.left:
                        que.append(top.left)
            if count==0:
                temp = temp[::-1]
            ans.append(temp)
            if count==0:
                count = 1
            else:
                count=0
        return ans
            
            