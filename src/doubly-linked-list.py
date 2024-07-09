class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
            return
        
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    
    def prepend(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node

    
    def delete_node(self, val):
        if self.head is None:
            return
        
        curr = self.head
        while(curr):
            if curr.val == val:
                if(curr == self.head):
                    self.head = self.head.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                if curr.prev is not None:
                    curr.prev.next = curr.next
                curr = None
                return
            curr = curr.next
        
        node = None

    def print_list(self):
        curr = self.head
        while(curr):
            print(curr.val, end="")
            curr = curr.next
        print()

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

dll.print_list()
dll.delete_node(4)
dll.print_list()
                    