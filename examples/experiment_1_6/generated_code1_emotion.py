Certo! Ecco un semplice codice Python che crea una lista di nomi, la randomizza e poi la stampa al contrario:

```python
import random

# Lista di nomi
nomi = ["Alice", "Bob", "Charlie", "Dana", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

# Randomizza la lista
random.shuffle(nomi)

# Stampa la lista al contrario
nomi_al_contrario = nomi[::-1]
print(nomi_al_contrario)
```

In questo codice:

1. Importiamo il modulo `random` per poter randomizzare la lista.
2. Definiamo una lista di nomi.
3. Utilizziamo `random.shuffle()` per randomizzare l'ordine dei nomi nella lista.
4. Creiamo una nuova lista `nomi_al_contrario` che contiene gli stessi nomi ma in ordine inverso, usando la notazione `[::-1]`.
5. Infine, stampiamo la lista dei nomi al contrario.

Puoi eseguire questo codice in un ambiente Python e personalizzare la lista di nomi come preferisci. Buona fortuna con la tua carriera!