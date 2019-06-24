class TreeNode:
    def __init__(self,x):
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
    
    def traval(self, node):
        if node is None:
            return
        print(node.val, end=" ")
        self.traval(node.left)
        self.traval(node.right)


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 is None and t2 is None:
            return None
        if t1 and t2 is None:
            return t1
        if t2 and t1 is None:
            return t2
        t1.val = t1.val + t2.val
        print(t1.val)
        self.mergeTrees(t1.left,t2.left)
        self.mergeTrees(t1.right,t2.right)

        return t1


if __name__ == "__main__":
    p = [1,3]
    q = [1,3]
    pp = Tree()
    qq = Tree()
    for i in range(len(p)):
        pp.add(p[i])
    for i in range(len(q)):
        qq.add(q[i])


    sol = Solution()
    print(sol.mergeTrees(pp.root,qq.root))