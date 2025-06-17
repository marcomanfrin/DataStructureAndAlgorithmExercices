def is_balanced(s: str) -> bool:
    """
    Ritorna True se la stringa `s` è bilanciata rispetto alle parentesi
    tonde (), quadre [] e graffe {}.
    Usa uno stack esplicito (lista Python).
    """
    # Mappa di chiusura -> apertura
    matching = {')': '(', ']': '[', '}': '{'}
    stack: list[str] = []                              # lo stack

    for ch in s:
        if ch in matching.values():                    # parentesi d’apertura
            stack.append(ch)
        elif ch in matching:                           # parentesi di chiusura
            if not stack or stack.pop() != matching[ch]:
                return False                           # chiusura sbagliata
        # gli altri caratteri vengono ignorati (opzionale: else -> errore)
    return not stack                                   # True se vuoto

tests = ["([]{})", "([)]", "((()))", "", "[(]{})"]
for t in tests:
    print(f"{t!r:10} -> {is_balanced(t)}")