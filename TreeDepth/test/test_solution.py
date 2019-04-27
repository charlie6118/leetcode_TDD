import pytest
from src.solution import Solution, TreeNode

s = Solution()

def test_case0():
    tree = None
    assert s.maxDepth(tree) == 0

def test_case1():
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    assert s.maxDepth(tree) == 3