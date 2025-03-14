from domain.masina import Masina
from service.car_service import CarService


class CarManager:
    def __init__(self, service):
        self.service = service
        self.masini = self.citire_fisier()

    def citire_fisier(self):
        masini = []
        try:
            with open("masini", "r") as file:
                for line in file:
                    data = line.split(" ")
                    data[3] = int(data[3])
                    data[4] = int(data[4])
                    masini.append(Masina(*data))
        except FileNotFoundError:
            print("Fisierul 'masini' nu a fost gasit!")
        return masini

    @staticmethod
    def afisare_meniu():
        print("\nMeniu:")
        print("1. Afiseaza masinile")
        print("2. Sorteaza dupa token cu bubble sort")
        print("3. Sorteaza dupa marca si model cu bubble sort")
        print("4. Sorteaza dupa marca, model si token cu bubble sort")
        print("5. Sorteaza dupa profit cu bubble sort")
        print("6. Cauta dupa token cu binary search")
        print("x. Iesire")

    def afisare_masini(self):
        if not self.masini:
            print("Nu exista masini de afisat!")
        else:
            for masina in self.masini:
                print(masina)

    def run_console(self):
        while True:
            self.afisare_meniu()
            optiune = input("Alege o optiune: ")

            if optiune == "1":
                self.afisare_masini()
            elif optiune == "2":
                self.service.bubble_sort(self.masini, "tokenMasina")
                self.afisare_masini()
            elif optiune == "3":
                self.service.bubble_sort(self.masini, "marca_model")
                self.afisare_masini()
            elif optiune == "4":
                self.service.bubble_sort(self.masini, "marca_model_token")
                self.afisare_masini()
            elif optiune == "5":
                self.service.bubble_sort(self.masini, "profit")
                self.afisare_masini()
            elif optiune == "6":
                token = input("Introdu tokenul mașinii căutate: ")
                self.masini = sorted(self.masini, key=lambda x: x.get_tokenMasina())
                result = self.service.binary_search(self.masini, token)
                if result != -1:
                    print(f"Mașina cu tokenul {token} a fost găsită: {self.masini[result]}")
                else:
                    print(f"Mașina cu tokenul {token} nu a fost găsită.")
            elif optiune == "x":
                print("La revedere!")
                break
            else:
                print("Optiune invalida! Incearca din nou.")
