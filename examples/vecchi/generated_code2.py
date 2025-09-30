```python
def ordina_lista(lista):
    """Ordina una lista di numeri interi in ordine crescente."""
    return sorted(lista)

# Esempio di utilizzo
numeri = [5, 3, 8, 1, 4]
numeri_ordinati = ordina_lista(numeri)
print(numeri_ordinati)  # Dovrebbe stampare: [1, 3, 4, 5, 8]
```