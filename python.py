import threading
import time

class ReservationSystem:
    def __init__(self):
        self.women_services = ["Strzyżenie 30 zł", "Farbowanie 150 zł", "Modelowanie 100 zł", "Keratynowe prostowanie 100 zł", "Zabiegi pielęgnacyjne 80 zł"]
        self.men_services = ["Strzyżenie 30 zł", "Golenie 20 zł", "Modelowanie brody 100 zł", "Farbowanie 50 zł", "Zabiegi pielęgnacyjne 80 zł"]
        self.available_dates = {
            "Damskie": {
                "Maj": ["10.05", "15.05", "20.05", "25.05", "30.05"],
                "Czerwiec": [],
                "Lipiec": ["05.07", "10.07", "15.07", "20.07", "25.07"]
            },
            "Męskie": {
                "Maj": ["12.05", "17.05", "22.05", "27.05", "31.05"],
                "Czerwiec": [],
                "Lipiec": ["07.07", "12.07", "17.07", "22.07", "27.07"]
            }
        }

    def display_menu(self):
        print("Witaj w systemie rezerwacji usług fryzjerskich!")
        print("Wybierz dla kogo chcesz zarezerwować usługę:")
        print("1. Damskie")
        print("2. Męskie")

    def get_user_choice(self):
        choice = input("Twój wybór (1-2): ")
        while choice not in ["1", "2"]:
            choice = input("Wybierz opcję 1 lub 2: ")
        return choice

    def display_services(self, choice):
        if choice == "1":
            print("Dostępne usługi dla kobiet:")
            for i, service in enumerate(self.women_services, start=1):
                print(f"{i}. {service}")
        elif choice == "2":
            print("Dostępne usługi dla mężczyzn:")
            for i, service in enumerate(self.men_services, start=1):
                print(f"{i}. {service}")

    def get_service_choice(self, choice):
        if choice == "1":
            services = self.women_services
        elif choice == "2":
            services = self.men_services

        service_choice = input("Wybierz numer usługi: ")
        while not service_choice.isdigit() or int(service_choice) < 1 or int(service_choice) > len(services):
            service_choice = input("Podaj prawidłowy numer usługi: ")
        return services[int(service_choice) - 1]

    def display_available_months(self, choice):
        print("Dostępne miesiące rezerwacji:")
        if choice == "1":
            print("1. Maj")
            print("2. Czerwiec")
            print("3. Lipiec")
        elif choice == "2":
            print("1. Maj")
            print("2. Czerwiec")
            print("3. Lipiec")

    def get_month_choice(self):
        month_choice = input("Wybierz numer miesiąca: ")
        while not month_choice.isdigit() or int(month_choice) < 1 or int(month_choice) > 3:
            month_choice = input("Podaj prawidłowy numer miesiąca: ")
        return month_choice

    def display_available_dates(self, choice, service, month_choice):
        months = ["Maj", "Czerwiec", "Lipiec"]
        month = months[int(month_choice) - 1]
        dates = self.available_dates["Damskie"][month] if choice == "1" else self.available_dates["Męskie"][month]

        print(f"Dostępne terminy dla {service} w {month}:")
        for i, date in enumerate(dates, start=1):
            print(f"{i}. {date}")

    def get_date_choice(self, choice, service, month_choice):
        months = ["Maj", "Czerwiec", "Lipiec"]
        month = months[int(month_choice) - 1]
        dates = self.available_dates["Damskie"][month] if choice == "1" else self.available_dates["Męskie"][month]

        date_choice = input("Wybierz numer terminu: ")
        while not date_choice.isdigit() or int(date_choice) < 1 or int(date_choice) > len(dates):
            date_choice = input("Podaj prawidłowy numer terminu: ")
        return dates[int(date_choice) - 1]

    def make_reservation(self, choice, service, month_choice, date):
        months = ["Maj", "Czerwiec", "Lipiec"]
        month = months[int(month_choice) - 1]

        if choice == "1":
            self.available_dates["Damskie"][month].remove(date)
        elif choice == "2":
            self.available_dates["Męskie"][month].remove(date)

        print("Rezerwacja została dokonana. Dziękujemy!")

    def run(self):
        self.display_menu()
        user_choice = self.get_user_choice()
        self.display_services(user_choice)

        service_choice = self.get_service_choice(user_choice)
        self.display_available_months(user_choice)
        month_choice = self.get_month_choice()

        if month_choice == "2" and not self.available_dates["Damskie"]["Czerwiec"] and not self.available_dates["Męskie"]["Czerwiec"]:
            print("Wszystkie terminy w czerwcu są zajęte. Dostępne terminy są w maju i lipcu.")
            month_choice = input("Wybierz numer miesiąca (1 - maj, 3 - lipiec): ")
            while month_choice not in ["1", "3"]:
                month_choice = input("Podaj prawidłowy numer miesiąca (1 - maj, 3 - lipiec): ")

        self.display_available_dates(user_choice, service_choice, month_choice)
        date_choice = self.get_date_choice(user_choice, service_choice, month_choice)

        self.make_reservation(user_choice, service_choice, month_choice, date_choice)


if __name__ == "__main__":
    reservation_system = ReservationSystem()
    reservation_system.run()