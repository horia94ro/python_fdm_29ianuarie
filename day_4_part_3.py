# def par_sau_impar(x):
#     if x % 2 == 0:
#         return "True", "PAR"
#     return False, "IMPAR"
#
# rez = par_sau_impar(16)
# print(rez[0])
#
# try:
#     x = 10
#     y = 10 / 1
#     print("A")
#     lista = [1, 2, 3]
#     lista[2] = 10
#     print("D")
#     f = open("t.txt")
#
#     f.close()
#     # print(f.read())
#     # a = int("abc")
#
# except ZeroDivisionError as e:
#     print("Ba, nu mai imparti la 0\n", str(e))
# except IndexError as e:
#     print("Te-ai lovit de un index inexistent", str(e))
# # except ValueError as e:
# #     print("Operatie nepermisa pe fisier", str(e))
# except Exception as e:
#     print("Exceptie generala", e.__repr__())
# else:
#     print("Bloc afisat doar cand lipsesc exceptii!")
# finally:
#     print("Bloc de finally")
#
# print("C")

import sys
def citire(nr_elem):
    lista_elem = list()
    for i in range(0, nr_elem):
        lista_elem.append(input("Elementul {}:".format(i)))
    return lista_elem


def conversie(lista):
    lista_conversii = []
    lista_erori = []
    for elem in lista:
        try:
            elem = float(elem)
            lista_conversii.append(elem)
        except ValueError:
            lista_erori.append(elem)
    return lista_conversii, lista_erori

valorile = citire(int(sys.argv[1]))
rez = conversie(valorile)
print("Lista de conversii: ", rez[0])
print("Lista de erori: ", rez[1])
















