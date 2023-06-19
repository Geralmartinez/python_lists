dogs = []
menu_option = ""
while menu_option != "3" :
    print ("1. agregar cachorros")
    print("2. ver cachorritos")
    print("3. salir")
    menu_option = input()

    if menu_option == "1":
        dog = []
        name = input ("ingrese el name de su cachorrito")
        age = input ("ingrese la edad de su cachorrito")
        breed = input(" ingrese la la raza de su cachorrito")
        dog.append(name)
        dog.append(age)
        dog.append(breed)
        dogs.append(dog)
        print("cachorrito agregado con exito")

    elif menu_option == "2":
        number = 0
        while number  < len(dogs):
            print("------------")
            print(f"el nombre: {dogs[number][0]}")
            print(f"la edad: {dogs[number][1]}")
            print(f"el raza: {dogs[number][2]}")
            number += 1
    elif menu_option == "3" :
         print("gracias por participar")
