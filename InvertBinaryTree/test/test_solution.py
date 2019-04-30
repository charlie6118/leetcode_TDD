import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    root = TreeNode(4)
    root.right = TreeNode(7)
    root.left = TreeNode(2)
    print(root.val, root.left.val, root.right.val)
    s = [root]
    root.left, root.right = root.right, root.left
    s += root.left, root.right
    print(root.val, root.left.val, root.right.val)
    assert False