from domain.masina import Masina
from service.car_service import CarService
from ui.console import CarManager


# masini = list()
#
# file = open("masini", "r")
# for line in file:
#     data = line.split(" ")
#     data[3] = int(data[3])
#     data[4] = int(data[4])
#     masini.append(Masina(*data))
#
# for masina in masini:
#     print(masina)

def main():
    car_service = CarService()
    car_manager = CarManager(car_service)
    car_manager.run_console()

main()