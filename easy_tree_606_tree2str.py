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
    def tree2str(self, root):
        """
        :type t: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)
        resstr = str(root.val)
        if root.left:
            resstr += "(" + self.tree2str(root.left) + ")" 
        else:
            resstr += "()"
        if root.right:
            resstr += "(" + self.tree2str(root.right) + ")" 

        return resstr

if __name__ == "__main__":
    t = [1,2,2,3,4,5,3]
    tt = Tree()
    for i in range(len(t)):
        tt.add(t[i])
    
    sol = Solution()
    print(sol.tree2str(tt.root))