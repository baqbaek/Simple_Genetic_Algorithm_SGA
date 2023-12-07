import random


class Osobnik:
    def __init__(self, dlugosc_genotypu):
        # Inicjalizacja genotypu losowymi wartościami z przedziału 1 do 255
        self.genotyp = [random.choice([0, 1]) for _ in range(dlugosc_genotypu)]
        while int(''.join(map(str, self.genotyp)), 2) == 0:
            self.genotyp = [random.choice([0, 1]) for _ in range(dlugosc_genotypu)]
        self.wartosc = 0  # Wartość funkcji celu dla danego osobnika

    def reprezentacja_dziesietna(self):
        # Reprezentacja dziesiętna genotypu
        return int(''.join(map(str, self.genotyp)), 2)


def funkcja_kwadratowa(osobnik, a, b, c):
    # Konwersja genotypu na liczbę dziesiętną
    x = int(''.join(map(str, osobnik.genotyp)), 2)
    # Wartość funkcji celu dla danego osobnika (fun. kwadratowa)
    return a * x ** 2 + b * x + c


def inicjalizuj_populacje(rozmiar_populacji, dlugosc_genotypu):
    # Inicjalizacja populacji nowymi osobnikami z genotypami w przedziale 1-255
    return [Osobnik(dlugosc_genotypu) for _ in range(rozmiar_populacji)]


def krzyzowanie(rodzic1, rodzic2, prawdopodobienstwo_krzyzowania):
    # Krzyżowanie genotypów rodziców w punkcie przecięcia
    if random.random() < prawdopodobienstwo_krzyzowania:
        punkt_krzyzowania = random.randint(0, min(len(rodzic1.genotyp), len(rodzic2.genotyp)) - 1)
        # Zamiana fragmentów genotypów między rodzicami
        rodzic1.genotyp[punkt_krzyzowania:], rodzic2.genotyp[punkt_krzyzowania:] = \
            rodzic2.genotyp[punkt_krzyzowania:], rodzic1.genotyp[punkt_krzyzowania:]


def mutacja(osobnik, prawdopodobienstwo_mutacji):
    # Mutacja genotypu z określonym prawdopodobieństwem
    for i in range(len(osobnik.genotyp)):
        if random.random() < prawdopodobienstwo_mutacji:
            osobnik.genotyp[i] = 1 - osobnik.genotyp[i]

def dostosuj_do_funkcji_ujemnej(populacja, a, b, c):
    # Dodanie stałej do wartości funkcji celu, aby uniknąć wartości ujemnych
    min_value = min(funkcja_kwadratowa(osobnik, a, b, c) for osobnik in populacja)
    for osobnik in populacja:
        osobnik.wartosc += abs(min_value)

def selekcja(populacja, a, b, c):
    # Sortowanie populacji według wartości funkcji celu (malejąco)
    dostosuj_do_funkcji_ujemnej(populacja, a, b, c)
    populacja.sort(key=lambda osobnik: funkcja_kwadratowa(osobnik, a, b, c), reverse=True)


def zapisz_wyniki_do_pliku(plik, osobnik, iteracja):
    # Zapis wyników do pliku tekstowego w reprezentacji binarnej i dziesiętnej
    genotyp_binarny = ''.join(map(str, osobnik.genotyp))
    genotyp_dziesietny = osobnik.reprezentacja_dziesietna()

    plik.write(
        f"Generacja {iteracja + 1}: Genotyp: {genotyp_binarny}({genotyp_dziesietny}) Wartość: {osobnik.wartosc}\n")


def main():
    random.seed()
    a = 1
    b = -250
    c = 10000
    ile_iteracji = 40
    #y = a * -250x + 10000

    liczba_populacji = int(input("Podaj liczbę populacji: "))
    prawdopodobienstwo_krzyzowania = float(input("Podaj prawdopodobieństwo krzyżowania (0-1): "))
    prawdopodobienstwo_mutacji = float(input("Podaj prawdopodobieństwo mutacji (0-1): "))

    populacja = inicjalizuj_populacje(liczba_populacji, 8)

    with open("wyniki_ssi_kubiczek.txt", "w", encoding="utf-8") as plik_wyjsciowy:
        for iteracja in range(ile_iteracji):
            for osobnik in populacja:
                osobnik.wartosc = funkcja_kwadratowa(osobnik, a, b, c)

            selekcja(populacja, a, b, c)
            zapisz_wyniki_do_pliku(plik_wyjsciowy, populacja[0], iteracja)

            for i in range(0, liczba_populacji - 1, 2):  # Zmiana zakresu pętli
                krzyzowanie(populacja[i], populacja[i + 1], prawdopodobienstwo_krzyzowania)
                mutacja(populacja[i], prawdopodobienstwo_mutacji)
                mutacja(populacja[i + 1], prawdopodobienstwo_mutacji)

    print(f"Najlepszy osobnik: {''.join(map(str, populacja[0].genotyp))}")
    print(f"Wartość funkcji kwadratowej: {populacja[0].wartosc}")
    print(f"Wartość dziesiętna najlepszego osobnika: {populacja[0].reprezentacja_dziesietna()}")


if __name__ == "__main__":
    main()
