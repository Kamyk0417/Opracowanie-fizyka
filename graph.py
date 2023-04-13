import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Raw Data.csv')            #Do tej linijki otworzenie w pythonie tabeli z pomiarami z aplikacji

acc = []            #pusta lista gdzie będą wszystkie pomiary przyspieszenia
time = []           #-||- czasu

for row in range(1320, len(df.index)):          #dodanie danych z tabeli do powyższych list (1. indeks zgodny z 1. indeksem w głównym pliku
    acc.append(df.iloc[row][4])
    time.append(df.iloc[row][0])

plt.plot(time, acc)             #Wykres otrzymany z aplikacji

plt.xlabel('Time')
plt.ylabel("Acceleration")
plt.grid()
plt.show()
