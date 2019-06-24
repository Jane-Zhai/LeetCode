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
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        parent = {}
        depth = {}
        def dfs(node, par=None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left,node)
                dfs(node.right,node)
        dfs(root)
        return depth[x] == depth[y] and parent[x]!=parent[y]


if __name__ == "__main__":
    t = [1,2,3,4,5,6,7]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])
    sol = Solution()
    print(sol.isCousins(tt.root,4,6))