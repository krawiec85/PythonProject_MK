class Ptak:
    '''
    Klasa opisująca ptaka w Pythonie.
    '''

    def __init__(self, gatunek, szybkość):
        self.gatunek = gatunek
        self.szybkość = szybkość

    def latam(self):
        print('Tu', self.gatunek, 'Lecę z szybkością', self.szybkość)

class Kura(Ptak):
    '''
    Tu Kura
    '''

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print('Tu', self.gatunek, 'Ja nie latam')

or1 = Ptak("Orzeł", 45)
or1.latam() # Tu Orzeł Lecę z szybkością 45

kur1 = Ptak("Kura", 0)
kur1.latam() # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam() # Tu Kura domowa Ja nie latam