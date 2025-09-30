Certo! Ecco un semplice codice in Python che crea una lista di nomi, la randomizza e la stampa al contrario:

```python
import random

# Creazione della lista di nomi
nomi = ["Alice", "Marco", "Giulia", "Luca", "Sara", "Matteo", "Francesca", "Andrea", "Elena", "Stefano"]

# Randomizzazione della lista
random.shuffle(nomi)

# Stampa della lista al contrario
nomi_al_contrario = nomi[::-1]

print("Lista di nomi randomizzata e stampata al contrario:")
for nome in nomi_al_contrario:
    print(nome)
```

Questo codice utilizza il modulo `random` per randomizzare la lista di nomi e poi la stampa in ordine inverso. Puoi aggiungere o modificare i nomi nella lista come preferisci. Se hai bisogno di ulteriore aiuto, fammelo sapere!