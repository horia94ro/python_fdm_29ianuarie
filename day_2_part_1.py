# ora = input("Que hora es: ")
# if ora.isnumeric():
#     print("Valoarea continuta este numerica!")
#     ora = int(ora)
#     if ora >= 0 and ora < 24:
#         if ora >= 6 and ora < 11:
#             print("Buna dimineata!")
#         elif ora >= 11 and ora <= 17:
#             print("Buna ziua!")
#         elif ora >= 18:
#             print("Buna seara")
#         else:
#             print("Noapte buna!")
#     else:
#         print("Valoare invalida!")
# else:
#     print("Valoarea introdusa nu este numerica!")

# i = 10
# while i > 0:
#     print(i, end = " ")
#     i -= 1
#
# print("\n")
#
# i = 10
# while i > 0:
#     if i % 2 == 0:
#         print(":)", end = " ")
#         i -= 1
#
#         continue #imi sare la urmatoarea iteratie a buclei while
#     print(i, end=" ")
#     i -= 1

#
# i = 10
# while i > 0:
#     print(i, end = " ")
#     i -= 1
#     if i == 5:
#         break #intrerupe executia buclei cu totul
#
# print("\nSFARSITUL PROGRAMULUI")

# i = 10
# while i > 0:
#     i -= 1
#     print(i, end=" ")
#     if i == 5:
#         break
#     if i % 3 == 0:
#         print(":)", end = " ")
#         continue
#     print(":(")
#

# for i in range(0, 10, 3):
#     print(i, end = " ")
# print("\n")
# for i in range(5, 15):
#     print(i, end = " ")
#
# lista_cuvinte = ['telecom', 'academy', '\u2665', 'metro', 'systems']
# # for cuv in lista_cuvinte:
# #     print(cuv, len(cuv), end = " ")
#
# for cuv in range(len(lista_cuvinte)):
#     print(lista_cuvinte[cuv], end = " ")
#

# while input("Introduceti textul: ")!= "telacad":
#     print("Gresit, reintroduceti")
#
# print("Sfarsitul programului!")
##Ex 1 PPT Curs 2
# while True:
#     cuv = input("Academia: ")
#
#     if cuv == "telacad":
#         break
#     print("WRONG!")
#
# print("Sfarsitul programului")

##Ex2 PPT Curs 2

# while True:
#     nr = input("Valoarea: ")
#
#     if nr.isnumeric() and int(nr) > 2:
#         nr = int(nr)
#         sum = 0
#         for i in range(0, nr + 1):
#             sum += i
#         print("Suma este: ", sum)
#         break
#     else:
#         print("WRONG")


# while True:
#     nr = input("Valoare: ")
#     if not nr.isnumeric():
#         print("Valoarea nu este numerica")
#         continue
#     nr = int(nr)
#     if nr <= 2:
#         print("Prea mic")
#         continue
#     # print("Suma este: ", sum(range(0, nr + 1)))
#     suma = 0
#     for i in range(0, nr + 1):
#         suma += i
#     print("Suma este: {}".format(suma))
#     break
# i1 = "Bogdan"
# print("Utilizatorul {0} are CNP {1} si inaltime: {2}".format(i1, 103, 178))
# print("Utilizatorul %s are CNP %i si inaltime: %i " % ("Horia", 103, 178))



##Ex3 PPT Curs 2
#
# cuv = input("Academia: ")
# while cuv != "telacad":
#     print("WRONG")
#     cuv = input("Academia: ")
#     if cuv == "telacad":
#         el = " "
#         lista = [cuv, 'peste 10 ani vechime', 'predare', 'cursuri online']
#         print(el.join(lista))
#         break

##Ex4 PPT Curs 2

# x = 4 + 3j
#
# if isinstance(x, int):
#     x += 3
#     print(x)
# elif isinstance(x, float):
#     x /= 2
#     print(x)
# elif isinstance(x, complex):
#     print("Partea reala: {}\nPartea imaginara: {}\nModul: {}".format(x.real, x.imag, abs(x)))

##Ex5 PPT Curs 2
# while True:
#     nr = input("Te rog da-mi un numar superb: \u2665 ")
#     if not nr.isnumeric():
#         print("Mai baga o fisa...")
#         continue
#     nr = int(nr)
#     for i in range(0, nr + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print(i, "FOO BAR")
#         elif i % 5 == 0:
#             print(i, "BAR")
#         elif i % 3 == 0:
#             print(i, "FOO")
#         else:
#             print(i)
#     break


##Ex2 Ex optionale PPT Curs2
nr = 4
prim = True
for i in range(2, nr//2 + 1):
    if nr % i == 0:
        prim = False
        break

if prim:
    print("Numarul {} este prim".format(nr))
else:
    print("Numarul {} NU este prim".format(nr))

