Certo! Ecco un esempio di codice Python che crea una lista di nomi, la randomizza e poi la stampa al contrario:

```python
import random

# Creazione della lista di nomi
nomi = ["Alice", "Marco", "Giulia", "Luca", "Sofia", "Matteo", "Chiara", "Andrea"]

# Randomizzazione della lista
random.shuffle(nomi)

# Stampa della lista al contrario
nomi_reverse = nomi[::-1]
print(nomi_reverse)
```

Questo codice utilizza il modulo `random` per mescolare la lista di nomi e poi utilizza lo slicing per stampare la lista in ordine inverso. Puoi eseguire questo codice in un ambiente Python e vedrai i nomi stampati in un ordine casuale e al contrario.