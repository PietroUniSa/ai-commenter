Ecco un'implementazione della classe `ContoBancario` in Python che soddisfa i requisiti specificati. La classe consente di creare un conto bancario, effettuare depositi e prelievi, e gestisce le eccezioni per fondi insufficienti e input non validi.

```python
class ContoBancario:
    def __init__(self, intestatario, saldo_iniziale=0, limite_scoperto=0):
        self.intestatario = intestatario
        self.saldo = saldo_iniziale
        self.limite_scoperto = limite_scoperto

    def deposita(self, importo):
        if importo <= 0:
            raise ValueError("L'importo del deposito deve essere maggiore di zero.")
        self.saldo += importo
        print(f"Deposito di {importo} effettuato. Saldo attuale: {self.saldo}.")

    def preleva(self, importo):
        if importo <= 0:
            raise ValueError("L'importo del prelievo deve essere maggiore di zero.")
        if self.saldo - importo < -self.limite_scoperto:
            raise ValueError("Fondi insufficienti per effettuare il prelievo.")
        self.saldo -= importo
        print(f"Prelievo di {importo} effettuato. Saldo attuale: {self.saldo}.")

    def mostra_saldo(self):
        return f"Saldo attuale di {self.intestatario}: {self.saldo}."

# Esempio di utilizzo
if __name__ == "__main__":
    conto = ContoBancario("Mario Rossi", 1000, 200)
    print(conto.mostra_saldo())
    
    try:
        conto.deposita(500)
        conto.preleva(200)
        conto.preleva(1500)  # Questo dovrebbe sollevare un'eccezione
    except ValueError as e:
        print(e)

    print(conto.mostra_saldo())
```

### Descrizione della classe:

1. **Costruttore (`__init__`)**: Inizializza il conto bancario con un intestatario, un saldo iniziale e un limite di scoperto.

2. **Metodo `deposita`**: Permette di depositare un importo. Se l'importo è minore o uguale a zero, solleva un'eccezione `ValueError`.

3. **Metodo `preleva`**: Permette di prelevare un importo. Se l'importo è minore o uguale a zero o se il prelievo supera il saldo disponibile (considerando il limite di scoperto), solleva un'eccezione `ValueError`.

4. **Metodo `mostra_saldo`**: Restituisce una stringa che mostra il saldo attuale del conto.

### Esempio di utilizzo:
Il codice di esempio alla fine crea un conto, effettua un deposito e un prelievo, e gestisce le eccezioni per un tentativo di prelievo non valido.