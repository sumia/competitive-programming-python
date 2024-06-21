# Detecting a Cycle
# Time - O(N)
# Space -> O(1)

# Linked list - fast/slow pointers
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return False 

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

# create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Link nodes to without cycle: 1 -> 2 -> 3 -> 4 
node1.next = node2
node2.next = node3
node3.next = node4
print(has_cycle(node1)) # False

# Link nodes to form cycle: 1 -> 1
node1.next = node1
print(has_cycle(node1)) # True

# Link nodes to form cycle: 1 -> 2 -> 3 -> 4 -> 2
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print(has_cycle(node1)) # True