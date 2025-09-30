Certo! Ecco un'implementazione di base della classe `ContoBancario` in Python. Questa classe include metodi per depositare e prelevare fondi, controllare il saldo e stampare le informazioni sul conto.

```python
class ContoBancario:
    def __init__(self, numero_conto, titolare, saldo_iniziale=0):
        self.numero_conto = numero_conto
        self.titolare = titolare
        self.saldo = saldo_iniziale

    def deposita(self, importo):
        if importo <= 0:
            print("L'importo da depositare deve essere positivo.")
            return
        self.saldo += importo
        print(f"Deposito di {importo} effettuato. Saldo attuale: {self.saldo}")

    def preleva(self, importo):
        if importo <= 0:
            print("L'importo da prelevare deve essere positivo.")
            return
        if importo > self.saldo:
            print("Fondi insufficienti per effettuare il prelievo.")
            return
        self.saldo -= importo
        print(f"Prelievo di {importo} effettuato. Saldo attuale: {self.saldo}")

    def mostra_saldo(self):
        print(f"Il saldo attuale del conto {self.numero_conto} è: {self.saldo}")

    def info_conto(self):
        print(f"Conto: {self.numero_conto}\nTitolare: {self.titolare}\nSaldo: {self.saldo}")


# Esempio di utilizzo
if __name__ == "__main__":
    mio_conto = ContoBancario("123456789", "Mario Rossi", 1000)
    mio_conto.mostra_saldo()
    
    mio_conto.deposita(500)
    mio_conto.preleva(200)
    mio_conto.preleva(1500)  # Questo dovrebbe mostrare un messaggio di errore
    mio_conto.mostra_saldo()
    mio_conto.info_conto()
```

### Descrizione della classe:

1. **Costruttore (`__init__`)**: Inizializza il conto con un numero di conto, un titolare e un saldo iniziale. Se non viene fornito un saldo iniziale, viene impostato a 0.

2. **Metodo `deposita`**: Aggiunge un importo al saldo se l'importo è positivo.

3. **Metodo `preleva`**: Sottrae un importo dal saldo se l'importo è positivo e ci sono fondi sufficienti nel conto.

4. **Metodo `mostra_saldo`**: Stampa il saldo attuale del conto.

5. **Metodo `info_conto`**: Mostra le informazioni dettagliate del conto, inclusi il numero di conto, il titolare e il saldo.

Puoi utilizzare questa classe per gestire un conto bancario in modo semplice. Se hai bisogno di ulteriori funzionalità o modifiche, fammi sapere!