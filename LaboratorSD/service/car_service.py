from domain.masina import Masina

class CarService:
    @staticmethod
    def comparator(masina1, masina2, criteriu):

        if criteriu == "tokenMasina":
            return masina1.get_tokenMasina() > masina2.get_tokenMasina()

        elif criteriu == "marca_model":
            return (masina1.get_marca(), masina1.get_model()) > (masina2.get_marca(), masina2.get_model())

        elif criteriu == "marca_model_token":
            return (masina1.get_marca(), masina1.get_model(), masina1.get_tokenMasina()) > (masina2.get_marca(), masina2.get_model(), masina2.get_tokenMasina())

        elif criteriu == "profit":
            return masina1.profit() > masina2.profit()

        return False

    @staticmethod
    def bubble_sort(masini, criteriu):

        n = len(masini)

        for i in range(n):

            swapped = False

            for j in range(0, n - i - 1):

                if CarService.comparator(masini[j], masini[j + 1], criteriu):
                    masini[j], masini[j + 1] = masini[j + 1], masini[j]
                    swapped = True

            if not swapped:
                break

        return masini

    @staticmethod
    def binary_search(cars, token):

        left = 0
        right = len(cars) - 1

        while left <= right:
            middle = (left + right) // 2

            if cars[middle].get_tokenMasina() == token:
                return middle

            elif cars[middle].get_tokenMasina() > token:
                right = middle - 1

            else:
                left = middle + 1

        return -1