Certo! Ecco un esempio di codice Python che crea una lista di nomi, la randomizza e poi la stampa al contrario:

```python
import random

# Creazione della lista di nomi
nomi = ["Alice", "Marco", "Giulia", "Luca", "Francesca", "Matteo", "Sara", "Giovanni"]

# Randomizzazione della lista
random.shuffle(nomi)

# Stampa della lista al contrario
nomi_al_contrario = nomi[::-1]
print(nomi_al_contrario)
```

### Come funziona il codice:
1. **Importazione del modulo random**: Per randomizzare la lista utilizziamo il modulo `random`.
2. **Creazione della lista di nomi**: Qui definisci i nomi che desideri includere nella lista.
3. **Randomizzazione**: Utilizziamo `random.shuffle()` per mescolare i nomi nella lista.
4. **Stampa al contrario**: Utilizziamo la slicing `[::-1]` per ottenere la lista al contrario e poi la stampiamo.

Puoi eseguire questo codice in un ambiente Python e otterrai una lista di nomi randomizzati e stampata in ordine inverso. Se hai bisogno di altro, fammi sapere!