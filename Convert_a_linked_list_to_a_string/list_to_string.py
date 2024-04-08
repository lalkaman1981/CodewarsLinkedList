"""
convert array to a string
"""

class Node:
    """
    node class 
    """
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

def stringify(array: "Node") -> str:
    """
    accept array and returns string
    """
    if array is None:
        return "None"

    data = array.data
    text = f"{data}"
    head = array

    while data is not None:
        head = head.next

        if not head:
            text += " -> None"
            break

        data = head.data
        text += f" -> {data}"

    return text

print(stringify(Node(0, Node(1, Node(2, Node(3))))))
