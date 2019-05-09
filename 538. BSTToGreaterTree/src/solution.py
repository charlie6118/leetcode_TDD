# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(self, root, acc):
        if root:
            root.val += self.traverse(root.right, acc)
            return self.traverse(root.left, root.val)
        else:
            return acc
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.traverse(root, 0)
        return root
                