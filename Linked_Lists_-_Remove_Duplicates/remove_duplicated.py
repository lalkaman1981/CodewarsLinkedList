"""
removes duplicates
"""

class Node(object):
    """
    node class
    """
    def __init__(self, data = None):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    remover duplicates
    """
    head1 = head

    while head and head.next is not None:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next

    return head1
