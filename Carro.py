class Carro:
    ruedas = None
    puertas = None
    color = None
    marca = None

    def __init__(self, ruedas=None, puertas=None, color=None, marca=None):
        self.ruedas = ruedas
        self.puertas = puertas
        self.color = color
        self.marca = marca

    def __str__(self):
        return f"Carro: {self.marca} {self.color} {self.puertas} puertas {self.ruedas} ruedas"

    def __repr__(self):
        return f"Carro({self.ruedas}, {self.puertas}, {self.color}, {self.marca})"

    # metodo para evaluar si dos objetos son iguales
    def __eq__(self, other):
        return self.marca == other.marca and self.color == other.color and self.puertas == other.puertas and self.ruedas == other.ruedas

    def frenar(self):
        print("Frenando")

    def acelerar(self):
        print("Acelerando")

    def girar(self, direccion):
        print(f"Girando hacia {direccion}")
