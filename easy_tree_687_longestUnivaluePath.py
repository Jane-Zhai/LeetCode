# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxl = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root,val):
            if root is None:
                return 0
            left = depth(root.left,root.val)
            right = depth(root.right,root.val)
            self.maxl = max(self.maxl, left+right)
            if (val == root.val):
                return max(left,right)+1
            return 0
        
        depth(root,root.val)
        return self.maxl