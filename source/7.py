from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val: int,
                 left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def longest_path_length(root: Optional[TreeNode]) -> int:
    """
    Restituisce la lunghezza (in archi) del percorso più lungo
    presente in un albero binario.  È l’equivalente del *diameter*.
    """

    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
        """
        Ritorna (height, best) per il sotto-albero con radice `node`.

        height = lunghezza (in archi) del percorso più lungo che scende
                 da `node` fino a una foglia.
        best   = diametro massimo all’interno di questo sotto-albero.
        """
        if node is None:
            return -1, 0          # altezza di albero vuoto = -1 (così la foglia ha 0)

        lh, lbest = dfs(node.left)
        rh, rbest = dfs(node.right)

        height = 1 + max(lh, rh)                # altezza del nodo corrente
        through = lh + rh + 2                   # cammino che passa per `node`
        best = max(lbest, rbest, through)       # diametro migliore fin qui
        return height, best

    _, diameter = dfs(root)
    return diameter

#      1
#     / \
#    2   3
#       / \
#      4   5
#         /
#        6
root = TreeNode(1,
        left=TreeNode(2),
        right=TreeNode(3,
               left=TreeNode(4),
               right=TreeNode(5,
                      left=TreeNode(6))))

print(longest_path_length(root))   # output: 4