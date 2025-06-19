class CharNode:
    def __init__(self, char):
        self.char = char

class StarNode:
    def __init__(self, child):
        self.child = child

class OrNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class ConcatNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
