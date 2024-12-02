from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
        }

        self._viimeisin_komento = None

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=self._kumoa_komento
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()
    
    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._viimeisin_komento = komento_olio
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

    def _kumoa_komento(self):
        if self._viimeisin_komento:
            self._viimeisin_komento.kumoa()
            self._arvo_var.set(self._sovelluslogiikka.arvo())

        if not self._viimeisin_komento:
            self._kumoa_painike["state"] = constants.DISABLED

class Summa:
    def __init__(self, sovelluslogiikka, syote_lukija):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_lukija = syote_lukija
        self._edellinen_tila = sovelluslogiikka.arvo()

    def suorita(self):
        try:
            arvo = int(self._syote_lukija())
            self._edellinen_tila = self._sovelluslogiikka.arvo()
            self._sovelluslogiikka.plus(arvo)
        except ValueError:
            pass

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_tila)

class Erotus:
    def __init__(self, sovelluslogiikka, syote_lukija):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_lukija = syote_lukija
        self._edellinen_tila = sovelluslogiikka.arvo() 

    def suorita(self):
        try:
            arvo = int(self._syote_lukija())
            self._edellinen_tila = self._sovelluslogiikka.arvo()
            self._sovelluslogiikka.miinus(arvo)
        except ValueError:
            pass

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_tila)

class Nollaus:
    def __init__(self, sovelluslogiikka, syote_lukija):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote_lukija = syote_lukija
        self._edellinen_tila = sovelluslogiikka.arvo()

    def suorita(self):
        self._edellinen_tila = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_tila)