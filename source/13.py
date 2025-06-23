from collections import Counter
from typing import List

def freq_sort(chars: List[str]) -> str:
    """
    Ritorna una stringa in cui i caratteri di `chars` compaiono
    ordinati per frequenza decrescente.
    A parità di frequenza, l'ordine è quello naturale del carattere.
    """
    # 1. Conteggio O(n) tramite hash table
    counts = Counter(chars)           # {'a': 3, 'b': 2, 'c': 1, ...}

    # 2. Ordinamento O(k log k) dove k = numero di caratteri distinti
    #    key = (-freq, char) così l'ordinamento è prima per frequenza desc.,
    #    poi alfabetico asc. (utile per avere un risultato deterministico)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    # 3. Ricostruzione stringa O(n)
    #    Per ogni (char, freq) moltiplica il carattere per la frequenza.
    return "".join(char * freq for char, freq in ordered)

print(freq_sort(['a', 'b', 'a', 'c', 'a', 'b']))   # "aaabbc"

# Come funziona, passo per passo
# Conteggio
# Counter calcola un hash per ogni carattere e aggiorna il relativo contatore: tutto in tempo lineare rispetto alla lunghezza dell’input.
# Ordinamento dei conteggi
# sorted riceve le coppie (carattere, frequenza) e le ordina usando come chiave una tupla con la frequenza negata (così l’ordinamento naturale crescente di Python diventa decrescente sulle frequenze) e il carattere stesso per rompere i pareggi.
# Ricostruzione della stringa
# Con un comprehension moltiplichiamo il carattere per la sua frequenza e concatenamo i pezzi nell’ordine scelto.
# Complessità
# Tempo: O(n + k log k)
# Dove n è la lunghezza totale della lista e k il numero di simboli distinti. Nella pratica k è al massimo 256 se lavoriamo con ASCII, spesso molto meno: quindi l’ordinamento è trascurabile rispetto al conteggio.
# Spazio extra: O(k) per la hash-table dei contatori più O(n) per la stringa di output (che per definizione deve contenerli tutti).

from typing import List

def freq_sort_v2(chars: List[str]) -> str:
    """
    Restituisce una stringa i cui caratteri compaiono in ordine di frequenza
    decrescente. A parità di frequenza si usa l’ordine alfabetico del carattere.
    """
    # 1. -------------------- conteggio manuale --------------------------
    freq: dict[str, int] = {}
    for ch in chars:                       # un passaggio lineare
        freq[ch] = freq.get(ch, 0) + 1     # hash-table: O(1) medio

    # 2. -------------------- ordinamento per frequenza ------------------
    #    Chiave = tupla (-frequenza, carattere) così:
    #    – la frequenza negativa impone l’ordine decrescente
    #    – il carattere rompe i pareggi in modo deterministico
    ordered = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

    # 3. -------------------- ricostruzione della stringa ----------------
    pieces = []
    for ch, count in ordered:              # pochi simboli distinti
        pieces.append(ch * count)          # concateniamo 'aaa', 'bb', ...
    return "".join(pieces)
