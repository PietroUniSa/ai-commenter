Ecco un'implementazione della classe `ContoBancario` in Python che soddisfa i requisiti specificati. La classe include metodi per la creazione di un conto, il deposito e il prelievo di denaro, e gestisce le eccezioni per fondi insufficienti e input non validi.

```python
class ContoBancario:
    def __init__(self, intestatario: str, saldo_iniziale: float, limite_scoperto: float):
        if saldo_iniziale < 0:
            raise ValueError("Il saldo iniziale non può essere negativo.")
        if limite_scoperto > 0:
            raise ValueError("Il limite di scoperto deve essere zero o negativo.")
        
        self.intestatario = intestatario
        self.saldo = saldo_iniziale
        self.limite_scoperto = limite_scoperto

    def deposita(self, importo: float):
        if importo <= 0:
            raise ValueError("L'importo del deposito deve essere maggiore di zero.")
        self.saldo += importo
        print(f"Deposito di {importo} effettuato. Saldo attuale: {self.saldo}")

    def preleva(self, importo: float):
        if importo <= 0:
            raise ValueError("L'importo del prelievo deve essere maggiore di zero.")
        if self.saldo - importo < self.limite_scoperto:
            raise ValueError("Fondi insufficienti per il prelievo.")
        self.saldo -= importo
        print(f"Prelievo di {importo} effettuato. Saldo attuale: {self.saldo}")

    def mostra_saldo(self):
        print(f"Saldo attuale: {self.saldo}")

# Esempio di utilizzo
if __name__ == "__main__":
    try:
        conto = ContoBancario("Mario Rossi", 1000, -500)
        conto.mostra_saldo()
        conto.deposita(200)
        conto.preleva(1500)
        conto.mostra_saldo()
    except ValueError as e:
        print(f"Errore: {e}")
```

### Descrizione della classe `ContoBancario`:

1. **Inizializzazione**:
   - Il costruttore `__init__` accetta tre parametri: `intestatario`, `saldo_iniziale` e `limite_scoperto`.
   - Viene effettuata una verifica per assicurarsi che il saldo iniziale non sia negativo e che il limite di scoperto sia zero o negativo.

2. **Metodi**:
   - `deposita`: Permette di depositare un importo nel conto. Se l'importo è minore o uguale a zero, solleva un'eccezione.
   - `preleva`: Permette di prelevare un importo dal conto. Se l'importo è minore o uguale a zero o se il prelievo porterebbe il saldo al di sotto del limite di scoperto, solleva un'eccezione.
   - `mostra_saldo`: Mostra il saldo attuale del conto.

3. **Esempio di utilizzo**:
   - Nel blocco `if __name__ == "__main__":`, viene creato un conto bancario e vengono effettuate alcune operazioni, con gestione delle eccezioni per eventuali errori.

Puoi testare la classe e modificarla secondo le tue esigenze!