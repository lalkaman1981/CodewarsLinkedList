"""
slits one list into two smaller
"""

class Node(object):
    """
    node class
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    obj with two lists
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    alternatively splits
    """
    if head is None or head.next is None:
        return head

    first = None
    second = None
    counter = 0

    while head is not None:
        if counter % 2:
            if second:
                temp = second
                while second and second.next is not None:
                    second = second.next
                second.next = Node(head.data)
                second = temp
            else:
                second = Node(head.data)

        else:
            if first:
                temp = first
                while first.next is not None:
                    first = first.next
                first.next = Node(head.data)
                first = temp
            else:
                first = Node(head.data)

        head = head.next
        counter += 1

    return Context(first, second)
