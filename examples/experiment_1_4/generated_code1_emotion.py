Certo! Ecco un semplice programma in Python che crea una lista di numeri pari e dispari, e poi li stampa al contrario:

```python
# Creazione di una lista di numeri da 1 a 20
numeri = list(range(1, 21))

# Separazione in numeri pari e dispari
numeri_pari = [num for num in numeri if num % 2 == 0]
numeri_dispari = [num for num in numeri if num % 2 != 0]

# Unione delle liste
numeri_completi = numeri_pari + numeri_dispari

# Stampa dei numeri al contrario
print("Numeri pari e dispari stampati al contrario:")
for num in reversed(numeri_completi):
    print(num)
```

### Spiegazione del codice:
1. Creiamo una lista di numeri da 1 a 20.
2. Utilizziamo una list comprehension per separare i numeri pari e i numeri dispari.
3. Uniamo le due liste in `numeri_completi`.
4. Stampiamo i numeri in ordine inverso utilizzando `reversed()`.

Puoi eseguire questo codice in un ambiente Python per vedere il risultato!