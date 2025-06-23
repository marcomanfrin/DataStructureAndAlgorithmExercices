def merge_sort(arr):
    """
    Ordina la lista `arr` in modo non-distruttivo, restituendone
    una nuova versione ordinata (stable sort).

    Algoritmo:
    1. Caso base: se la lista ha 0 o 1 elementi è già ordinata.
    2. Passo ricorsivo:
       a) si divide l'array a metà
       b) si ordina ricorsivamente ciascuna metà
       c) si fondono (merge) le due metà in un'unica lista ordinata
    """

    # ---- 1. CASO BASE -------------------------------------------------
    if len(arr) <= 1:           # vettore di lunghezza 0 o 1 → già ordinato
        return arr[:]           # copia difensiva (non modifica input)

    # ---- 2a. DIVIDE ---------------------------------------------------
    mid = len(arr) // 2         # punto di taglio centrale
    left_half  = arr[:mid]      # slice sinistra
    right_half = arr[mid:]      # slice destra

    # Ordina ricorsivamente le due metà (2b. CONQUER)
    sorted_left  = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # ---- 2c. MERGE ----------------------------------------------------
    merged = []                 # lista risultato
    i = j = 0                   # indici correnti nelle due metà

    # Finché entrambi gli array hanno elementi a disposizione
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            merged.append(sorted_left[i])   # prende da sinistra
            i += 1
        else:
            merged.append(sorted_right[j])  # prende da destra
            j += 1

    # Uno dei due array potrebbe avere ancora elementi residui
    merged.extend(sorted_left[i:])          # flush della coda sinistra
    merged.extend(sorted_right[j:])         # flush della coda destra

    return merged

nums = [38, 27, 43, 3, 9, 82, 10]
print("Originale:", nums)
print("Ordinato :", merge_sort(nums))

# Perché funziona
# Divide & Conquer: il problema di ordinare n elementi viene spezzato in due sotto-problemi di taglia n/2, risolti indipendentemente.
# Merge lineare: poiché le due metà in uscita sono già ordinate ricorsivamente, basta un singolo passaggio lineare per combinarle senza violare l’ordine.
# Stabilità: il test <= (anziché <) garantisce che, a parità di chiave, l’elemento della metà sinistra venga copiato prima—quindi l’ordine relativo degli elementi uguali rimane invariato.
# Complessità
# Tempo: ogni livello di ricorsione esegue un merge di costo O(n) e ci sono log₂ n livelli ⇒ complessità complessiva O(n log n), costante in tutti i casi (migliore, medio, peggiore).
# Spazio: richiede O(n) spazio addizionale perché il merge crea un nuovo array (più lo stack ricorsivo O(log n)); esistono versioni in-place più complesse che sacrificano un po’ di chiarezza per ridurre la memoria.