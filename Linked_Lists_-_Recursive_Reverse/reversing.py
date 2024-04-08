"""
recursively reversing the linked list
"""

class Node(object):
    """
    Node class
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def reverse(head):
    """
    reverse linked list
    """
    head1, temp = head, None

    while head and head.next is not None:
        temp, head = head, head.next

    if temp:
        temp.next = None
        return Node(head.data, reverse(head1))

    return head1
