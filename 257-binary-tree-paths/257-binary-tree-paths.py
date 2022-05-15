# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def bt(r, temp = []):
            if temp and not r:
                ans.append(temp)
                return
            if not r:
                return
            if not r.left and not r.right:
                bt(r.left, temp + ["->", str(r.val)])
            if r.left:
                bt(r.left, temp+ ["->", str(r.val)])
            if r.right:
                bt(r.right, temp+ ["->", str(r.val)])
        bt(root)
        fin = []
        for i in ans:
            fin.append("".join(i[1:]))
        return fin