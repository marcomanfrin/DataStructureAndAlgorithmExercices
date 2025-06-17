#Esercizi

Gli esercizi seguenti sono pensati per supportare l'apprendimento e sono di grande aiuto nella preparazione all'esame finale. Gli esercizi più impegnativi offrono anche un'esplorazione più approfondita per chi desidera ampliare la comprensione oltre il materiale di base.

---
1. Analizza la complessità temporale e spaziale del seguente algoritmo. Usa la notazione Big-O e giustifica la tua risposta: (big o)
    
    ```python
    python
    CopiaModifica
    def rearrange_list(data):
        result = []
        for i in range(len(data)):
            for j in range(i, len(data)):
                result.append(data[j])
            data = data[1:]
        return result
    
    ```
 2. Scrivi una funzione Python che, data una lista collegata (linked list) singolarmente concatenata di interi ordinati in ordine crescente, rimuove tutti i duplicati mantenendo solo una copia per ogni valore. (linked list)
    
    Esempio:
    ```python
    python
    CopiaModifica
    Input: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5
    Output: 1 -> 2 -> 3 -> 4 -> 5
    ```
 
 3. Data una lista di interi non negativi, scrivi una funzione che determini se è possibile raggiungere l'ultimo indice partendo dall'indice 0. Ogni valore nella lista rappresenta il numero massimo di passi avanti che puoi compiere da quella posizione. (linked list)
    
    Esempio:
    ```python
    python
    CopiaModifica
    Input: [3, 2, 1, 0, 4] → Output: False
    Input: [2, 3, 1, 1, 4] → Output: True
    
    ```
 4. Scrivi una funzione che verifica se una data stringa di parentesi è bilanciata. (stack)

    Esempio:    
    ```python
    python
    CopiaModifica
    ([]{}) → True
    ([)] → False
    ((())) → True
    ```
    La soluzione deve usare esplicitamente uno **stack**.

 5.  Hai due code (queue). Scrivi una classe Python che utilizza solo queste due code per simulare una pila (stack). Implementa le operazioni di `push` e `pop`. (queue)
   
 6.  Scrivi una funzione Python che, dato un albero binario (non necessariamente un albero binario di ricerca), restituisce la somma dei valori dei nodi ai livelli di profondità pari (livello 0, 2, 4, ...). Giustifica brevemente la tua scelta del metodo di attraversamento (ricorsione o coda). (trees)
   
 7.  Scrivi una funzione che restituisce la lunghezza del percorso più lungo in un albero binario (non necessariamente bilanciato né un BST), dove il percorso può iniziare e finire in qualsiasi nodo e deve seguire solo connessioni padre-figlio. (trees)
   
 8.  Definisci i seguenti tipi di grafi, evidenziando le differenze principali e fornendo almeno un caso d'uso per ciascuno: (graphs)
    - Grafo orientato
    - Grafo pesato
    - Grafo ciclico
    - Grafo bipartito
   
  9.  Descrivi come funziona l'algoritmo di Dijkstra. Qual è la differenza principale rispetto all’algoritmo di Bellman-Ford? Poi implementa l’algoritmo di Dijkstra in Python usando un dizionario per rappresentare il grafo e una coda di priorità per la selezione dei nodi. (graph)
   
  10. Spiega cosa sono le tabelle hash (hash table) e in cosa differiscono da una lista e da un insieme (set). Fornisci un esempio concreto in cui usare una tabella hash è più efficiente rispetto ad altre strutture dati. (hash table)
   
  11. Spiega le differenze in termini di complessità temporale, spaziale e stabilità tra almeno tre algoritmi di ordinamento (es. Bubble Sort, Merge Sort, Quick Sort). Per ciascuno dei seguenti casi, indica quale algoritmo è più adatto e perché: (sorting)
    - Input già ordinato
    - Input in ordine inverso
    - Input con molti duplicati
    - Input molto grande (milioni di elementi)
  
  12. Scrivi una funzione Python che implementa l’algoritmo di Merge Sort. Includi commenti che spiegano passo dopo passo come funziona l’algoritmo. Facoltativamente, discuti la sua complessità temporale e spaziale. (sorting)
   
  13.  Data una lista di caratteri, restituisci una stringa in cui i caratteri sono ordinati in base alla frequenza decrescente. (sorting)
    Esempio:
    ```python
    python
    CopiaModifica
    Input: ['a', 'b', 'a', 'c', 'a', 'b']
    Output: "aaabbc"
    ```
    Suggerimento: Usa una tabella hash per contare le frequenze, poi ordina in base alla frequenza.
    
    14. Per ciascuno dei seguenti algoritmi di ordinamento, indica se è stabile o instabile, e spiega cosa significa "stabilità" nel contesto degli algoritmi di ordinamento: (sorting)
    - Bubble Sort
    - Insertion Sort
    - Quick Sort
    - Heap Sort
    - Merge Sort