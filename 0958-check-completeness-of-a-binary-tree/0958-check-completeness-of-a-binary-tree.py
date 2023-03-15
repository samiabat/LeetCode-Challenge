# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Check if the tree is empty
        if root is None:
            return True

        # Create an empty queue and enqueue the root node
        queue = []
        queue.append(root)
        is_leaf_node = False

        # Loop through the queue until it is empty
        while len(queue) > 0:
            # Dequeue a node from the queue
            node = queue.pop(0)

            # Check if the left child of the dequeued node is None
            if node.left is None:
                is_leaf_node = True
            else:
                # If the left child of the dequeued node is not None
                # and we have encountered a leaf node previously,
                # the tree is not complete
                if is_leaf_node:
                    return False
                # Enqueue the left child of the dequeued node
                queue.append(node.left)

            # Check if the right child of the dequeued node is None
            if node.right is None:
                is_leaf_node = True
            else:
                # If the right child of the dequeued node is not None
                # and we have encountered a leaf node previously,
                # the tree is not complete
                if is_leaf_node:
                    return False
                # Enqueue the right child of the dequeued node
                queue.append(node.right)

        # If we have traversed all the nodes in the queue
        # and haven't found any violation of completeness,
        # the tree is complete
        return True
