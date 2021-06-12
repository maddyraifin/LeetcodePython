# Reference: https://leetcode.com/problems/range-sum-of-bst/
# Sequence = 938. Range Sum of BST
# Prepared by - Maddy Rai
import time
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def searchInOrder(root, lsval):
        # Cannot iterate over root.val is not None
        if root:
            TreeNode.searchInOrder(root.left, lsval)
            lsval.append(root.val)
            TreeNode.searchInOrder(root.right, lsval)


class Solution:
    def rangeSumBST(self, root, low, high):
        lsval = []
        TreeNode.searchInOrder(root, lsval)

        if len(lsval) not in range(1, 2*104+1) or min(lsval) < 1 or max(lsval) > 105:
            raise Exception("Unexpected node inputs")

        if low not in range(1, 106) or high not in range(1, 106):
            raise Exception("Numbers not in range")

        if any(i > 1 for i in list(collections.Counter(lsval).values())):
            raise Exception("Atleast one node value exists more than once")

        # Low & High numbers should exist in the Binary Tree
        return sum(lsval[sorted(lsval).index(low):sorted(lsval).index(high)+1])


# Create and connect a Binary Search Tree
n1, n2, n3, n4, n5, n7 = TreeNode(10), TreeNode(5), TreeNode(15), TreeNode(3), TreeNode(7), TreeNode(18)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.right = n7

low = 7
high = 15

tic = time.perf_counter()
result = Solution.rangeSumBST(None, n1, low, high)
toc = time.perf_counter()
print(f"Time taken = {toc - tic:0.8f} seconds")
print(result)
