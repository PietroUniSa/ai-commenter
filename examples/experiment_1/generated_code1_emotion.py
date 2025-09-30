Ecco un'implementazione della classe `ContoBancario` in Python che soddisfa i requisiti specificati. La classe consente di creare un conto con un intestatario, un saldo iniziale e un limite di scoperto. Include anche metodi per depositare e prelevare denaro, gestendo le eccezioni per fondi insufficienti e input non validi.

```python
class ContoBancario:
    def __init__(self, intestatario: str, saldo_iniziale: float, limite_scoperto: float):
        if saldo_iniziale < 0:
            raise ValueError("Il saldo iniziale non può essere negativo.")
        if limite_scoperto > 0:
            raise ValueError("Il limite di scoperto deve essere negativo o zero.")
        
        self.intestatario = intestatario
        self.saldo = saldo_iniziale
        self.limite_scoperto = limite_scoperto

    def deposita(self, importo: float):
        if importo <= 0:
            raise ValueError("L'importo da depositare deve essere positivo.")
        self.saldo += importo
        print(f"Deposito effettuato: {importo}. Saldo attuale: {self.saldo:.2f}.")

    def preleva(self, importo: float):
        if importo <= 0:
            raise ValueError("L'importo da prelevare deve essere positivo.")
        if self.saldo - importo < self.limite_scoperto:
            raise ValueError("Fondi insufficienti per il prelievo.")
        
        self.saldo -= importo
        print(f"Prelievo effettuato: {importo}. Saldo attuale: {self.saldo:.2f}.")

    def get_saldo(self) -> float:
        return self.saldo

    def __str__(self):
        return f"Conto Bancario di {self.intestatario}: Saldo = {self.saldo:.2f}, Limite di scoperto = {self.limite_scoperto:.2f}"


# Esempio di utilizzo:
if __name__ == "__main__":
    try:
        conto = ContoBancario("Mario Rossi", 1000.0, -200.0)
        print(conto)
        
        conto.deposita(200.0)
        conto.preleva(1500.0)
        print(conto)
        
        conto.preleva(100.0)  # Questo solleverà un'eccezione
    except ValueError as ve:
        print(f"Errore: {ve}")
```

### Spiegazione del codice:
1. **Costruttore (`__init__`)**: Inizializza l'oggetto `ContoBancario` con un intestatario, un saldo iniziale e un limite di scoperto. Verifica che il saldo iniziale non sia negativo e che il limite di scoperto sia non positivo.
  
2. **Metodo `deposita`**: Aggiunge fondi al saldo. Se l'importo è negativo o zero, viene sollevata un'eccezione.

3. **Metodo `preleva`**: Riduce il saldo di un importo specificato. Se l'importo è negativo o se il prelievo porterebbe il saldo al di sotto del limite di scoperto, viene sollevata un'eccezione.

4. **Metodo `get_saldo`**: Restituisce il saldo attuale.

5. **Metodo `__str__`**: Fornisce una rappresentazione stringa dell'oggetto `ContoBancario`.

6. **Esempio di utilizzo**: Dimostra come creare un conto, effettuare depositi e prelievi, e gestire le eccezioni che possono verificarsi.