class ListNode:
    def __init__(self, node = None):
        self.val = node
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        编写一个程序，找到两个单链表相交的起始节点。
        """
        curA = headA
        curB = headB
        while curA:
            while curB:
                if curA.next==curB.next:
                    print("Reference of the node with value = %d" % curB.next.val)
                    return
                # print(curB.val)
                curB = curB.next  
            # print("A",curA.val) 
            curA = curA.next
            curB = headB
            

class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        判断链表是否有交集，可以设置两个指针，一个指针从第一个链表开始遍历，
        遍历完第一个链表再遍历第二个链表，另一个指针从第二个链表开始遍历，
        遍历完第二个链表再遍历第一个链表，不管两个链表在交集前的长度如何，
        如果有交集的话，两个指针肯定会同时遍历到最后的交集部分。
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa is not pb: 
            pa = headB if pa == None else pa.next
            pb = headA if pb == None else pb.next           
        return pa


anode1 = ListNode(4)
anode2 = ListNode(1)
bnode1 = ListNode(5)
bnode2 = ListNode(0)
bnode3 = ListNode(1)
node1 = ListNode(8)
node2 = ListNode(4)
node3 = ListNode(5)
anode1.next = anode2
anode2.next = node1
bnode1.next = bnode2
bnode2.next = bnode3
bnode3.next = node1
node1.next = node2
node2.next = node3

res = Solution2().getIntersectionNode(anode1,bnode1)