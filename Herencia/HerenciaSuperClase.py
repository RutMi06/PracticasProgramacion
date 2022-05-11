from abc import ABC


class Numero(ABC):
    _sonIguales = bool("")

    @staticmethod
    def evaluarOperadores():
        pass

    def getSonIguales(self):
        return self._sonIguales

class Suma(Numero):
    __numero1 = int(0)
    __numero2 = int(0)
    __numero3 = int(0)

    def __init__(self, numero1, numero2, numero3):
        if numero1 < 0 or numero2 < 0 or numero3 < 0:
            self.__numero1 = 0
            self.__numero2 = 0
            self.__numero3 = 0
        else:
            self.__numero1 = numero1
            self.__numero2 = numero2
            self.__numero3 = numero3
        self.evaluarOperadores()

    def evaluarOperadores(self):
        if self.__numero1 + self.__numero2 == self.__numero3:
            self._sonIguales = True
            return self._sonIguales
        else:
            self._sonIguales = False
            return self._sonIguales


class Resta(Numero):
    __numero1 = int(0)
    __numero2 = int(0)
    __numero3 = int(0)

    def __init__(self, numero1, numero2, numero3):
        if numero1 < 0 or numero2 < 0 or numero3 < 0:
            self.__numero1 = 0
            self.__numero2 = 0
            self.__numero3 = 0
        else:
            self.__numero1 = numero1
            self.__numero2 = numero2
            self.__numero3 = numero3
        self.evaluarOperadores()

    def evaluarOperadores(self):
        if self.__numero1 - self.__numero2 == self.__numero3 or self.__numero2 - self.__numero1 == self.__numero3:
            self._sonIguales = True
            return self._sonIguales
        else:
            self._sonIguales = False
            return self._sonIguales


class Division(Numero):
    __numero1 = int(0)
    __numero2 = int(0)
    __numero3 = int(0)

    def __init__(self, numero1, numero2, numero3):
        if numero1 < 0 or numero2 < 0 or numero3 < 0:
            self.__numero1 = 0
            self.__numero2 = 0
            self.__numero3 = 0
        else:
            self.__numero1 = numero1
            self.__numero2 = numero2
            self.__numero3 = numero3
        self.evaluarOperadores()

    def evaluarOperadores(self):
        if self.__numero2 == 0:
            self._sonIguales = False
        elif self.__numero1 % self.__numero2 == self.__numero3 or self.__numero2 % self.__numero1 == self.__numero3:
            self._sonIguales = True
            return self._sonIguales
