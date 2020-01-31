# lista_mea = [("Laurentiu", 27), ("Cristi", 32), ("Dani", 25)]
# dictionar = dict(lista_mea)
# dictionar = {
#             'Laurentiu' : 27,
#             'Cristi': 32,
#             'Dani' : 23
#             }
# print(dictionar)
#
# dictionar['Dani'] = 26
# print(dictionar)
#
# dictionar['Robert'] = 34
# print(dictionar)
# dictionar.update({'Dani':27, 'Mihaela':30})
# print(dictionar)
# del dictionar['Laurentiu']
# print(dictionar)
# dictionar[1] = 10
# print(dictionar)
# # dictionar[[1, 2, 3]] = 10
# print(dictionar)
#
#
# print(list(dictionar.keys()))
# print(list(dictionar.values()))
#
# for k, v in dictionar.items():
#     print("Cheia {0} are valoarea {1}".format(k, v))
#
# # print('Dani' in dictionar)
# print(dictionar.get('Andrei', "MESAJ EROARE"))
# d1 = dict(zip((1, 2, 3), ("Andrei", "B", "C"))) #primul tuplu -> cheile; al doilea -> valorile
# print(d1)
# # for k, v in enumerate([1, 2, 3]):
# #     print(k, v)

# line = input("Dati textul: ")
# lista_mea = line.split()
# dictionar = dict()
# # for element in lista_mea:
# #     dictionar.update({element:lista_mea.count(element)})
# #
# # print(dictionar)
#
# for element in lista_mea:
#     if element in dictionar:
#         dictionar[element] += 1
#     else:
#         dictionar[element] = 1
# print(dictionar)
# nr_secunde = 1875460
# # t1 = t1 + (nr_secunde // 86400, (nr_secunde%86400)//3600, (nr_secunde))
# sec_minut = 60
# sec_ora = 60 * sec_minut
# sec_zi = 24 * sec_ora
# sec_saptamana = 7 * sec_zi
# sec_luna = 4 * sec_saptamana
# t1 = (sec_zi, sec_ora, sec_minut)
# t2 = ()
# for val in t1:
#     rez = nr_secunde // val
#     nr_secunde = nr_secunde - rez * val
#     t2 = t2 + (rez, )
# print(t2)
# t3 = ('Zile', 'Ore', 'Minute')
# dictionar = dict(zip(t3, t2))
# print(dictionar)






