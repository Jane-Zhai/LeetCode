# class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 注意这里是一个二叉搜索树，根结点的右子树上所有的点的值都比根结点大，左子树上所有点的值都比根结点的值小
        # 因此分为四种情况，
        # 1、如果两个节点一个值比节点大，一个小，那么二者的公共节点肯定是根结点，
        # 2、如果两个节点中有一个与根结点的值同样大，那么二者的公共节点同样是根结点
        # 3、如果两个节点的值都比根结点小，那么二者的公共节点出现在根结点的左子树中，递归查询
        # 4、如果两个节点的值都比根结点大，那么二者的公共节点出现在根结点的右子树中，递归查询
        
        if (p.val - root.val) * (q.val - root.val) <= 0:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
