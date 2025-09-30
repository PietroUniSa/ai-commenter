Ecco una funzione in Python che ordina una lista di numeri interi in ordine crescente utilizzando il metodo `sort()`:

```python
def ordina_lista(lista):
    """
    Questa funzione ordina una lista di numeri interi in ordine crescente.

    :param lista: Lista di numeri interi da ordinare
    :return: Lista ordinata in ordine crescente
    """
    lista.sort()
    return lista

# Esempio di utilizzo
numeri = [5, 3, 8, 1, 2]
numeri_ordinati = ordina_lista(numeri)
print(numeri_ordinati)  # Output: [1, 2, 3, 5, 8]
```

In alternativa, puoi utilizzare la funzione `sorted()` che restituisce una nuova lista ordinata senza modificare l'originale:

```python
def ordina_lista(lista):
    """
    Questa funzione restituisce una nuova lista di numeri interi ordinati in ordine crescente.

    :param lista: Lista di numeri interi da ordinare
    :return: Nuova lista ordinata in ordine crescente
    """
    return sorted(lista)

# Esempio di utilizzo
numeri = [5, 3, 8, 1, 2]
numeri_ordinati = ordina_lista(numeri)
print(numeri_ordinati)  # Output: [1, 2, 3, 5, 8]
```

Puoi scegliere uno dei due metodi in base alle tue esigenze!