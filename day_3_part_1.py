# lista_mea = []
# lista_dublate = []
# elem = input("Introduceti valoare: ")
# while elem:
#     lista_mea.append(int(elem))
#     # lista_dublate.append(int(elem) * 2)
#     elem = input("Introduceti valoare: ")
# print(lista_mea)
# # for val in lista_mea:
# #     lista_dublate.append(val * 2)
#
#
#
# lista_dublate = [i * 2 for i in lista_mea] #List comprehension
# print(lista_dublate)
# #
# lista_culori = ['rosu', 'galben', 'albastru', 'verde']
# lista_rez = [cuv.upper() for cuv in lista_culori]
# print(lista_rez)
# lista_rez  = [cuv for cuv in lista_culori if len(cuv) == 4]
# print(lista_rez)

# import requests
# # print(requests.__cake__)
# telacad = requests.get("https://telacad.ro")
# print(telacad.content)

# set_initial = {10, 20, "Telecom", "Metro", 10, 20, 1, 2, 3}
# print(set_initial)
# # print(set[1]) seturile nu suporta referirea prin index
# set_1 = set([10, 20, 30, 40, 50, 10, 10, 20, 20])
# print(set_1)
# print(40 in set_1)
# print(50 not in set_initial)
# set_2 = {True, "metro", "castraveti"}
# set_2.add("1")
# set_2.add("element nou")
# set_2.add(30)
# set_2.add(30)
# print(set_2)
# set_2.update([70, 80, 90, 100, 70])
# print(set_2)
# set_2.remove(70)
# # set_2.remove(70) #KeyError daca elementul nu mai exista in set
# set_2.discard(70) #Nu arunca eroare daca elementul nu exista
set_3 = set(["a", "b", "c", 1, 2, 3])
set_4 = set([1, 2, 3, "telecom"])
# print(set_3.pop())
# print(set_3)
print(set_4.intersection(set_3))
print(set_4.difference(set_3))
print(set_3.difference(set_4))
print(set_3.union(set_4))


