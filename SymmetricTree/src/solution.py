# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def leftTraverse(root):
            leftT = []
            if root:
                leftT.append(root.val)
                leftT = leftT + leftTraverse(root.left)
                leftT = leftT + leftTraverse(root.right)
            else:
                leftT.append(None)
            return leftT

        def rightTraverse(root):
            righT = []
            if root:
                righT.append(root.val)
                righT = righT + rightTraverse(root.right)
                righT = righT + rightTraverse(root.left)
            else:
                righT.append(None)
            return righT

        return leftTraverse(root) == rightTraverse(root)