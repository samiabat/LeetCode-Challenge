from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque()
        
        que.append(root)
        ans=[]
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
            ans.append(sum(temp)/len(temp))
        return ans
            
            
            