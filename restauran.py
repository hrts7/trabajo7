class restaurante():
    def __init__(self, nombre, comida):
        self.nombre= nombre
        self.comida= comida
        self.estado= "cerrado"

    def describir_res(self):
        print(f"Restaurante: {self.nombre}")
        print(f"Tipo de comida: {self.comida}")

    def abrir_res(self):
        if self.estado == "cerrado":
            print(f"el restaurante {self.nombre} esta abierto ")
            self.estado= "abierto"
        else:
            print("ya esta abierto! ")


class heladeria(restaurante):
    def __init__(self, nombre, comida):
        super().__init__(nombre, comida)
        self.sabores= []

    def los_sabor(self):
        if self.sabores:
            print("Sabores disponibles: ")
            for sabor in self.sabores:
                print(f"- {sabor}")
        else:
            print("no hay sabores disponibles. ")

