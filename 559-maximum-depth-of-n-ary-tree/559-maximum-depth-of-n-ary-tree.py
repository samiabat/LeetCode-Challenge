"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.dfs(root)
    def dfs(self, node:'Node', value = 0):
        if not node:
            return value
        if not node.children:
            return value+1
        arr = []
        for i in range(len(node.children)):
            arr.append(self.dfs(node.children[i], value+1))
        return max(arr)
            
        