Certo! Ecco un esempio di una classe `ContoBancario` in Python che rappresenta un conto bancario. Questa classe include metodi per depositare, prelevare e visualizzare il saldo del conto.

```python
class ContoBancario:
    def __init__(self, intestatario, saldo_iniziale=0):
        self.intestatario = intestatario
        self.saldo = saldo_iniziale

    def deposita(self, importo):
        if importo > 0:
            self.saldo += importo
            print(f"Deposito di {importo} effettuato. Saldo attuale: {self.saldo}")
        else:
            print("L'importo del deposito deve essere positivo.")

    def preleva(self, importo):
        if importo > 0:
            if importo <= self.saldo:
                self.saldo -= importo
                print(f"Prelievo di {importo} effettuato. Saldo attuale: {self.saldo}")
            else:
                print("Fondi insufficienti per effettuare il prelievo.")
        else:
            print("L'importo del prelievo deve essere positivo.")

    def mostra_saldo(self):
        print(f"Il saldo attuale di {self.intestatario} è: {self.saldo}")

# Esempio di utilizzo
if __name__ == "__main__":
    conto = ContoBancario("Mario Rossi", 100)
    conto.mostra_saldo()
    conto.deposita(50)
    conto.preleva(30)
    conto.mostra_saldo()
    conto.preleva(150)  # Tentativo di prelievo con fondi insufficienti
```

### Descrizione della classe:

- **`__init__`**: Questo è il costruttore della classe, che inizializza il nome dell'intestatario e il saldo iniziale del conto.
- **`deposita`**: Questo metodo consente di depositare un importo nel conto, verificando che l'importo sia positivo.
- **`preleva`**: Questo metodo consente di prelevare un importo dal conto, verificando che l'importo sia positivo e che ci siano fondi sufficienti.
- **`mostra_saldo`**: Questo metodo visualizza il saldo attuale del conto.

Puoi utilizzare questa classe per creare un conto bancario e gestire le operazioni di deposito e prelievo.