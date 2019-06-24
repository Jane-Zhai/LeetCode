# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
        二叉搜索树保证具有唯一的值。
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return 0
        if root.val > R:
            return self.rangeSumBST(root.left,L,R)
        elif root.val < L:
            return self.rangeSumBST(root.right,L,R)
        else:
            return root.val + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)
        