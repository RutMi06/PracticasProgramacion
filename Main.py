from Herencia.HerenciaSuperClase import Suma, Resta, Division


def main():
    Numero = Suma(100, 245, 345)
    print(Numero.getSonIguales())
    print(" ")

    Numero = Resta(245, 100, 145)
    print(Numero.getSonIguales())
    print(" ")

    Numero = Division(245, 100, 45)
    print(Numero.getSonIguales())
    print(" ")


if __name__ == "__main__":
    main()