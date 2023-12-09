import random

# Parametry funkcji kwadratowej
a = -1
b = 250
c = -10000

# Funkcja do wypisywania bitów liczby binarnej
def drukuj_bity(n):
    bity = 2 * n.bit_length()
    tmp = [str((n >> i) & 1) for i in range(bity - 1, -1, -1)]
    print(''.join(tmp))

# Funkcja do negacji bitów liczby binarnej
def odwroc_bity(n):
    return ~n & ((1 << n.bit_length()) - 1)

# Funkcja generująca losową liczbę z zakresu
def losowa_liczba(min_val=0, max_val=255):
    return random.randint(min_val, max_val)

# Funkcja konwertująca liczbę binarną na dziesiętną
def binarna_na_dziesietna(binary_string):
    decimal, i = 0, 0
    for bit in reversed(binary_string):
        decimal += int(bit) * (2 ** i)
        i += 1
    return decimal

# Funkcja krzyżowania dwóch liczb binarnych
def krzyzowanie_binarnych(num1, num2, pc):
    # Określanie liczby bitów dla obu liczb
    bity = max(num1.bit_length(), num2.bit_length())
    # Tworzenie listy bitów dla krzyżowania
    tmp = [str((num1 >> i) & 1) for i in range(max(bity - pc, 0), bity)]
    tmp.extend([str((num2 >> i) & 1) for i in range(bity - pc - 1, -1, -1)])
    # Konwersja z powrotem na liczbę dziesiętną
    num_in_decimal = binarna_na_dziesietna(''.join(tmp))
    return num_in_decimal

# Funkcja kwadratowa
def funkcja_kwadratowa(x):
    return a * x**2 + b * x + c

# Funkcja selekcji ruletkowej
def selekcja_ruletkowa(osoby_lista):
    # Przesunięcie funkcji kwadratowej w górę, aby uwzględnić wartości ujemne
    f_suma = sum(funkcja_kwadratowa(x) + 5626 for x in osoby_lista)

    # Obliczanie prawdopodobieństwa wyboru każdego osobnika
    osoby_prawdopodobienstwo_lista = [
        (funkcja_kwadratowa(x) + 5626) / f_suma for x in osoby_lista
    ]

    selected = []
    for _ in range(len(osoby_lista)):
        random_num = random.random()
        temp_counter = 0
        # Wybieranie osobników na podstawie ruletki
        for i, prob in enumerate(osoby_prawdopodobienstwo_lista):
            temp_counter += prob
            if temp_counter > random_num:
                selected.append(osoby_lista[i])
                break

    osoby_lista[:] = selected

# Główna funkcja algorytmu genetycznego
def main(ile_wyn, lb_pop, ile_os, pr_krzyz, pr_mut):
    najlepsze_wyniki = [0] * ile_wyn
    plik_wynikowy = open("wyniki.txt", "w")

    for uruchomienie_programu in range(ile_wyn):
        populacja_osobnikow = [losowa_liczba() for _ in range(ile_os)]

        for numer_populacji in range(lb_pop):
            random.shuffle(populacja_osobnikow)

            for indeks_pary in range(0, ile_os, 2):
                # Krzyżowanie z określoną szansą
                if losowa_liczba(0, 1000) <= pr_krzyz * 1000 and indeks_pary + 1 < len(populacja_osobnikow):
                    punkt_krzyzowania = losowa_liczba(1, 7)
                    nowy_osobnik1 = krzyzowanie_binarnych(populacja_osobnikow[indeks_pary], populacja_osobnikow[indeks_pary + 1], punkt_krzyzowania)
                    nowy_osobnik2 = krzyzowanie_binarnych(populacja_osobnikow[indeks_pary + 1], populacja_osobnikow[indeks_pary], punkt_krzyzowania)
                    populacja_osobnikow[indeks_pary] = nowy_osobnik1
                    populacja_osobnikow[indeks_pary + 1] = nowy_osobnik2

                # Mutacja z określoną szansą
                if losowa_liczba(0, 1000) <= pr_mut * 1000:
                    populacja_osobnikow[indeks_pary] = odwroc_bity(populacja_osobnikow[indeks_pary])

                if losowa_liczba(0, 1000) <= pr_mut * 1000:
                    populacja_osobnikow[indeks_pary + 1] = odwroc_bity(populacja_osobnikow[indeks_pary + 1])

            # Selekcja ruletkowa
            selekcja_ruletkowa(populacja_osobnikow)

        # Zapisywanie wyników do pliku
        najlepsze_wyniki[uruchomienie_programu] = max(populacja_osobnikow, key=funkcja_kwadratowa)
        plik_wynikowy.write(f"{funkcja_kwadratowa(najlepsze_wyniki[uruchomienie_programu])}\t  {najlepsze_wyniki[uruchomienie_programu]}\n")

    # Znajdowanie najlepszego wyniku spośród wszystkich prób
    najlepszy_wynik_globalny = max(najlepsze_wyniki, key=funkcja_kwadratowa)
    plik_wynikowy.close()
    return najlepszy_wynik_globalny

# Wywołanie głównej funkcji
if __name__ == "__main__":
    # Ustawienia parametrów
    ile_wyn = 40
    lb_pop = 10
    ile_os = 12
    pr_krzyz = 0.8
    pr_mut = 0.1

    wynik = main(ile_wyn, lb_pop, ile_os, pr_krzyz, pr_mut)
    print(f"Najlepszy x: {wynik}\nNajlepszy f(x): {funkcja_kwadratowa(wynik)}")
