# Lista 8 Zad. 5
# Napisać program, gdzie zadaniem gracza jest odgadnięcie liczby. 
# Liczba jest wprowadzona na stałe w kodzie. 
# Jeżeli użytkownik poda za dużą liczbę program wyświetli komunikat „Szukana wartość jest mniejsza”. 
# Jeżeli wprowadzi za małą liczbę program wyświetli „Szukana wartość jest większa”. 
# Po odgadnięciu liczby gracz dowiaduje się po ilu próbach udało mu się zakończyć grę.

# Przykład:
# Podaj liczbę: 22
# Szukana wartość jest większa
# Podaj liczbę: 45
# Szukana wartość jest mniejsza
# Podaj liczbę: 42
# Brawo! Odgadłeś liczbę w 3 próbach.

# Przykład 2:
# Podaj liczbę: 42
# Brawo! Odgadłeś liczbę w 1 próbach.


szukana_liczba = 42  # Liczba do odgadnięcia
proby = 0

while True:
    proba = int(input("Podaj liczbę: "))
    proby += 1
    if proba > szukana_liczba:
        print("Szukana wartość jest mniejsza")
    elif proba < szukana_liczba:
        print("Szukana wartość jest większa")
    else:
        print(f"Brawo! Odgadłeś liczbę w {proby} próbach.")
        break