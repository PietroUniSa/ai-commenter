Certo! Ecco una possibile implementazione della classe `ContoBancario` in Python che soddisfa i requisiti descritti:

```python
class ContoBancario:
    def __init__(self, intestatario: str, saldo_iniziale: float, limite_scoperto: float = 0.0):
        """Inizializza un nuovo conto bancario."""
        if saldo_iniziale < 0:
            raise ValueError("Il saldo iniziale non può essere negativo.")
        self.intestatario = intestatario
        self.saldo = saldo_iniziale
        self.limite_scoperto = limite_scoperto

    def deposita(self, importo: float) -> None:
        """Deposita una somma di denaro nel conto."""
        if importo <= 0:
            raise ValueError("L'importo da depositare deve essere maggiore di zero.")
        self.saldo += importo
        print(f"Deposito di {importo:.2f} effettuato. Saldo attuale: {self.saldo:.2f}")

    def preleva(self, importo: float) -> None:
        """Preleva una somma di denaro dal conto."""
        if importo <= 0:
            raise ValueError("L'importo da prelevare deve essere maggiore di zero.")
        if self.saldo - importo < -self.limite_scoperto:
            raise ValueError("Fondi insufficienti per il prelievo.")
        self.saldo -= importo
        print(f"Prelievo di {importo:.2f} effettuato. Saldo attuale: {self.saldo:.2f}")

    def mostra_saldo(self) -> float:
        """Restituisce il saldo attuale del conto."""
        return self.saldo

# Esempio di utilizzo della classe ContoBancario
if __name__ == "__main__":
    conto = ContoBancario("Mario Rossi", 1000.0, 200.0)
    conto.deposita(500.0)
    conto.preleva(300.0)
    print(f"Saldo finale: {conto.mostra_saldo():.2f}")
```

### Spiegazione della classe:
- **Inizializzazione**: Il costruttore (`__init__`) accetta il nome dell'intestatario, il saldo iniziale e un limite di scoperto. Se il saldo iniziale è negativo, solleva un'eccezione.
- **Metodi per il deposito**: Il metodo `deposita` consente di aggiungere denaro al conto, con un controllo per assicurarsi che l'importo sia positivo.
- **Metodi per il prelievo**: Il metodo `preleva` permette di ritirare denaro dal conto. Controlla se l'importo è positivo e se il saldo non supera il limite di scoperto.
- **Mostra saldo**: Il metodo `mostra_saldo` restituisce il saldo attuale del conto.

### Esempio di utilizzo
Nel blocco `if __name__ == "__main__":`, viene creato un conto bancario e vengono effettuati delle operazioni di deposito e prelievo, mostrando infine il saldo finale. 

Puoi espandere la classe con ulteriori funzionalità se necessario!