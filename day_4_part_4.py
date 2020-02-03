def modifica_val(x):
    print("Locatia lui x in metoda: ", id(x))
    x += 1
    print("Locatia lui x in metoda dupa modificare: ", id(x))

def modifica_lista(lista):
    print("Locatia listei in metoda: ", id(lista))

    lista.append(27)
    print("Locatia listei in metoda dupa modificare: ", id(lista))


val = [1, 2, 3]
print("Locatia lui val in progr: ", id(val))
modifica_lista(val)
print(val)

print("Locatia lui val dupa apelul metodei: ", id(val))

# a = 10
# print("Locatia lui a in progr: ", id(a))
#
# modifica_val(a)
# print(a)
# print("Locatia lui a dupa apel: ", id(a))