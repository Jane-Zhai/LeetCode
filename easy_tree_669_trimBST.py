class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.val < L:
            return self.trimBST(root.right,L,R)
        if root.val > R:
            return self.trimBST(root.left,L,R)
        root.left = self.trimBST(root.left,L,root.val)
        root.right = self.trimBST(root.right,root.val,R)
        return root