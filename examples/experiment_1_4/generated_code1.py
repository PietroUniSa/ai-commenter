Certo! Ecco un programma in Python che genera una lista di numeri pari e dispari, quindi li stampa in ordine inverso:

```python
def genera_numeri(n):
    numeri_pari = []
    numeri_dispari = []
    
    for i in range(n):
        if i % 2 == 0:
            numeri_pari.append(i)
        else:
            numeri_dispari.append(i)
    
    return numeri_pari, numeri_dispari

def stampa_in_ordine_inverso(lista):
    print(lista[::-1])

def main():
    n = int(input("Inserisci un numero intero: "))
    numeri_pari, numeri_dispari = genera_numeri(n)
    
    print("Numeri pari in ordine inverso:")
    stampa_in_ordine_inverso(numeri_pari)
    
    print("Numeri dispari in ordine inverso:")
    stampa_in_ordine_inverso(numeri_dispari)

if __name__ == "__main__":
    main()
```

### Come funziona il programma:
1. La funzione `genera_numeri(n)` genera due liste: una per i numeri pari e una per i numeri dispari fino a `n`.
2. La funzione `stampa_in_ordine_inverso(lista)` stampa la lista passata come argomento in ordine inverso.
3. La funzione `main()` chiede all'utente di inserire un numero intero `n`, chiama la funzione per generare i numeri e poi stampa le liste di numeri pari e dispari in ordine inverso.

### Esempio di utilizzo:
Se l'utente inserisce `10`, il programma stamperà:
```
Numeri pari in ordine inverso:
[8, 6, 4, 2, 0]
Numeri dispari in ordine inverso:
[9, 7, 5, 3, 1]
```

Puoi eseguire il codice in un ambiente Python per testarlo!