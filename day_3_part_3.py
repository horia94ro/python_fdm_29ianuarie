def patrat(x):
    return x ** 2

def verifica_par(x):
    if x % 2 == 0:
        print("par")
        return
    print('impar')
    # return "impar"
# print(patrat(3))
# print(verifica_par(11))


def suma(a = 0, b = 10):
    # if type(a) != int:
    #     return "A NU ESTE INT"
    return a + b

# print(suma())
# print(suma(7))
# print(suma(7, 20))
# print(suma(a = 10, b = 20))
# print(suma(5, b = 7))
# print(suma("Telecom", " Academy"))
# print(suma([1, 2,3 ], [4, 5, 6]))
# print(suma("Telecom", 10))

def banner_motd(mesaj, delim = "\u2665"):
    """
    Functia afiseaza mesajul formatat frumos
    :param mesaj: Mesajul pe care il doresc afisat
    :param delim: Caracterul cu care fac chenar
    :return: None
    """
    print(delim * len(mesaj))
    print(mesaj)
    print(delim * len(mesaj))

# banner_motd("Buna dimineata")
# banner_motd("Buna seara", "*")
# banner_motd(delim="-", mesaj = "Buna ziua!")

def hypervolume(b, c, *args, d):
    for i in args:
        print(i, end = " ")
    # args[0] = 10
    print(type(args))

# hypervolume(1, 2, 3, 4, 5, d = 10)
# hypervolume(0, 1, d = 15)
# hypervolume(10, 20, d = 20)
# hypervolume("Gheorghe", 10, True, d = 15)

# def functie(name, **kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
#     print(name)
#     print(type(kwargs))
#
# functie("telecom", cheie_1 = 10, cheie_2 = 20, cheie_3 = 30)
# functie("academy")

def minim_lista(*args):
    if len(args) > 0:
        minim = args[0]
        for i in args:
            if i < minim:
                minim = i
        print("Minimul este: ", minim)
    else:
        print("Lista este goala!")

# minim_lista(-2, 4, 7, 10, 23, -99, 100)
# minim_lista(-2, -2)


def minim_lista_2(lista_elemente):
    minim = lista_elemente[0]
    for i in range(1, len(lista_elemente)):
        if lista_elemente[i] < minim:
            minim = lista_elemente[i]
    return minim

print(minim_lista_2([1, 2, 3, -1]))
