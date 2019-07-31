from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout, QComboBox
from PyQt5.QtWidgets import QLineEdit, QPushButton
import sys
from graf import *
from pozostale import *

'''W TYM MODULE:
*obsługa okienek
*obsługa wyjątków/blędów
'''


class MyException(Exception):
    def __init__(self, info):
        self.info = info
    def __str__(self):
        return str(self.info)

init_indeksy(indeksy)
inicjalizuj_graf()

class Okno_pierwsze(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.okno3 = Okno_macierz()
        self.okno3.show()
        self.interfejs()

    def interfejs(self):

        # ETYKIETY
        etykieta1 = QLabel("PIERWSZE MIASTO:", self)
        etykieta2 = QLabel("DRUGIE MIASTO:", self)

        # PRZYPISANIE WIDGETÓW DO UKŁADU TABELARYCZNEGO
        uklad_tabelaryczny = QGridLayout()
        uklad_tabelaryczny.addWidget(etykieta1, 1, 1)
        uklad_tabelaryczny.addWidget(etykieta2, 1, 4)

        # LINIOWE POLA EDYCYJNE
        self.miastoA = QLineEdit()
        self.miastoB = QLineEdit()

        # UMIESZCZENIE NA UKŁADZIE TABELATYCZNYM
        uklad_tabelaryczny.addWidget(self.miastoA, 2, 0, 1, 3)
        uklad_tabelaryczny.addWidget(self.miastoB, 2, 3, 1, 3)
        pol_przycisk = QPushButton("&POŁĄCZ", self)
        roz_przycisk = QPushButton("&ROZŁĄCZ", self)
        ok_przycisk = QPushButton("&GOTOWE!", self)
        zak_przycisk = QPushButton("&ZAMKNIJ", self)

        pol_przycisk.resize(roz_przycisk.sizeHint())
        roz_przycisk.resize(roz_przycisk.sizeHint())
        zak_przycisk.resize(zak_przycisk.sizeHint())
        ok_przycisk.resize(roz_przycisk.sizeHint())

        uklad_tabelaryczny.addWidget(pol_przycisk, 4, 1, 1, 2)
        uklad_tabelaryczny.addWidget(roz_przycisk, 4, 3, 1, 2)
        uklad_tabelaryczny.addWidget(ok_przycisk, 6, 1, 1, 2)
        uklad_tabelaryczny.addWidget(zak_przycisk, 6, 3, 1, 2)

        # PRZYPISANIE UTWORZONEGO UKŁADU DO OKNA
        self.setLayout(uklad_tabelaryczny)

        # OBSŁUGA PRZYCISKÓW
        pol_przycisk.clicked.connect(self.polaczenie)
        roz_przycisk.clicked.connect(self.polaczenie)
        zak_przycisk.clicked.connect(self.zakoncz)
        ok_przycisk.clicked.connect(self.new_window)

        self.setGeometry(400, 100, 400, 200)
        self.setWindowIcon(QIcon('pociag.png'))
        self.setWindowTitle("Dodawanie połączeń")
        self.show()

    def polaczenie(self):

        nadawca = self.sender()
        miasto_A = str(self.miastoA.text())
        miasto_B = str(self.miastoB.text())
        sprawdzA=sprawdzB=0
        check_and_modify= lambda x: x+1
        for miasto in graf.keys():
            if (miasto_A == miasto):
                sprawdzA=check_and_modify(sprawdzA)
            if (miasto_B == miasto):
                sprawdzB=check_and_modify(sprawdzB)
        try:
            if  sprawdzA==0 and sprawdzB==0:
                raise MyException("oba")
        except MyException as oba:
            QMessageBox.critical(self, "BŁĄD!", "Oba miasta zostały wprowadzone niepoprawnie!")
            return
        try:
            if sprawdzA==0:
                raise MyException("pierwsze")
        except MyException as pierwsze:
            QMessageBox.critical(self, "BŁĄD!", "Pierwsze miasto zostało wprowadzone niepoprawnie!")
            return
        try:
            if sprawdzB==0:
                raise MyException("drugie")
        except MyException as drugie:
            QMessageBox.critical(self, "BŁĄD!", "Drugie miasto zostało wprowadzone niepoprawnie!")
            return
        try:
            if miasto_A==miasto_B:
                raise MyException("identyczne")
        except MyException as identyczne:
            QMessageBox.critical(self, "BŁĄD!", "Wprowadziłeś dwa razy to samo miasto!")
            return
        try:
            if czyistnieje(miasto_A, miasto_B) == True and nadawca.text() == "&POŁĄCZ":
                raise MyException("istnieje")
        except MyException as istnieje:
            QMessageBox.critical(self, "BŁĄD!", "Podana trasa już istnieje!")
            return
        try:
            if czyistnieje(miasto_A,miasto_B)==False and nadawca.text() == "&ROZŁĄCZ":
                raise MyException("nie_istnieje")
        except MyException as nie_istnieje:
            QMessageBox.critical(self,"BŁĄD!", "Nie można skasować nieistniejącego polączenia")
            return

        if nadawca.text() == "&POŁĄCZ":
            dodaj_polaczenie(graf, miasto_A, miasto_B)

            QMessageBox.critical(self, "POŁĄCZENIE", "Utworzono nowe połączenie bezpośrednie!")
            self.okno3 = Okno_macierz()
            self.okno3.show()
            print(graf.keys())
            print(graf.values())
            return

        elif nadawca.text() == "&ROZŁĄCZ":
            usun_polaczenie(graf, miasto_A, miasto_B)
            QMessageBox.critical(self, "POŁĄCZENIE", "Skasowano istniejące połączenie bezpośrednie!")
            self.okno3 = Okno_macierz()
            self.okno3.show()
            print(graf.keys())
            print(graf.values())
            return

    # ZAKOŃCZENIE PROGRAMU - PRZYCISKIEM 'ZAKOŃCZ' I KLAWISZEM ESCAPE
    def zakoncz(self):
        self.okno3.close()
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.okno3.close()
            self.close()

    def new_window(self):
        self.okno2 = Okno_drugie()
        self.okno2.show()



# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#



class Okno_drugie(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs2()

    def interfejs2(self):

        # ETYKIETY
        etykieta1 = QLabel("MIASTO POCZĄTKOWE:", self)
        etykieta2 = QLabel("MIASTO KOŃCOWE:", self)
        etykieta3 = QLabel("ZNALEZIONE POŁĄCZENIE:", self)

        # PRZYPISANIE WIDGETÓW DO UKŁADU TABELARYCZNEGO
        uklad_tabelaryczny = QGridLayout()
        uklad_tabelaryczny.addWidget(etykieta1, 0, 2)
        uklad_tabelaryczny.addWidget(etykieta2, 2, 2)
        uklad_tabelaryczny.addWidget(etykieta3, 4, 2)

        # LINIOWE POLA EDYCYJNE
        self.miasto_startowe = QLineEdit()
        self.miasto_koncowe = QLineEdit()
        self.wynik = QLineEdit()

        self.wynik.readonly = True
        self.wynik.setToolTip('')

        # UMIESZCZENIE NA UKŁADZIE TABELATYCZNYM
        uklad_tabelaryczny.addWidget(self.miasto_startowe, 1, 2)
        uklad_tabelaryczny.addWidget(self.miasto_koncowe, 3, 2)
        uklad_tabelaryczny.addWidget(self.wynik, 5, 2)
        se_przycisk = QPushButton("&SZUKAJ", self)
        end_przycisk = QPushButton("&ZAMKNIJ", self)
        end_przycisk.resize(end_przycisk.sizeHint())
        uklad_tabelaryczny.addWidget(se_przycisk, 6, 1, 1, 2)
        uklad_tabelaryczny.addWidget(end_przycisk, 6, 3, 1, 2)

        # PRZYPISANIE UTWORZONEGO UKŁADU DO OKNA
        self.setLayout(uklad_tabelaryczny)

        # OBSŁUGA PRZYCISKÓW
        end_przycisk.clicked.connect(self.zakoncz)
        se_przycisk.clicked.connect(self.szukaj_trasy)

        self.setGeometry(400, 333, 400, 200)
        self.setWindowIcon(QIcon('pociag.png'))
        self.setWindowTitle("Wyszukiwarka połączeń kolejowych")
        self.show()

        # STARTOWY NAPIS W POLU ZE ZNALEZIONĄ TRASĄ
        wyniki = ("TU POJAWI SIĘ TWOJE ZNALEZIONE POŁĄCZENIE:")

        self.wynik.setText(str(wyniki))

    # ZAKOŃCZENIE PROGRAMU - PRZYCISKIEM 'ZAKOŃCZ' I KLAWISZEM ESCAPE
    def zakoncz(self):
        self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def szukaj_trasy(self):

        nadawca = self.sender()
        ms = str(self.miasto_startowe.text())
        mk = str(self.miasto_koncowe.text())

        if nadawca.text() == "&SZUKAJ":
            podroz = ""
            if ms == "" or mk == "":  # SPRAWDZENIE CZY POLA NIE SĄ PUSTE
                podroz = "UZUPEŁNIJ BRAKUJĄCE MIASTA!"
                self.wynik.setText(str(podroz))
                return

            spr_ms = 0  # SPRAWDZENIE CZY WPROWADZONE MIASTA ISTNIEJĄ
            spr_mk = 0
            check_and_modify=lambda x: x+1

            for k in graf.keys():
                if ms == k:
                    spr_ms=check_and_modify(spr_ms)
                if mk == k:
                    spr_mk =check_and_modify(spr_mk)

            if spr_ms==0:
                podroz = "MIASTO POCZATKOWE NIE ISTNIEJE!"
                self.wynik.setText(str(podroz))
                return
            if spr_mk==0:
                podroz = "MIASTO KOŃCOWE NIE ISTNIEJE!"
                self.wynik.setText(str(podroz))
                return

            if ms == mk:  # SPRAWDZENIE CZY OBA MIASTA NIE SĄ IDENTYCZNE
                podroz = "MIASTO STARTOWE MUSI BYĆ INNE NIŻ KOŃCOWE!"
                self.wynik.setText(str(podroz))
                return

            trasy = list(BFS(graf, ms, mk))  # SPRAWDZENIE CZY ISTNIEJE DANE POĄCZENIE
            if (trasy[0] == "0"):
                podroz = "ZADANE POŁĄCZENIE NIE ISTNIEJE!"
                self.wynik.setText(str(podroz))
                return

            for i in range(0, len(trasy)):
                podroz += trasy[i]
                if i != len(trasy) - 1:
                    podroz += "->"
        if len(trasy) == 2:
            QMessageBox.critical(self, "SUKCES!", "Znaleziono połączenie bezpośrednie!")
        else:
            QMessageBox.critical(self, "SUKCES!", "Znaleziono połączenie wymagające przesiadki!")
        self.wynik.setText(str(podroz))
        return



# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#



class Okno_macierz(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):
        uklad_tabelaryczny = QGridLayout()
        self.setLayout(uklad_tabelaryczny)

        macierz_miasta_v = ""
        macierz_dane_v = ""
        for w in range(0, liczba_miast):
            macierz_miasta_v = macierz_miasta_v + miasta[w] + "\n"
            for k in range(0, liczba_miast):
                macierz_dane_v = macierz_dane_v + " " + str(macierz[w][k]) + " "
            macierz_dane_v += "\n"
        macierz_dane = QPushButton(macierz_dane_v, self)
        macierz_miasta = QPushButton(macierz_miasta_v, self)

        uklad_tabelaryczny.addWidget(macierz_dane, 1, 2, 13, 6)
        uklad_tabelaryczny.addWidget(macierz_miasta, 1, 0, 13, 1)

        self.setGeometry(803, 100, 200, 100)
        self.setWindowIcon(QIcon('pociag.png'))
        self.setWindowTitle("Macierz sąsiedztwa")
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            okno.close()
            self.close()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    okno = Okno_pierwsze()
    okno.show()
    sys.exit(app.exec_())