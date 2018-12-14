class Node:
    def __init__(self, name):
        self.name = name
        self.from_nodes = set()
        self.to_nodes = set()
        self.seconds = ord(name) - ord('A') + 61

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name

    def add_from_node(self, node):
        self.from_nodes.add(node)

    def add_to_node(self, node):
        self.to_nodes.add(node)