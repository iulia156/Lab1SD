class Masina:
    def __init__(self, marca, model, tokenMasina, pretAchizitie, pretVanzare):
        self.__marca = marca
        self.__model = model
        self.__tokenMasina = tokenMasina
        self.__pretAchizitie = pretAchizitie
        self.__pretVanzare = pretVanzare

    def profit(self):
        return self.__pretVanzare - self.__pretAchizitie

    def get_marca(self):
        return self.__marca

    def get_model(self):
        return self.__model

    def get_tokenMasina(self):
        return self.__tokenMasina

    def get_pretAchizitie(self):
        return self.__pretAchizitie

    def get_pretVanzare(self):
        return self.__pretVanzare

    def set_marca(self, marca):
        self.__marca = marca

    def set_model(self, model):
        self.__model = model

    def set_tokenMasina(self, tokenMasina):
        self.__tokenMasina = tokenMasina

    def set_pretAchizitie(self, pretAchizitie):
        self.__pretAchizitie = pretAchizitie

    def set_pretVanzare(self, pretVanzare):
        self.__pretVanzare = pretVanzare

    def __str__(self):
        return f"Marca: {self.__marca}, Model: {self.__model}, Token: {self.__tokenMasina}, PretAchizitie: {self.__pretAchizitie}, PretVanzare: {self.__pretVanzare}"

