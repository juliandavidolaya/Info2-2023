##### Base de datos implementada como lo pide el ejercicio

import pymongo
from datetime import datetime

# Establecer conexión con la base de datos de MongoDB
client = pymongo.MongoClient("mongodb+srv://julianolaya:<passwooorr-ojo-noolvidar>@cluster0.2ujzn4v.mongodb.net/test")
database = client["clinica_veterinaria"]
collection = database["mascotas_hospitalizadas"]

# Función para ingresar una nueva mascota hospitalizada
def ingresar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    num_historia = input("Ingrese el número de historia clínica de la mascota: ")
    tipo = input("Ingrese el tipo de mascota (canino o felino): ")
    peso = float(input("Ingrese el peso de la mascota: "))
    fecha_ingreso = datetime.now()
    medicamento_nombre = input("Ingrese el nombre del medicamento que se está administrando: ")
    medicamento_dosis = float(input("Ingrese la dosis del medicamento que se está administrando: "))
    nueva_mascota = {"nombre": nombre, "num_historia": num_historia, "tipo": tipo, "peso": peso, "fecha_ingreso": fecha_ingreso, "medicamento": {"nombre": medicamento_nombre, "dosis": medicamento_dosis}}
    collection.insert_one(nueva_mascota)
    print("Mascota ingresada exitosamente.")

# Función para modificar la información de una mascota hospitalizada
def modificar_mascota():
    num_historia = input("Ingrese el número de historia clínica de la mascota que desea modificar: ")
    mascota = collection.find_one({"num_historia": num_historia})
    if mascota:
        opcion = input(f"¿Qué información desea modificar de la mascota {mascota['nombre']}? (nombre, tipo, peso, medicamento) ")
        if opcion == "nombre":
            nuevo_nombre = input("Ingrese el nuevo nombre de la mascota: ")
            collection.update_one({"num_historia": num_historia}, {"$set": {"nombre": nuevo_nombre}})
            print("Nombre modificado exitosamente.")
        elif opcion == "tipo":
            nuevo_tipo = input("Ingrese el nuevo tipo de la mascota (canino o felino): ")
            collection.update_one({"num_historia": num_historia}, {"$set": {"tipo": nuevo_tipo}})
            print("Tipo modificado exitosamente.")
        elif opcion == "peso":
            nuevo_peso = float(input("Ingrese el nuevo peso de la mascota: "))
            collection.update_one({"num_historia": num_historia}, {"$set": {"peso": nuevo_peso}})
            print("Peso modificado exitosamente.")
        elif opcion == "medicamento":
            nuevo_medicamento_nombre = input("Ingrese el nuevo nombre del medicamento que se está administrando: ")
            nuevo_medicamento_dosis = float(input("Ingrese la nueva dosis del medicamento que se está administrando: "))
            collection.update_one({"num_historia": num_historia}, {"$set": {"medicamento": {"nombre": nuevo_medicamento_nombre, "dosis": nuevo_medicamento_dosis}}})
            print("Medicamento modificado exitosamente.")
        else:
            print("Opción invalida.")

# Función para ver la información de una mascota hospitalizada por su número de historia clínica
def ver_mascota():
    num_historia = input("Ingrese el número de historia clínica de la mascota que desea ver: ")
    mascota = collection.find_one({"num_historia": num_historia})
    if mascota:
        print("Nombre:", mascota["nombre"])
        print("Número de historia clínica:", mascota["num_historia"])
        print("Tipo:", mascota["tipo"])
        print("Peso:", mascota["peso"])
        print("Fecha de ingreso:", mascota["fecha_ingreso"])
        print("Medicamento:")
        print("\tNombre:", mascota["medicamento"]["nombre"])
        print("\tDosis:", mascota["medicamento"]["dosis"])
    else:
        print("No se encontró una mascota con ese número de historia clínica.")

# Función para ver la lista de todas las mascotas hospitalizadas
def ver_lista_mascotas():
    mascotas = collection.find()
    for mascota in mascotas:
        print("Nombre:", mascota["nombre"])
        print("Número de historia clínica:", mascota["num_historia"])
        print("Tipo:", mascota["tipo"])
        print("Peso:", mascota["peso"])
        print("Fecha de ingreso:", mascota["fecha_ingreso"])
        print("Medicamento:")
        print("\tNombre:", mascota["medicamento"]["nombre"])
        print("\tDosis:", mascota["medicamento"]["dosis"])
        print("")

# Función para ver la lista de medicamentos que se están administrando a todas las mascotas hospitalizadas
def ver_lista_medicamentos():
    medicamentos = set()
    mascotas = collection.find()
    for mascota in mascotas:
        medicamentos.add(mascota["medicamento"]["nombre"])
        print("Medicamentos que se están administrando:")
    for medicamento in medicamentos:
        print("\t", medicamento)

# Función para eliminar una mascota hospitalizada por su número de historia clínica
def eliminar_mascota():
    num_historia = input("Ingrese el número de historia clínica de la mascota que desea eliminar: ")
    result = collection.delete_one({"num_historia": num_historia})
    if result.deleted_count > 0:
        print("Mascota eliminada exitosamente.")
    else:
        print("No se encontró una mascota con ese número de historia clínica.")

# Loop principal del programa
while True:
    print("Bienvenido al sistema de la clínica veterinaria.")
    print("Por favor seleccione una opción:")
    print("1. Ingresar una nueva mascota hospitalizada.")
    print("2. Modificar la información de una mascota hospitalizada.")
    print("3. Ver la información de una mascota hospitalizada por su número de historia clínica.")
    print("4. Ver la lista de todas las mascotas hospitalizadas.")
    print("5. Ver la lista de medicamentos que se están administrando a todas las mascotas hospitalizadas.")
    print("6. Eliminar una mascota hospitalizada por su número de historia clínica.")
    print("7. Salir del sistema.")
    opcion = input("Ingrese su opción: ")
    if opcion == "1":
        ingresar_mascota()
    elif opcion == "2":
        modificar_mascota()
    elif opcion == "3":
        ver_mascota()
    elif opcion == "4":
        ver_lista_mascotas()
    elif opcion == "5":
        ver_lista_medicamentos()
    elif opcion == "6":
        eliminar_mascota()
    elif opcion == "7":
        print("Gracias por utilizar el sistema de la clínica veterinaria. Hasta luego.")
        break
    else:
        print("Opción inválida. Por favor ingrese una opción válida.") 
    




