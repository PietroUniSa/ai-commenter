Certo! Ecco un esempio di codice Python che crea una lista di nomi, la randomizza e poi la stampa al contrario. Puoi personalizzare la lista di nomi come preferisci.

```python
import random

# Creiamo una lista di nomi
nomi = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"]

# Randomizziamo la lista
random.shuffle(nomi)

# Stampa la lista randomizzata al contrario
nomi_inverted = nomi[::-1]

print("Lista di nomi randomizzati al contrario:")
print(nomi_inverted)
```

In questo codice:
1. Importiamo il modulo `random` per utilizzare la funzione `shuffle`.
2. Creiamo una lista di nomi.
3. Utilizziamo `random.shuffle` per randomizzare la lista in modo che i nomi vengano disposti in ordine casuale.
4. Infine, stampiamo la lista randomizzata al contrario utilizzando la notazione `[::-1]`.

Puoi eseguire questo codice nel tuo ambiente Python per vedere il risultato. Se hai bisogno di ulteriori modifiche o funzionalità, fammelo sapere!