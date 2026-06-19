Sistema de Gestión de Biblioteca

Este es un programa interactivo desarrollado en Python que permite administrar el inventario de una biblioteca mediante una estructura CRUD (Crear, Leer, Actualizar, Eliminar)

Funcionalidades

Este proyecto incluye las siguientes funcionalidades a través de un menú interactivo:

* Registrar Libro: Permite agregar un nuevo libro al sistema solicitando Título, Autor, Categoría y Año de publicación. Valida que no existan duplicados y que los   campos no estén vacíos.
*Mostrar Libros: Muestra la lista completa de todos los libros registrados en el sistema de manera ordenada.
* Modificar Libro: Modifica los datos de un libro existente buscando por su título. Protege los formatos con manejo de excepciones.
* Eliminar Libro: Elimina un libro del sistema de forma permanente buscando por su título.

Requisitos Técnicos Aplicados

* Uso de listas principales y diccionarios como bases de datos en memoria.
* Uso de funciones independientes y debidamente documentadas.
* Validaciones de texto vacío y manejo de excepciones (try/except) para asegurar que el formato del año sea un número entero (`int`) obligatorio.

Autor

Nikolás Soto
* FPY1101 Fundamentos de Programación.
