# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(root, acc):
            if root:
                traverse(root.left, acc)
                acc.append(root.val)
                traverse(root.right, acc)
        result = []
        traverse(root, result)
        return result