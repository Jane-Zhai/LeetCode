class Node:
    def __init__(self, node=None):
        self.val = node
        self.next = None


class MyLinkedList(object):

    def __init__(self,node=None):
        """
        Initialize your data structure here.
        """
        self.__head = node
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur = self.__head
        count = 0
        while cur:          
            if count == index:
                return cur.val
            cur = cur.next
            count += 1
        return -1
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next = self.__head
        self.__head = node
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.__head is None:
            self.__head = Node(val)
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        
        if index == 0:
            self.addAtHead(val)
        else:
            cur = self.__head
            count = 1
            node = Node(val)
            while cur.next:
                if count == index: 
                    node.next = cur.next
                    cur.next = node
                    return
                cur = cur.next
                count += 1
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index == 0:
            self.__head = self.__head.next
        else:
            cur = self.__head
            count = 1
            while cur.next:
                if count == index:
                    cur.next = cur.next.next
                    return
                cur = cur.next
                count += 1

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.val, end=" ")
            cur = cur.next
        print("")


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

obj = MyLinkedList()
print(obj.get(2))
obj.addAtHead(1)
obj.travel()
obj.addAtTail(3)
obj.travel()
obj.addAtIndex(1,2)
obj.travel()
obj.deleteAtIndex(1)
obj.travel()