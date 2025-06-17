def can_jump(nums: list[int]) -> bool:
    """
    Restituisce True se l’ultimo indice è raggiungibile da 0.
    Algoritmo greedy: manteniamo la distanza massima raggiungibile finora.
    """
    max_reach = 0                       # posizione più lontana raggiungibile
    for i, jump in enumerate(nums):     # i = indice corrente
        if i > max_reach:               # se non possiamo arrivare fin qui…
            return False                # …allora siamo “bloccati”
        max_reach = max(max_reach, i + jump)  # aggiorno la portata
    return True                         # se il ciclo termina, l’ultimo indice è raggiungibile

print (can_jump([3, 2, 1, 0, 4]))  # False
print (can_jump([2, 3, 1, 1, 4]))  # True
