# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        ans = []
        while level:
            ans.append([i.val for i in level])
            newLevel = []
            for i in level:
                if i.left:
                    newLevel.append(i.left)
                if i.right:
                    newLevel.append(i.right)
                
            level = newLevel
        return ans
        