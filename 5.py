class ListNode:
    """Nodo di una lista collegata singolarmente."""
    def __init__(self, val: int, next: "ListNode | None" = None):
        self.val = val
        self.next = next

    # Utile solo per la stampa “1 -> 2 -> …”
    def __repr__(self):
        values = []
        cur = self
        while cur:
            values.append(str(cur.val))
            cur = cur.next
        return " -> ".join(values)

def remove_duplicates(head: ListNode | None) -> ListNode | None:
    """
    Rimuove i duplicati da una lista *già ordinata* in-place.
    Mantiene una sola copia per valore.
    Restituisce la testa (che potrebbe non cambiare).
    """
    current = head                       # ① puntatore che avanza nella lista
    while current and current.next:      # ② finché esistono almeno due nodi da confrontare
        if current.val == current.next.val:
            # ③ duplicato trovato: “saltiamo” il nodo successivo
            current.next = current.next.next
            # non avanziamo current: potremmo avere 1 -> 1 -> 1
        else:
            # ④ valori diversi: avanziamo
            current = current.next
    return head                           # ⑤ lista ora priva di duplicati

def build_linked_list(values):
    head = None
    for val in reversed(values):         # costruiamo la lista dal fondo
        head = ListNode(val, head)
    return head

# Input di esempio
head = build_linked_list([1, 2, 2, 3, 4, 4, 4, 5])
print("Before :", head)

head = remove_duplicates(head)
print("After  :", head)
