from pozostale import *
from PyQt5.QtWidgets import QMessageBox

'''W TYM MODULE:
*graf wraz z jego wstępną inicjalizacją wybranymi trasami
*funkcje dodające i odejmujące trasy
*sprawdzanie istnienia trasy
'''


graf = {'Kraków': [],
        'Miechów': [],
        'Tunel': [],
        'Kozłów':[],
        'Kielce': [],
        'Ostrowiec': [],
        'Charsznica': [],
        'Włoszczowa': [],
        'Częstochowa':[],
        'Zawiercie': [],
        'Dąbrowa': [],
        'Wolbrom': [],
        'Katowice':[],
        'Sosnowiec': []}

def dodaj_polaczenie(graf, miastoA, miastoB):
    graf[miastoA].append(miastoB)
    graf[miastoB].append(miastoA)
    indA=indeksy[miastoA]
    indB=indeksy[miastoB]
    macierz[indA][indB]=1
    macierz[indB][indA]=1
    #print(indA, indB)

def usun_polaczenie(graf, miastoA, miastoB):
    pom = graf[miastoA]  # Usuwanie wartości w kluczu miastoA
    graf[miastoA] = []
    for i in range(0, len(pom)):
        if (pom[i] != miastoB):
            graf[miastoA].append(pom[i])
    pom = graf[miastoB]  # Usuwanie wartości w kluczu miastoB
    graf[miastoB] = []
    for i in range(0, len(pom)):
        if (pom[i] != miastoA):
            graf[miastoB].append(pom[i])
    indA = indeksy[miastoA]
    indB = indeksy[miastoB]
    macierz[indA][indB] = 0
    macierz[indB][indA] = 0

def czyistnieje(miastoA, miastoB):
    pom=graf[miastoA]
    for i in range(0,len(pom)):
        if pom[i]==miastoB:
            return True
    return False

def inicjalizuj_graf():
    dodaj_polaczenie(graf, "Kraków", "Zawiercie")
    dodaj_polaczenie(graf, "Kraków", "Miechów")
    dodaj_polaczenie(graf, "Miechów", "Tunel")
    dodaj_polaczenie(graf, "Kozłów", "Tunel")
    dodaj_polaczenie(graf, "Charsznica", "Tunel")
    dodaj_polaczenie(graf, "Kielce", "Kozłów")
    dodaj_polaczenie(graf, "Ostrowiec", "Kozłów")
    dodaj_polaczenie(graf, "Ostrowiec", "Częstochowa")
    dodaj_polaczenie(graf, "Włoszczowa", "Charsznica")
    dodaj_polaczenie(graf, "Wolbrom", "Charsznica")
    dodaj_polaczenie(graf, "Włoszczowa", "Częstochowa")
    dodaj_polaczenie(graf, "Dąbrowa", "Zawiercie")
    dodaj_polaczenie(graf, "Dąbrowa", "Katowice")
    dodaj_polaczenie(graf, "Dąbrowa", "Wolbrom")
    print("Nastapila wstepna inicjalizacja grafu")

