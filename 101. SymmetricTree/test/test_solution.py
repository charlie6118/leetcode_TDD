import pytest
from src.solution import Solution, TreeNode

s = Solution()

def test_case0():
    tree = TreeNode(1)
    assert s.isSymmetric(tree) == True

def test_case1():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    assert s.isSymmetric(tree) == False

def test_case2():
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    assert s.isSymmetric(tree) == False

def test_case3():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    assert s.isSymmetric(tree) == False