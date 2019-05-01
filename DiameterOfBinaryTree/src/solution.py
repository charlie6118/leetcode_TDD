# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.numOfNodes = 1
        
    def getHeight(self, root):
        if not root:
            return 0
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        self.numOfNodes = max(self.numOfNodes, l + r + 1)
        return max(l, r) + 1
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.getHeight(root)
        return self.numOfNodes - 1
    