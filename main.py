from biblioteca import Biblioteca

def mostrar_menu():
    print("\n=== Sistema de Biblioteca ===")
    print("1. Agregar Libro")
    print("2. Agregar Revista")
    print("3. Agregar Periódico")
    print("4. Prestar ítem")
    print("5. Devolver ítem")
    print("6. Buscar por autor")
    print("7. Listar todos los ítems")
    print("0. Salir")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            biblioteca.agregar_libro(titulo, autor, editorial)
        elif opcion == "2":
            titulo = input("Título: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            numero = input("Número: ")
            biblioteca.agregar_revista(titulo, autor, editorial, numero)
        elif opcion == "3":
            titulo = input("Título: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            fecha = input("Fecha de publicación: ")
            biblioteca.agregar_periodico(titulo, autor, editorial, fecha)
        elif opcion == "4":
            titulo = input("Título: ")
            print(biblioteca.prestar_item(titulo))
        elif opcion == "5":
            titulo = input("Título: ")
            print(biblioteca.devolver_item(titulo))
        elif opcion == "6":
            autor = input("Autor: ")
            resultados = biblioteca.buscar_por_autor(autor)
            if resultados:
                print("Ítems encontrados:")
                for item in resultados:
                    print(item.mostrar_detalles())
            else:
                print("No se encontraron ítems para ese autor.")
        elif opcion == "7":
            biblioteca.listar_items()
        elif opcion == "0":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")