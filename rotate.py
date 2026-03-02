class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head
    
    # 1. Compute length and find the actual tail
    last_node = head
    length = 1
    while last_node.next:
        last_node = last_node.next
        length += 1
    
    # 2. Adjust k (if k > length)
    k = k % length
    if k == 0:
        return head
    
    # 3. Connect tail to head to form a circle
    last_node.next = head
    
    # 4. Find the new tail: (length - k - 1) steps from head
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    
    # 5. Set the new head and break the circle
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head
