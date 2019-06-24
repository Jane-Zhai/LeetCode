# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
        只有给定的树是单值二叉树时，才返回 true；否则返回 false。
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return None
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                if cur.left.val != cur.val:
                    return False
                else:
                    queue.append(cur.left)
            if cur.right:
                if cur.right.val != cur.val:
                    return False
                else:
                    queue.append(cur.right)
        return True