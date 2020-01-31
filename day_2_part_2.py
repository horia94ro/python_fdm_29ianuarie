# text = input("Sirul de caractere...")
# if len(text) > 2:
#     rez_1 = text[:2] + text[-2:] # primele si ultimele 2 caractere
#     rez_2 = text[::-1]
#     rez_2 = rez_2[:2]
#     print(rez_1)
#     print(rez_2) #ultimele doua caractere citite de la coada la cap
# else:
#     print("Sir prea scurt")

# sir = input("Introduceti adresa de e-mail: ")
# print(len(sir))
# sir = sir.strip("*$789 ")
# print(len(sir))
# print(sir)
#
# lista_mea = []
# nr = int(input("Cate elemente vrei sa adaugi?"))
# for i in range(0, nr):
#     elem = input("Elementul {}: ".format(i))
#     if elem in lista_mea:
#         print("Elementul e deja adaugat")
#     else:
#         lista_mea.append(elem)
#
# print("Numar elemente unice: {}".format(len(lista_mea)))

lista_mea = ['telecom', 'google', 10, 'metro', 'metro', True, True]
# lista_unice = []
# for element in lista_mea:
#     if element in lista_unice:
#         continue
#     else:
#         lista_unice.append(element)
#         # break
# print(lista_unice)
nr_unice = 0
for elem in lista_mea:
    if lista_mea.count(elem) == 1:
        nr_unice += 1

print(nr_unice)






