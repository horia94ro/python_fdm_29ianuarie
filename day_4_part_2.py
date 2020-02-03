import sys

def citeste_cuvinte(nume_fisier):
    """
    Metoda care citeste dintr-un fisier si returneaza lista cu cuvinte
    :param nume_fisier: Numele fisierului din care citesc
    :return: lista de cuvinte (as a list)   c
    """
    lista = []
    with open(file = nume_fisier) as f:
        for line in f.readlines():
            for cuvant in line.split():
                lista.append(cuvant)
    # afisare(lista)
    return lista

def afisare(lista):
    for elem in lista:
        print(elem, end = "\n")



# print(__name__)

def main(nume_fisier):
    lista_cuvinte = citeste_cuvinte(nume_fisier)
    afisare(lista_cuvinte)

if __name__ == "__main__":
    main(sys.argv[1])