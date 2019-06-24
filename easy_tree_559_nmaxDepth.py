"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return None
        level_size = 1
        height = 0
        queue = [root]
        while queue:
            cur = queue.pop(0)
            level_size -= 1
            if cur.children:
                queue.extend(cur.children)
            if level_size == 0:
                height += 1
                level_size = len(queue)
        return height
        

class Solution(object):
    def maxDepth(self, root):
        return self.height(root)
    def height(self,node):
        if node is None:
            return 0
        depth = 0
        for i in node.children:
            depth = max(self.height(i), depth)
        return 1+depth