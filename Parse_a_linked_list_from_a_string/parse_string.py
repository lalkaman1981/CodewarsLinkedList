"""
parses list
"""

class Node:
    """
    node class
    """
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self):
        return f"{self.data}"

def linked_list_from_string(string: str) -> "Node":
    """
    returns linked list from string
    """
    if string is None or string == "None":
        return None

    if " -> " not in string:
        return Node(string)

    lst = string.split(" -> ")

    head = Node(int(lst[-2]))

    for element in reversed(lst[:-2]):
        element = int(element)
        head = Node(element, head)

    return head
