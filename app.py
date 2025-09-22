import funciones

#Bucle principal
while True:
    #menu de opciones
    print("\n******--- Gestor de Tareas ---******\n")
    print("1. Añadir tarea")
    print("2. Eliminar tarea")
    print("3. Marcar como completada")
    print("4. Ver tareas")
    print("5. Salir")
    
    print("\n")
    
# Entrada para el usuario
    opcion = input("Introduzca una opción: ")

    print("\n")
    
    # Menú de opciones
    match opcion:
        case "1":
            funciones.agregar_tarea(funciones.tareas)
        
        case "2":
            funciones.eliminar_tarea(funciones.tareas)
        
        case "3": 
            funciones.tarea_completada(funciones.tareas)
        
        case "4": 
            funciones.ver_tareas(funciones.tareas)
                
        case "5": 
            print("Gracias por usar el software de ConsoleTec.")
            break
        
        case _:
            print("Opcion invalida.")