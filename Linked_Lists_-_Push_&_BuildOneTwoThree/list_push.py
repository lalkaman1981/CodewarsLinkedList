"""
push and one_two_three
"""

class Node:
    """
    node class
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(data, head):
    """
    pushes
    """
    return Node(head, data)

def build_one_two_three():
    """
    builds one-two-three linked array
    """
    return Node(1, Node(2, Node(3)))
