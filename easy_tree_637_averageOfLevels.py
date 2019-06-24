class TreeNode(object):
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

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        queue = [root]
        while queue:
            next_queue = []
            item = []
            for node in queue:
                if node:
                    item.append(node.val)
                    next_queue.append(node.left)
                    next_queue.append(node.right)
            if item:
                res.append(sum(item)/len(item))
            queue = next_queue
        return res


if __name__ == "__main__":
    t = [1,2,2,3,4,5,3]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])
    
    sol = Solution()
    print(sol.averageOfLevels(tt.root))