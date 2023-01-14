from pprint import pprint

import Carro
import CarroVolador


def comparar_carros():
    comparar_carro_nuevo = Carro.Carro(4, 4, 'rojo', 'Toyota')
    comparar_carro_viejo = Carro.Carro(1, 1, 'rojo', 'Toyota')

    # evaluda si dos carros son iguales
    pprint(comparar_carro_nuevo.__eq__(comparar_carro_viejo))


if __name__ == '__main__':
    carro_nuevo = Carro.Carro(4, 4, 'rojo', 'Toyota')

    # nos vamos para Singapur
    carro_nuevo.acelerar()
    carro_nuevo.frenar()
    carro_nuevo.girar('izquierda')
    carro_nuevo.acelerar()
    carro_nuevo.frenar()
    carro_nuevo.girar('derecha')
    carro_nuevo.acelerar()
    carro_nuevo.frenar()
    pprint('Llegamos a Singapur')

    pprint('---------------------------------')

    pprint('Ahora vamos a volar')
    carro_volador = CarroVolador.CarroVolador('rojo', True)
    carro_volador.vuela()
    carro_volador.aterriza()
    carro_volador.acelerar()
    carro_volador.frenar()

    pprint(carro_volador.__dict__)


