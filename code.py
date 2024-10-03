class Pila:
    def __init__(self):
        self.items = []

    def crear(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def esta_vacia(self):
        return self.items == []

    def imprimir(self):
        print("Pila:", self.items)


class Cola:
    def __init__(self):
        self.items = []

    def crear(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def esta_vacia(self):
        return self.items == []

    def imprimir(self):
        print("Cola:", self.items)


def modificar_estructura(estructura, x):
    """
    Elimina todos los elementos de la estructura hasta encontrar el valor X, sin eliminar X.

    Args:
      estructura: Una instancia de la clase Pila o Cola.
      x: El valor que se busca en la estructura.
    """
    elementos_eliminados = []
    while not estructura.esta_vacia() and estructura.items[-1] != x:
        elementos_eliminados.append(estructura.desapilar())
    if not estructura.esta_vacia():
        estructura.imprimir()
    else:
        print("El valor X no se encontró en la estructura.")


def menu():
    pila = Pila()
    cola = Cola()

    while True:
        print("\n--- Menú ---")
        print("1. Operaciones con Pila")
        print("2. Operaciones con Cola")
        print("3. Modificar Estructura")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            while True:
                print("\n--- Operaciones con Pila ---")
                print("1. Crear Pila")
                print("2. Apilar")
                print("3. Desapilar")
                print("4. Imprimir Pila")
                print("5. Volver al Menú Principal")

                sub_opcion = input("Ingrese una opción: ")

                if sub_opcion == "1":
                    pila.crear()
                    print("Pila creada.")
                elif sub_opcion == "2":
                    valor = int(input("Ingrese el valor a apilar: "))
                    pila.apilar(valor)
                elif sub_opcion == "3":
                    valor = pila.desapilar()
                    if valor is not None:
                        print("Valor desapilado:", valor)
                    else:
                        print("La pila está vacía.")
                elif sub_opcion == "4":
                    pila.imprimir()
                elif sub_opcion == "5":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "2":
            while True:
                print("\n--- Operaciones con Cola ---")
                print("1. Crear Cola")
                print("2. Encolar")
                print("3. Desencolar")
                print("4. Imprimir Cola")
                print("5. Volver al Menú Principal")

                sub_opcion = input("Ingrese una opción: ")

                if sub_opcion == "1":
                    cola.crear()
                    print("Cola creada.")
                elif sub_opcion == "2":
                    valor = int(input("Ingrese el valor a encolar: "))
                    cola.encolar(valor)
                elif sub_opcion == "3":
                    valor = cola.desencolar()
                    if valor is not None:
                        print("Valor desencolado:", valor)
                    else:
                        print("La cola está vacía.")
                elif sub_opcion == "4":
                    cola.imprimir()
                elif sub_opcion == "5":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "3":
            while True:
                print("\n--- Modificar Estructura ---")
                print("1. Modificar Pila")
                print("2. Modificar Cola")
                print("3. Volver al Menú Principal")

                sub_opcion = input("Ingrese una opción: ")

                if sub_opcion == "1":
                    valor = int(input("Ingrese el valor X para modificar la pila: "))
                    modificar_estructura(pila, valor)
                elif sub_opcion == "2":
                    valor = int(input("Ingrese el valor X para modificar la cola: "))
                    modificar_estructura(cola, valor)
                elif sub_opcion == "3":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
