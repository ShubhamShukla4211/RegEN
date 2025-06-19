class State:
    def __init__(self):
        self.edges = []  # list of (char, next_state)

class NFA:
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def build_nfa(node):
    if isinstance(node, CharNode):
        s1, s2 = State(), State()
        s1.edges.append((node.char, s2))
        return NFA(s1, s2)

    if isinstance(node, ConcatNode):
        nfa1 = build_nfa(node.left)
        nfa2 = build_nfa(node.right)
        nfa1.accept.edges.append((None, nfa2.start))
        return NFA(nfa1.start, nfa2.accept)

    if isinstance(node, OrNode):
        start, accept = State(), State()
        nfa1 = build_nfa(node.left)
        nfa2 = build_nfa(node.right)
        start.edges.append((None, nfa1.start))
        start.edges.append((None, nfa2.start))
        nfa1.accept.edges.append((None, accept))
        nfa2.accept.edges.append((None, accept))
        return NFA(start, accept)

    if isinstance(node, StarNode):
        start, accept = State(), State()
        nfa = build_nfa(node.child)
        start.edges.append((None, nfa.start))
        start.edges.append((None, accept))
        nfa.accept.edges.append((None, nfa.start))
        nfa.accept.edges.append((None, accept))
        return NFA(start, accept)
