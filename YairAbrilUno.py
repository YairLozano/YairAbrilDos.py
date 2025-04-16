print ("Gestion de tareas pendientes")

def mostrar_menu():
    print("gestor de tarea penientes")
    print("escribir tarea")
    print("ver todas las tareas")
    print("Marcar una tarea como completada")
    print("salir")

tareas = []

while True:
    mostrar_menu()
    opcion = input("selecciona una opcion")

if opcion == "1":
    tarea = input("ingresa la descripcion de la tarea:")
    tareas.append(tarea)
    print("tarea escrita") 

elif opcion == "2":
    if not tareas:
        print("no hay tareas pendientes")
    else:
        print("tareas pendientes")
        for i,tarea in enumerate(tareas,1):
            print("tarea")

elif opcion == "3":
    if not tareas:
        print("no hay tareas para completar")
    else:
        for i,tarea in enumerate(tareas,1):
            print("tarea")
        num = input("ingresa el numero de la tarea completada")    
               
        if 1 <= num <= len(tareas):
            print ("tare completada y eliminada")
