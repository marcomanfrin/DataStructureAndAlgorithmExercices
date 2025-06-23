from collections import deque
from typing import Optional


class TreeNode:
    """Nodo di un albero binario."""

    def __init__(
        self,
        val: int,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def sum_even_levels(root: Optional[TreeNode]) -> int:
    """
    Restituisce la somma dei valori dei nodi agli
    *livelli di profondità pari* (0, 2, 4, …).
    Traversal BFS con una coda.
    """
    if root is None:
        return 0

    total = 0
    q = deque([(root, 0)])  # (nodo, profondità)

    while q:
        node, depth = q.popleft()

        if depth % 2 == 0:  # livello pari?
            total += node.val

        # Enqueue figli — profondità = depth + 1
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))

    return total


# Perché BFS (coda) è la scelta più naturale

# 	•	Separation of concerns In BFS i nodi di uno stesso livello vengono estratti consecutivamente; 
#       sapere la profondità di un nodo è immediato perché la manteniamo nel tuple (node, depth) o sfruttiamo il numero di elementi 
#       della coda prima di ogni “layer”.
# 	•	Niente ricorsione profonda Un albero molto sbilanciato potrebbe far sforare la ricorsione massima di Python; 
#       la coda evita questo rischio.
# 	•	Espressività Quando l’obiettivo dipende esplicitamente dal livello (pari/dispari, massimo per livello, ecc.), 
#       BFS rispecchia l’ordine in cui ci interessano i nodi.

# Costruiamo l'albero:
#         1            ← livello 0 (pari)
#       /   \
#      2     3         ← livello 1 (dispari)
#     / \     \
#    4   5     6       ← livello 2 (pari)

root = TreeNode(
    1,
    left=TreeNode(
        2,
        left=TreeNode(4),
        right=TreeNode(5)
    ),
    right=TreeNode(
        3,
        right=TreeNode(6)
    )
)

# Calcoliamo la somma dei livelli pari
result = sum_even_levels(root)
print("Somma livelli pari:", result)   # atteso: 1 + 4 + 5 + 6 = 16