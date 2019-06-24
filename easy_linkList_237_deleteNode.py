# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # 这道题关键是理解题意，不给你整个链表，只给你一个节点，如何把这个节点删除，
        # 其实我们没必要真的把这个节点删除，而是把这个节点对应的val值删除即可，
        # 所以我们可以偷天换日，把下一个节点的值赋给这个节点，再把下一个节点删除。
        node.val = node.next.val
        node.next = node.next.next


bnode1 = ListNode(5)
bnode2 = ListNode(0)
bnode3 = ListNode(1)
node1 = ListNode(8)
node2 = ListNode(4)
node3 = ListNode(5)
bnode1.next = bnode2
bnode2.next = bnode3
bnode3.next = node1
node1.next = node2
node2.next = node3


Solution().deleteNode(node1)

cur = bnode1
while cur:
    print(cur.val, end=" ")
    cur = cur.next
print("")