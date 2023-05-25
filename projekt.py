from datetime import datetime

class UslugaFryzjerska:
    def __init__(self, nazwa, czas_trwania):
        self.nazwa = nazwa
        self.czas_trwania = czas_trwania

class Rezerwacja:
    def __init__(self, usluga, data, godzina, klient):
        self.usluga = usluga
        self.data = data
        self.godzina = godzina
        self.klient = klient

class Klient:
    def __init__(self, imie, nazwisko, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

class SalonFryzjerski:
    def __init__(self):
        self.uslugi = []
        self.rezerwacje = []

    def dodaj_usluge(self, usluga):
        self.uslugi.append(usluga)

    def usun_usluge(self, usluga):
        self.uslugi.remove(usluga)

    def dodaj_rezerwacje(self, rezerwacja):
        self.rezerwacje.append(rezerwacja)

    def usun_rezerwacje(self, rezerwacja):
        self.rezerwacje.remove(rezerwacja)

    def wyswietl_wolne_terminy(self):
        print("Wolne terminy:")
        for usluga in self.uslugi:
            for rezerwacja in self.rezerwacje:
                if rezerwacja.usluga == usluga:
                    continue  # Ta usługa ma już zarezerwowany termin
                print(f"- {usluga.nazwa}: {rezerwacja.data} {rezerwacja.godzina}")

    def zarezerwuj_usluge(self, usluga, data, godzina, klient):
        for rezerwacja in self.rezerwacje:
            if rezerwacja.data == data and rezerwacja.godzina == godzina:
                raise Exception("Termin jest już zarezerwowany")
        rezerwacja = Rezerwacja(usluga, data, godzina, klient)
        self.dodaj_rezerwacje(rezerwacja)
        print("Usługa została zarezerwowana")

    def wyswietl_uslugi(self):
        print("Dostępne usługi fryzjerskie:")
        for usluga in self.uslugi:
            print(f"- {usluga.nazwa}: {usluga.czas_trwania} minut")

    def znajdz_rezerwacje(self, klient):
        print(f"Rezerwacje dla klienta {klient.imie} {klient.nazwisko}:")
        for rezerwacja in self.rezerwacje:
            if rezerwacja.klient == klient:
                print(f"- {rezerwacja.usluga.nazwa}: {rezerwacja.data} {rezerwacja.godzina}")

# Tworzenie usług fryzjerskich
usluga1 = UslugaFryzjerska("Strzyżenie męskie", 30)
usluga2 = UslugaFryzjerska("Strzyżenie damskie", 60)
usluga3 = UslugaFryzjerska("Modelowanie", 45)
usluga4 = UslugaFryzjerska("Farbowanie", 90)
usluga5 = UslugaFryzjerska("Prostowanie włosów", 120)
usluga6 = UslugaFryzjerska("Zabiegi pielęgnacyjne", 60)

# Tworzenie salonu fryzjerskiego
salon = SalonFryzjerski()

# Dodawanie usług do salonu
salon.dodaj_usluge(usluga1)
salon.dodaj_usluge(usluga2)
salon.dodaj_usluge(usluga3)
salon.dodaj_usluge(usluga4)
salon.dodaj_usluge(usluga5)
salon.dodaj_usluge(usluga6)

# Tworzenie klientów
klient1 = Klient("Jan", "Kowalski", "123456789")
klient2 = Klient("Anna", "Nowak", "987654321")

# Przykładowe rezerwacje
data_rezerwacji = datetime(2023, 5, 21).date()
godzina_rezerwacji = datetime(2023, 5, 21, 10, 0).time()
try:
    salon.zarezerwuj_usluge(usluga1, data_rezerwacji, godzina_rezerwacji, klient1)
except Exception as e:
    print(str(e))

# Wyświetlanie dostępnych terminów
salon.wyswietl_wolne_terminy()

# Wyświetlanie dostępnych usług
salon.wyswietl_uslugi()

# Znajdowanie rezerwacji dla klienta
salon.znajdz_rezerwacje(klient1)

# Usunięcie usługi z salonu
salon.usun_usluge(usluga2)

# Wyświetlanie dostępnych usług po usunięciu
salon.wyswietl_uslugi()

# Zarezerwowanie innej usługi
data_rezerwacji2 = datetime(2023, 5, 22).date()
godzina_rezerwacji2 = datetime(2023, 5, 22, 15, 0).time()
try:
    salon.zarezerwuj_usluge(usluga3, data_rezerwacji2, godzina_rezerwacji2, klient2)
except Exception as e:
    print(str(e))

# Wyświetlanie wolnych terminów po rezerwacji
salon.wyswietl_wolne_terminy()

# Znajdowanie rezerwacji dla drugiego klienta
salon.znajdz_rezerwacje(klient2)