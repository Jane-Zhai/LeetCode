# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值"""
    def minDiffInBST(self, root):
        # BST中序遍历为升序的性质解题。
        def inorder(node):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        res = 999999
        l = inorder(root)
        for i in range(1,len(l)):
            res = min(res,l[i] - l[i-1])
        return res