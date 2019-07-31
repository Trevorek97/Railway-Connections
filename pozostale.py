from graf import *

'''W TYM MODULE:
*pomocnicza lista miast
*inicjalizacja macierzy
*inicjalizacja pomocniczego słownika indeksy
*algorytm BFS
'''
miasta = ['Kraków',
          'Miechów',
          'Tunel',
          'Kozłów',
          'Kielce',
          'Ostrowiec',
          'Charsznica',
          'Włoszczowa',
          'Częstochowa',
          'Zawiercie',
          'Dąbrowa',
          'Wolbrom',
          'Katowice',
          'Sosnowiec']

liczba_miast=14
macierz = [[0 for k in range(liczba_miast)] for w in range(liczba_miast)]

indeksy={}
setvalue = lambda x: x + 1
def init_indeksy(indeksy):
    i=-1
    for m in miasta:
        indeksy[m]=setvalue(i)
        i=setvalue(i)
    print("Słownik z indekami:", indeksy.items())

def BFS(graf, start, cel):  # Wyszukiwanie połączeń

    odwiedzone = []  # Odwiedzone węzły
    kolejka = [[start]]  # Kolejka ścieżek do sprawdzenia
    while kolejka:  # Pętla dopóki wszystkie możliwe ścieżki nie zostaną sprawdzone
        sciezka = kolejka.pop(0)  # Usuń pierwszy element z kolejki
        # Ostatni węzeł ze ścieżki
        wezel = sciezka[-1]
        if wezel not in odwiedzone:
            sasiedzi = graf[wezel]
            # Przejdź po wszystkich sąsiednich węzłach, zbuduj nową ścieżkę i dodaj ją do kolejki
            for sasiad in sasiedzi:
                nowa_sciezka = list(sciezka)
                nowa_sciezka.append(sasiad)
                kolejka.append(nowa_sciezka)
                # Zwróć ścieżkę jeśli sąsiad = cel
                if sasiad == cel:
                    return nowa_sciezka

                # Oznacz węzeł jako odwiedzony
                odwiedzone.append(wezel)
    # Gdy nie ma ścieżki między węzłami
    return "0"