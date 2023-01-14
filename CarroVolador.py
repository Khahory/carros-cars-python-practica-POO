import Carro


# hereda atributos y metodos de la clase Carro
class CarroVolador(Carro.Carro):
    ruedas = 6

    def __init__(self, color, esta_volando=False):
        # super() = todos los metodos y atributos de la clase padre
        super().__init__(color)  # llama al constructor de la clase padre
        self.esta_volando = esta_volando

    def vuela(self):
        print("Volando")
        self.esta_volando = True

    def aterriza(self):
        print("Aterrizando")
        self.esta_volando = False
