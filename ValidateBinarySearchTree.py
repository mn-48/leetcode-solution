# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root,  mn = -float('inf'), mx = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return mn <= root.val < mx and self.isValidBST(root.left, mn, root.val) and self.isValidBST(root.right, root.val+1, mx)