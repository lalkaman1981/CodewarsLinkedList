"""
finds a loop
"""
class Node:
    """
    class node
    """
    def __init__(self, next = None) -> None:
        self.next = next

def find_size(node):
    """
    finds loop size
    """
    node1 = node
    counter = 0

    while node1 is not None:
        counter += 1
        node1 = node1.next

        if node1 == node:
            return counter

def loop_size(node):
    """
    finds a loop
    """
    flash = node
    hulk = node

    while True:
        flash = flash.next.next
        hulk = hulk.next

        if flash == hulk:
            return find_size(flash)

obj = Node(Node(Node(Node(Node(Node(Node(Node())))))))
obj.next.next.next.next.next.next = obj.next.next.next.next
print(loop_size(obj))
