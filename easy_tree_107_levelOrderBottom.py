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
    def levelOrderBottom(self, root):
        """
        给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        res = list()
        while queue:
            next_queue = list()
            layer = list()

            for node in queue:
                if node is not None:
                    if node.left is not None:
                        next_queue.append(node.left)                    
                    if node.right is not None:
                        next_queue.append(node.right)
                layer.append(node.val)
            queue = next_queue
            res.append(layer) 
        res.reverse()
        return res


class Solution2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [(root,0)]
        res = []
        while stack!=[]:
            node,level = stack.pop()
            if node:
                if len(res) < (level+1):
                    res.insert(0,[])
                res[-(level+1)].append(node.val)
                stack.append((node.right,level+1))
                stack.append((node.left,level+1))
        return res


if __name__ == "__main__":
    t = [1,2,2,3,None,None,3]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])
    sol = Solution()
    print(sol.levelOrderBottom(tt.root))
            
                    


