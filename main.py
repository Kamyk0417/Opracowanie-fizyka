import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Raw Data.csv')
pd.set_option('display.max_rows', None)             #Do tej linijki otwarcie w pythonie pliku z pomiarami w aplikacji

df = df.drop(df[df["Absolute acceleration (m/s^2)"] < 2].index)             #pozbycie się pomiarów, gdzie przyspieszenie jest mniejsze od 2 (wyjaśnienie na kartce)

print(df.to_string())           #kontrolne wyświetlenie tabeli z pomiarami

mass = 74.2             #zmienna mass o wartości masy osoby wykonującej doświadczenie
results = []            #pusta lista do której będą dodawane moce chwilowe dla poszczególnych pomiarów

for i in range(1, len(df.index)):       #pętla wykonuje się tyle razy ile pomiarów wykonaliśmy o zmiennej i z każdym powtórzeniem pętli większej o 1
    sum = 0                             #suma będąca częścią wyznaczonego wzoru
    if df.iloc[i][4] < 2.06: break      #pętla się przerywa gdy pomiar przyspieszenia i-tego pomiaru będzie mniejszy od 2.06 (wyjaśnienie na kartce)
    for j in range(1, i):               #ta i następna linijka - obliczanie sumy (z wyznaczonego wzoru) od pierwszego do i-tego pomiaru
        sum += (df.iloc[j][0] - df.iloc[j-1][0]) * df.iloc[j][4]
    Pch = mass * df.iloc[i][4] * sum            #Obliczanie chwilowej mocy dla i-tego pomiaru wg wyznaczonego wzoru
    results.append(Pch)         #Dodanie chwilowej mocy i-tego pomiaru do listy

print(results)          #Wyświetlenie listy ze wszystkimi mocami
print(max(results))         #Znalezienie maksymalnej wartości
time = [x for x in range(len(results))]         #ponumerowanie otrzymanych mocy, w następnych linijkach interpretacja geometryczna otrzymanych wyników

plt.plot(time, results, color='g')

plt.xlabel('Measurements')
plt.ylabel("Power")
plt.grid()
plt.show()



