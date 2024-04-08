"""
swaps every pair
"""
class Node:
    """
    node class
    """
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """
    swaps pairs
    """
    if head is None or head.next is None:
        return head

    head1 = head.next
    previous = None

    while head and head.next is not None:
        next_head1 = head.next
        head.next = head.next.next
        next_head1.next = head
        if previous:
            previous.next = next_head1
        previous = head

        head = head.next

    return head1
