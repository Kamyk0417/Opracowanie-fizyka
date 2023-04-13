# Opracowanie-fizyka

W zadaniu miałem obliczyć moc chwilową, na którą miałem wzór P=masa*przyspieszenie*prędkość gdzie prędkość to było pole pod wykresem
W skrócie w pliku Raw Data.csv jest seria bardzo wielu bardzo krótkich pomiarów i przyspiesznie oraz jego składowe x,y,z (nieistotne)

plik pomiary.py po zastanowieniu chyba ważny nie jest
plik graph.py to po prostu przedstawienie tych pomiarów na wykresie (zaczyna się od pomiaru 1320 bo jakoś od wtedy zaczynają się istotne zmiany)
plik main.py:
  - w pewnym momencie ograniczenie a<2 wynika z interpretacji wykresu, że nawet przed pomiarem przyspieszenie dochodziło do 2
  - w pętli for i... liczę moce chwilowe, w for j... liczę sumę pól pod wykresem pod każdym z małych czasów (pomiarów)
  - ograniczenie <2.06 wynika już z odczytania konkretnego pomiaru
  - na koniec jest jeszcze wykres jak się ta moc chwilowa zmienia

Przepraszam jeżeli nie wszystko jest w pełni jasne, nie chciałem się zagłębiać w to co dokładnie się tu dzieje, ważniejszy jest chyba sam kod :)

Pozdrawiam 
Jakub Kamiński

PS Jeżeli kodu jest trochę za mało na sensowną ocenę to mam na githubie jeszcze "projekt" RPGGame, jest on ledwo zaczęty ale parę ciekawych linijek tam jest.
