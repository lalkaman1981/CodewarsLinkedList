"""
move node
"""

class Node(object):
    """
    Node class for reference
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    context class
    """
    def __init__(self, source, dest):
        start = Node(source.data)
        start.next = dest
        source = source.next

        self.source = source
        self.dest = start

def move_node(source, dest):
    """
    moves nodes
    """
    if source is None:
        return None

    return Context(source, dest)
