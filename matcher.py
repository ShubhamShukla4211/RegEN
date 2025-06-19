def epsilon_closure(states):
    stack = list(states)
    closure = set(states)
    while stack:
        state = stack.pop()
        for char, next_state in state.edges:
            if char is None and next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure

def match_nfa(nfa, string):
    current_states = epsilon_closure({nfa.start})
    for c in string:
        next_states = set()
        for state in current_states:
            for edge_char, next_state in state.edges:
                if edge_char == c:
                    next_states.add(next_state)
        current_states = epsilon_closure(next_states)
    return nfa.accept in current_states
