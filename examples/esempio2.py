import random

# Genera una lista di numeri casuali
def genera_lista(n, minimo, massimo):
    lista = []
    for _ in range(n):
        lista.append(random.randint(minimo, massimo))
    return lista

# Calcola la media di una lista di numeri
def calcola_media(valori):
    if len(valori) == 0:
        return 0
    return sum(valori) / len(valori)

# Punto di ingresso principale
def main():
    numeri = genera_lista(10, 1, 100)
    print("Lista generata:", numeri)
    media = calcola_media(numeri)
    print("Media dei valori:", media)

if __name__ == "__main__":
    main()
