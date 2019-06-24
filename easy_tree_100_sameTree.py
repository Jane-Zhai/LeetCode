class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self,item):
        node = TreeNode(item)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.val, end = " ")
        self.preorder(node.left)
        self.preorder(node.right)


class Solution:
    def isSamTress(self,p,q):
        """
        如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
        """
        while p and q:
            if p.val==q.val and self.isSamTress(p.left,q.left) and self.isSamTress(p.right,q.right):
                return True
            else:
                return False
        return p is q


class Solution2:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    p = [1,3]
    q = [1,3]
    pp = Tree()
    qq = Tree()
    for i in range(len(p)):
        pp.add(p[i])
    for i in range(len(q)):
        qq.add(q[i])

    pp.preorder(pp.root)
    print(" ")
    qq.preorder(qq.root)
    print(" ")


    sol = Solution()
    print(sol.isSamTress(pp.root,qq.root))



