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
    def isSymmetric(self, root):
        """
        给定一个二叉树，检查它是否是镜像对称的。
        :type root: TreeNode
        :rtype: bool
        """
        # 递归
        def check(node1,node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left,node2.right) and check(node1.right,node2.left)

        return check(root,root)

class Solution2(object):
    def isSymmetric(self, root):        
        # 迭代--层序遍历
        queue = [root]
        while(queue):
            next_queue = list()
            layer = list()
            for node in queue:
                if node is None:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)

                layer.append(node.val)
            if layer != layer[::-1]:
                return False
            queue = next_queue

        return True
                  

if __name__ == "__main__":
    t = [1,2,2,3,4,5,3]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])
    
    tt.traval(tt.root)
    sol = Solution2()
    print(sol.isSymmetric(tt.root))