# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


# class Linklist():
#     def __init__(self, node=None):
#         self.__head = node

#     def list2Linklist(self, L):
#         self.__head = ListNode(L[0])
#         cur = self.__head
#         for i in L[1:]:
#             node = ListNode(i)
#             cur.next = node
#             cur = cur.next

#     def travel(self):
#         cur = self.__head
#         while cur != None:
#             print(cur.val, end=" ")
#             cur = cur.next
#         print("")


class Solution():
    def __init__(self, node=None):
        self.__head = node

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        将两个有序链表合并为一个新的有序链表并返回。
        新链表是通过拼接给定的两个链表的所有节点组成的。 
        """
        head = cur = ListNode(0)       
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next          
        cur.next = l1 or l2
        return head.next



if __name__ == "__main__":
    # l1data = [1,3,4]
    # l2data = [1,2,4]

    # l1 = Linklist()
    # l1.list2Linklist(l1data)
    # l1.travel()

    # l2 = Linklist()
    # l2.list2Linklist(l2data)
    # l2.travel()

    l1_root = ListNode(1)
    l1_node1 = ListNode(2)
    l1_node2 = ListNode(4)
    l1_root.next = l1_node1
    l1_node1.next = l1_node2

    l2_root = ListNode(1)
    l2_node1 = ListNode(3)
    l2_node2 = ListNode(4)
    l2_root.next = l2_node1
    l2_node1.next = l2_node2


    sol = Solution()
    res = sol.mergeTwoLists(l1_root,l2_root)
    while res:
        print(res.val)
        res = res.next