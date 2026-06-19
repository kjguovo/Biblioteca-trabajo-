import os

# Pongo una lista vacía llamada biblioteca para guardar los libros
biblioteca = []

# Variables 
titulo = ""
autor = ""
categoria = ""
anio = 0
opcion = ""

#Funcion para registrar un nuevo libro.
#Valida que los campos no esten vacios, que no se repita el titulo
#y que el año sea un numero entero valido usando try/except.
def registrar_libro(titulo, autor, categoria, anio_texto):
    
    # 1. Validar campos vacios
    if titulo == "" or autor == "" or categoria == "":
        print("Error: Todos los campos son obligatorios (Titulo, Autor y Categoría).")
        return # Corta la funcion y regresa al menu

    # 2. Validar que no esté duplicado
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            print("Error: Ese libro ya existe en la biblioteca.")
            return

    # 3. Validar el formato numérico con try/except
    try:
        anio_int = int(anio_texto)
    except ValueError:
        print("Error: Debe ingresar un año válido (número entero).")
        return

    # Si pasa todas las validaciones, se crea el diccionario
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "anio": anio_int
    }      
    biblioteca.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado correctamente.")

def mostrar_libros():
    
    #Funcion para leer y mostrar en pantalla todos los libros registrados.
    
    if len(biblioteca) == 0:
        print("No hay libros registrados.")
    else:
        print("\n------ BIBLIOTECA ------")
        for libro in biblioteca:
            print(f"Título: {libro['titulo']} | Autor: {libro['autor']} | Categoría: {libro['categoria']} | Año: {libro['anio']}")
        print("------------------------\n")

def actualizar_libro(titulo_buscar, nuevo_autor, nueva_categoria, nuevo_anio_texto):
    
    #Funcion para buscar un libro por su titulo y actualizar las opciones
    #verificando que no queden vacíos y que el año sea correcto.
    
    if nuevo_autor == "" or nueva_categoria == "":
        print("Error: El autor y la categoría no pueden quedar vacíos.")
        return

    try:
        anio_int = int(nuevo_anio_texto)
    except ValueError:
        print("Error: Debe ingresar un año válido (número entero).")
        return

    for libro in biblioteca:
        if libro["titulo"].lower() == titulo_buscar.lower():
            libro["autor"] = nuevo_autor
            libro["categoria"] = nueva_categoria
            libro["anio"] = anio_int
            print(f"Libro '{libro['titulo']}' actualizado correctamente.")
            return
    else:        
        print(f"Libro '{titulo_buscar}' no encontrado.")

def eliminar_libro(titulo_buscar):
    
    #Funcion para buscar un libro por su título y removerlo de la lista.
    
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo_buscar.lower():
            biblioteca.remove(libro)
            print(f"Libro '{libro['titulo']}' eliminado correctamente.")
            return
    else:
        print(f"Libro '{titulo_buscar}' no encontrado.")



while True:
    os.system("cls")

    print("----Administrador de Biblioteca----")
    print("1. Agregar Libro")
    print("2. Mostrar Libros")
    print("3. Modificar Libro")
    print("4. Eliminar Libro")
    print("5. Salir")
    
    opcion = input("Opcion: ")

    if opcion == "1":
        os.system("cls")
        print("--- REGISTRAR NUEVO LIBRO ---\n")
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        categoria = input("Categoría: ").strip()
        anio_entrada = input("Año de publicación: ").strip() # Lo pedimos como texto primero
        
        # Le pasamos todo a la funcion para que ella valide y decida si registrar o usar return
        registrar_libro(titulo, autor, categoria, anio_entrada)
        input("\nEnter para continuar...")
        
    elif opcion == "2":
        os.system("cls")
        mostrar_libros()
        input("Enter para continuar...")
        
    elif opcion == "3":
        os.system("cls")
        print("--- MODIFICAR LIBRO EXISTENTE ---\n")
        titulo_buscar = input("Título del libro a modificar: ").strip()
        
        # Pedimos los datos
        nuevo_autor = input("Nuevo Autor: ").strip()
        nueva_categoria = input("Nueva Categoría: ").strip()
        nuevo_anio_entrada = input("Nuevo Año: ").strip()

        # La funcion se encarga de validar con return si algo falla
        actualizar_libro(titulo_buscar, nuevo_autor, nueva_categoria, nuevo_anio_entrada)
        input("\nEnter para continuar...")
        
    elif opcion == "4":
        os.system("cls")
        print("--- ELIMINAR LIBRO ---\n")
        titulo_buscar = input("Título del libro a eliminar: ").strip()
        eliminar_libro(titulo_buscar)
        input("\nEnter para continuar...")
        
    elif opcion == "5":
        os.system("cls")
        print("Salir....")
        input("Enter para continuar...")
        break
        
    else:
        os.system("cls")
        print("Opcion invalida")
        input("Enter para continuar...")
