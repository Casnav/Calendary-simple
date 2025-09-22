#lista de tareas
tareas = ["comer", "tirar la basura", "bañarse"]

# funciones del programa
def agregar_tarea(lista):
    #Entrada para la tarea
    tarea = input("Introduzca la descripción de la tarea: ")
    
    #Anadir la tarea al final de la lista
    lista.append(tarea)
    
    #Informe de tarea añadida
    print("\nLa tarea se añadió a la lista de tareas pendientes.\n")
    
    #Imprime la tarea añadida
    print(f"La tarea añadida es: {tarea}.")
    
    #Informa del numero de tarea
    print(f"La tarea se almacenó en la posición {len(lista)}\n")

def eliminar_tarea(lista):
    
    # Si la lista contiene algo
    if lista:
        #Llamamos a la funcion ver_tareas()
        ver_tareas(lista)
        
        #Entrada para que el usuario introduzca una tarea
        tarea = int(input("Introduzca el número de la tarea a eliminar: "))
        
        # Opcion invalida si la tarea no está en el rango de la lista
        if tarea <= 0 or tarea > len(lista):
            print("Opción inválida.")
        
        # si la opción es válida se elimina la tarea
        else:
            del lista[tarea - 1]
            print("Se eliminó la tarea.")
        
    # Si la lista está vacía se avisa de eso
    else:
        print("No hay tareas.")
 

def tarea_completada(lista):
    #Llamamos a la funcion ver_tareas()
    ver_tareas(lista)
    
    # entrada para que el usuario introduzca una tarea
    completada = int(input("Introduzca el numero de la tarea a marcar como completada: "))
    
    
        # Condicional para marcar tareas como completadas
    if completada > 0 and completada <= len(lista):
        # Condicional para evaluar si la tarea ya estaba completada
        # Si la tarea ya está completa...
        if "(Completada)" in lista[completada - 1]:
            print("La tarea ya estaba marcada como completada.")
        # En cambio, si no lo está...
        else:
            lista[completada - 1] = "(Completada)" + lista[completada - 1]
            print("Se marcó la tarea como completada.")
    # Avisar si la opción elegida es invalida
    else:
        print("opcion invalida.")



def ver_tareas(lista):
    # Condicional que evalúe si algo está en la lista
    
    # si hay algo en la lista se presenta
    if lista:
        for indice, tarea in enumerate(lista):
            print(f"{indice + 1}. {tarea}")
    # si la lista está vacía avisar de ello
    else:
        print("No hay tareas pendientes.")
    # Mensaje de fin de listado
    print("--- FIN DEL LISTADO DE TAREAS ----")
