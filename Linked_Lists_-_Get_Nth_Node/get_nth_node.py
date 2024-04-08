"""
get node by index
"""
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    gives el by its index
    """

    if not node:
        raise IndexError

    if index == 0:
        return node

    counter = 0
    data = node.data

    while data and counter != index:
        node = node.next
        data = node.data
        counter += 1

    if counter == index and data is not None:
        return node
    raise IndexError
