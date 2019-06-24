"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
        :type root: Node
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            temp = []
            
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(temp)
        return result 


{"$id":"1","children":
    [{"$id":"2","children":
        [{"$id":"5","children":[],"val":5},
         {"$id":"6","children":[],"val":6}],
     "val":3},
     {"$id":"3","children":[],"val":2},
     {"$id":"4","children":[],"val":4}],
"val":1}