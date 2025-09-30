Ecco una funzione in Python che ordina una lista di numeri interi in ordine crescente utilizzando l'algoritmo di ordinamento integrato `sort()`:

```python
def ordina_lista(lista):
    """
    Ordina una lista di numeri interi in ordine crescente.

    Args:
    lista (list): Una lista di numeri interi.

    Returns:
    list: La lista ordinata in ordine crescente.
    """
    lista.sort()
    return lista

# Esempio di utilizzo
numeri = [5, 2, 9, 1, 5, 6]
numeri_ordinati = ordina_lista(numeri)
print(numeri_ordinati)  # Output: [1, 2, 5, 5, 6, 9]
```

In questa funzione, utilizziamo il metodo `sort()` che modifica la lista originale in modo da ordinarla. Se desideri mantenere la lista originale invariata, puoi creare una copia della lista e ordinare quella:

```python
def ordina_lista(lista):
    """
    Ordina una lista di numeri interi in ordine crescente.

    Args:
    lista (list): Una lista di numeri interi.

    Returns:
    list: La lista ordinata in ordine crescente.
    """
    return sorted(lista)

# Esempio di utilizzo
numeri = [5, 2, 9, 1, 5, 6]
numeri_ordinati = ordina_lista(numeri)
print(numeri_ordinati)  # Output: [1, 2, 5, 5, 6, 9]
print(numeri)  # Output: [5, 2, 9, 1, 5, 6] (la lista originale rimane invariata)
```

Spero che questa funzione ti sia utile! Se hai bisogno di ulteriori modifiche o spiegazioni, non esitare a chiedere.