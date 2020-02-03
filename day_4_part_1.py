# alimentare = ['lapte', 'oua', 'castraveti', 'ciocolata']
# electrocasnice = ['televizor', 'telecom', 'radio']
# imobiliare = ['apartament', 'casa', 'garsoniera']
#
# valori_tva = {
#     "alimentare" : 5,
#     "electrocasnice" : 10,
#     "imobiliare" : 19,
#     "rest" : 8,
#     "general" : 10
# }
#
# def calcul_tva(produs, valoare_initiala):
#     val_finala = valoare_initiala + valoare_initiala * valori_tva['general'] / 100
#     if produs in alimentare:
#         val_finala += val_finala * valori_tva['alimentare'] / 100
#     elif produs in electrocasnice:
#         val_finala += val_finala * valori_tva['electrocasnice'] / 100
#     elif produs in imobiliare:
#         val_finala += val_finala * valori_tva['imobiliare'] / 100
#     else:
#         val_finala += val_finala * valori_tva['rest'] / 100
#
#     return round(val_finala, 2)
#
# produs = input("Ce produs cumparati?")
# val_intiala = int(input("Ce valoare are?"))
# val_finala = calcul_tva(produs, val_intiala)
# print("Valoarea finala este: {}".format(val_finala))

# def get_produs_type(produs):
#     dictionar = {
#         'lapte' : "A",
#         'malai' : "A",
#         'apartament' : "I",
#         'lcd' : 'E'
#     }
#     return dictionar[produs]
#
# def calc_val_produs(produs, val_initiala):
#     val_fara_tva = val_initiala * 1.10
#     tip_produs = get_produs_type(produs)
#     if tip_produs == 'A':
#         val_totala = val_fara_tva * 1.05
#     elif tip_produs == "E":
#         val_totala = val_fara_tva * 1.10
#     elif tip_produs == "I":
#         val_totala = val_fara_tva * 1.19
#     else:
#         val_totala = val_fara_tva * 1.08
#     return round(val_totala, 2)
#
# produs = 'lcd'
# val_init = 100
# print(calc_val_produs(produs, val_init))
#
# fisier = open(file = "fisier1.txt", mode = "wt", encoding = "utf-8")
# fisier.write("Text pentru prima linie")
# fisier.write(" continuare pentru prima linie\n")
# fisier.write("Continut pe linia a doua!")
# fisier.close()
#
# fis_nou = open(file = "fisier1.txt", mode = "rt", encoding = "utf-8")
# #argumentele de mode/encoding aveau aceste valori in mod implicit
# print(fis_nou.read(10))
# print(fis_nou.read())
# fis_nou.seek(12)
# print(fis_nou.readline())
# fis_nou.seek(0)
# print(fis_nou.readlines())
# fis_nou.close()
#
#
# fis_doi = open(file = "fisier1.txt", mode = "a+", encoding = "utf-8")
# fis_doi.writelines(["\nText adaugat in cadrul unui fisier existent\n",
#                     "Pe mai multe linii cu writelines\n"])
#
# fis_doi.seek(0)
# print(fis_doi.read())
# fis_doi.close()

# with open(file = "exemplu_cm.txt", mode = "wt", encoding='utf-8') as file:
#     file.write("Prima mea linie cu context manager\n")
#     file.write("Continuarea pe a doua linie")


# file.write("Alta linie") I/O Operation on closed file


#
# with open(file = "file_3.txt", mode = "wt", encoding = "utf-8") as file:
#     file.write("Linia 1\n")
#     file.write("Linia 2\n")
#     file.write("Linia 3\n")
#
# with open(file = "file_3.txt", mode = "a+") as file:
#     file.writelines(["Append linia 4\n", "Append linia 5\n"])
#
# with open(file = "file_3.txt") as file:
#     for element in file:
#         print(element, end = "")























