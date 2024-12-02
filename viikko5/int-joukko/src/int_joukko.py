KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def _kasvata_listaa(self):
        uusi_lista = self._luo_lista(len(self.ljono) + self.kasvatuskoko)
        uusi_lista[:self.alkioiden_lkm] = self.ljono
        self.ljono = uusi_lista
    
    def _siirra_alkiot_vasemmalle(self, kohta):
        for i in range(kohta, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0 

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if kapasiteetti is not None else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko is not None else OLETUSKASVATUS

        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti <= 0:
            raise ValueError("Kapasiteetin tulee olla positiivinen kokonaisluku.")
        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko <= 0:
            raise ValueError("Kasvatuskoon tulee olla positiivinen kokonaisluku.")
        
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            if self.alkioiden_lkm >= len(self.ljono):
                self._kasvata_listaa()
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, luku):
        if luku not in self.ljono[:self.alkioiden_lkm]:
            return False
        
        kohta = self.ljono[:self.alkioiden_lkm].index(luku)
        
        self._siirra_alkiot_vasemmalle(kohta)
        self.alkioiden_lkm -= 1
        
        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(joukko1, joukko2):
        tulos = IntJoukko()
        for luku in joukko1.to_int_list():
            tulos.lisaa(luku)
        for luku in joukko2.to_int_list():
            tulos.lisaa(luku)
        return tulos

    @staticmethod
    def leikkaus(joukko1, joukko2):
        tulos = IntJoukko()
        joukko2_taulu = joukko2.to_int_list()
        for luku in joukko1.to_int_list():
            if luku in joukko2_taulu:
                tulos.lisaa(luku)
        return tulos

    @staticmethod
    def erotus(joukko1, joukko2):
        tulos = IntJoukko()
        joukko2_taulu = joukko2.to_int_list()
        for luku in joukko1.to_int_list():
            if luku not in joukko2_taulu:
                tulos.lisaa(luku)
        return tulos

    def __str__(self):
        luvut = ", ".join(str(luku) for luku in self.ljono[:self.alkioiden_lkm])
        return f"{{{luvut}}}"
