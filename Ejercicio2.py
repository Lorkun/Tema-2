import random

def agregar_mision(misiones):
    tipe= input("Tipo de mision: ")
    planeta= input("Planeta destino: ")
    general= input("Quien lo solicita: ")

    nueva_mision = [tipe, planeta, general]
    misiones.append(nueva_mision)

def asignar_recursos(misiones):
    scout_troopers = 0
    speeder_bike=0
    vehicles = 0
    stormtroopers=0

    for mision in misiones:
        if mision[2] == "Palpatine" or mision[2] == "Darth Vader":
            scout_troopers += 15 
            speeder_bike += 2
            vehicles += 7
            stormtroopers +=50
        
        else:
            if mision[0] == "exploracion":
                scout_troopers += 15 
                speeder_bike += 2
            elif mision[0] == "contencion":
                vehicles += random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"])
                stormtroopers +=7   

            elif mision[0] == "ataque":
                stormtroopers += 50
                vehicles += random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"])

        print("Recursos Asignados: ")
        print("Scout Troopers", scout_troopers)
        print("Speeder Bike,", speeder_bike)
        print("Stormtroopers", stormtroopers)
        print("Vehiculos", vehicles)

def mostrar_misiones(misiones):
    print("Misiones: ")
    for mision in misiones:
        print("Tipo: ", mision[0])
        print("Planeta destino: ", mision[1])
        print("General que la solicita: ", mision[2])
        print("")

def mostrar_menu():
    print("1. Agregar misión")
    print("2. Asignar recursos")
    print("3. Mostrar misiones")
    print("4. Salir")

def ejecutar_programa():
    misiones = []
    entradas = 0
    while entradas !=4:
        mostrar_menu()
        entradas = int(input("Ingrese una entrada: "))
        if entradas == 1:
            agregar_mision(misiones)
        elif entradas == 2:
            asignar_recursos(misiones)
        elif entradas == 3:
            mostrar_misiones(misiones)
        else:
            print("Finalizando Programa...")

ejecutar_programa()
