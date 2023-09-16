from Clases import saludo,Person
import random
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nombres = []
    apellidos = []
    edades = []

    listNom = ["Emanuel", "Santiago", "Mariano", "Exequiel", "Jorgelina", "Sofia", "Pamela"]
    listApe = ["Del Moro", "Cortez", "Palacios", "Rojo", "Menem", "Raguzzi", "David"]
    i = 0
    clientes=[]
    # listEd = [, 24, 74, 44, 34, 21, 14]
    for x in listNom:

        info = saludo(random.choice(listNom), random.choice(listApe), random.randint(17, 80))
        info.guardar(clientes)
        i += 1

    saludo.data_csv(clientes)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
