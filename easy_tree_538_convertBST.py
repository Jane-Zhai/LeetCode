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

class Solution(object):
    def __init__(self):
        self.per = 0
    def convertBST(self, root):
        """
        给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        self.convertBST(root.right)
        root.val += self.per
        print(root.val)
        self.per = root.val
        print(self.per)
        self.convertBST(root.left)
        return root

if __name__ == "__main__":
    t = [5,3,7,1,4,6,8]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])

    sol = Solution()
    print(sol.convertBST(tt.root))           
         