Certo, possiamo costruire insieme una classe `ContoBancario` in Python che rappresenti un conto bancario. Seguiamo i passaggi necessari per garantirne il corretto funzionamento, inclusa la gestione delle eccezioni.

### Passo 1: Creazione della classe

Iniziamo creando la classe `ContoBancario`. Questa classe avrà un costruttore (`__init__`) che accetta l'intestatario, il saldo iniziale e il limite di scoperto.

### Passo 2: Definizione dei metodi

Aggiungeremo metodi per depositare e prelevare denaro. Inoltre, gestiremo le eccezioni per assicurci che non si possa prelevare più denaro di quanto disponibile, tenendo conto del limite di scoperto.

### Ecco il codice completo:

```python
class ContoBancario:
    def __init__(self, intestatario, saldo_iniziale=0, limite_scoperto=0):
        self.intestatario = intestatario
        self.saldo = saldo_iniziale
        self.limite_scoperto = limite_scoperto

    def deposita(self, importo):
        if importo <= 0:
            raise ValueError("L'importo del deposito deve essere positivo.")
        self.saldo += importo
        print(f"Deposito di {importo} effettuato. Saldo attuale: {self.saldo}")

    def preleva(self, importo):
        if importo <= 0:
            raise ValueError("L'importo del prelievo deve essere positivo.")
        if self.saldo - importo < -self.limite_scoperto:
            raise ValueError("Fondi insufficienti per questo prelievo.")
        self.saldo -= importo
        print(f"Prelievo di {importo} effettuato. Saldo attuale: {self.saldo}")

    def mostra_saldo(self):
        print(f"Saldo attuale: {self.saldo}")

# Esempio di utilizzo della classe:
conto = ContoBancario("Mario Rossi", 1000, 200)

conto.mostra_saldo()  # Mostra il saldo
conto.deposita(500)    # Deposita 500 euro
conto.preleva(200)     # Preleva 200 euro
conto.preleva(1500)    # Prova a prelevare 1500 euro (dovrebbe sollevare un'eccezione)
```

### Spiegazione del codice:

1. **Costruttore (`__init__`)**: Accetta il nome dell'intestatario, il saldo iniziale e il limite di scoperto. Questi valori vengono memorizzati come attributi dell'oggetto.

2. **Metodo `deposita`**: Accetta un importo da depositare. Se l'importo è positivo, viene aggiunto al saldo. In caso contrario, viene sollevata un'eccezione.

3. **Metodo `preleva`**: Accetta un importo da prelevare. Verifica se l'importo è positivo e se il saldo, meno l'importo da prelevare, non supera il limite di scoperto. Se non ci sono problemi, l'importo viene sottratto dal saldo. In caso contrario, viene sollevata un'eccezione.

4. **Metodo `mostra_saldo`**: Stampa il saldo attuale del conto.

### Esempio di utilizzo

Alla fine del codice, puoi vedere un esempio di come utilizzare la classe `ContoBancario`. Puoi creare un nuovo conto e testare i metodi di deposito e prelievo.

Se hai bisogno di ulteriori chiarimenti o ulteriori funzionalità, non esitare a chiedere!