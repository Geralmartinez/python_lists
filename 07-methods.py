# Método append
list = []
list.append("Xiaomi")
list.append("Motorola")
print(list)

# Método insert. Inserta un elemento en un índice específico de la lista.
list.insert(1,"Huawei")
print(list)

# Método extend: Agrega elementos de otro iterable (como otra lista) al final de la lista actual.

list_2 = ["Samsung", "Apple", "Toshiba"]
list.extend(list_2)

print(list)