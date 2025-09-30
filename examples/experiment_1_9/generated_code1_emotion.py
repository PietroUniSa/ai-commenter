Ciao! Certamente, posso aiutarti con questo. Ecco un esempio di codice Python che crea una lista di nomi, la randomizza e poi la stampa al contrario:

```python
import random

# Creiamo una lista di nomi
nomi = ["Alice", "Marco", "Giulia", "Luca", "Sara", "Matteo", "Francesca", "Davide"]

# Randomizziamo la lista
random.shuffle(nomi)

# Stampo la lista randomizzata al contrario
nomi_al_contrario = nomi[::-1]

print("Nomi randomizzati al contrario:")
for nome in nomi_al_contrario:
    print(nome)
```

### Come funziona il codice:
1. Importa il modulo `random` per poter randomizzare la lista.
2. Crea una lista di nomi.
3. Utilizza `random.shuffle()` per mescolare i nomi nella lista.
4. Usa la slicing `[::-1]` per ottenere la lista al contrario.
5. Stampa i nomi dalla lista al contrario.

Puoi eseguire questo codice in un ambiente Python e vedrai la lista di nomi randomizzati e stampati al contrario. Se hai bisogno di ulteriori modifiche o funzionalità, fammi sapere!