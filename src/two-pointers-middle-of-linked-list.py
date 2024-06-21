# Finding the Middle of a Linked List
# Time - O(N)
# Space - O(1)

# Linked Lists - fast/slow pointers

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def find_middle(head):
    if not head:
        return None
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# link nodes - 1 -> 2 -> 3
node1.next = node2
node2.next = node3

middle_node = find_middle(node1)
print(middle_node.val if middle_node else "None") # returns 2

node3.next = node4
middle_node = find_middle(node1)
print(middle_node.val if middle_node else "None") # returns 3