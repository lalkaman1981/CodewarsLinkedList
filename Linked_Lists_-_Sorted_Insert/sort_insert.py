"""
sorted insert
"""

class Node(object):
    """
    node class
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """
    sorted insert
    """

    if not head:
        return Node(data)

    if data < head.data:
        data = Node(data)
        data.next = head
        return data

    head1 = head

    while True:
        if head.next is None or head.next.data > data:
            data = Node(data)
            data.next = head.next
            head.next = data
            break

        head = head.next

    return head1
