class Producto:
    def __init__(self, codigo, nombre, precio, cantidad, categoria):
            self.codigo = codigo
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad
            self.categoria = categoria

    def mostrar_info(self):
            return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Cantidad {self.cantidad}, Categoria {self.categoria}"
        

class SistemaProducto:
    def __init__(self):
            self.producto = []


    def registrar_producto(self):
            codigo = input("Codigo del producto: ")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            categoria = input("Categoria del producto: ")

            for prod in self.producto:
                if prod.codigo == codigo:
                    print("El codigo ya existe en un producto")
                    return

            while True:
                cantidad = int(input("Cantidad del producto:"))
                if cantidad >= 0:
                    break
                print("Cantidad invalida")

            nuevo_producto = Producto(codigo, nombre, precio, cantidad, categoria)
            self.producto.append(nuevo_producto)
            print("Producto registrado")

    def mostrar_productos(self):

            if len(self.producto) == 0:
             print("No hay productos registrados")
             return

            print("Lista de productos:")

            for prod in self.producto:
                print(prod.mostrar_info())
            
    def buscar_producto(self):

            codigo_buscar = input("Ingrese el codigo del producto a buscar: ")

            for prod in self.producto:
                if prod.codigo == codigo_buscar:
                    print("Producto encontrado: ")
                    print(prod.mostrar_info())
                    return
                
            print("Producto no encontrado")

    def actualizar_producto(self):
            codigo_actualizar = input("Ingrese el codigo del producto a actualizar: ")

            for prod in self.producto:
                if prod.codigo == codigo_actualizar:
                    prod.cantidad = int(input("Nueva cantidad:"))
                    prod.precio = float(input("Nuevo precio:"))
                    prod.categoria = input("Nueva categoria")

                print("Producto actualizado")
                return
            print("Producto no encontrado")

            for prod in self.producto:
                if prod.codigo == codigo_actualizar:
                    while True:
                        nuevo_precio = float(input("Ingrese el nuevo precio:"))
                        if nuevo_precio == 0:
                            prod.precio = nuevo_precio
                            print("Precio actualizado")
                            return
                        print("Precio invalido, intente nuevamente")
                    print("Producto no encontrado")

            for prod in self.producto:
                if prod.codigo == codigo_actualizar:
                    while True:
                        nueva_categoria = input("Ingrese la nueva categoria: ")
                        if nueva_categoria == "":
                            prod.categoria = nueva_categoria
                            print("Categoria actualizada")
                            return
                        print("La categoria no puede estar vacia")
                    print("Producto no encontrado")


    def eliminar_producto(self):
            codigo_eliminar = input("Ingrese el codigo del producto a eliminar: ")

            for prod in self.producto:
                if prod.codigo == codigo_eliminar:
                    self.producto.remove(prod)
                    print("Producto eliminado")
                    return
                print("Producto no encontrado")



    def calcular_total_inv(self):
            total = 0

            for prod in self.producto:
                total += prod.precio * prod.cantidad

            print("Total acumulado", total)



    def productos_agotados(self):
            agotados = False

            for prod in self.producto:
                if prod.cantidad == 0:
                    print(f"{prod.nombre} esta agotado")
                    agotados = True
            if agotados == False:
                print("No hay productos agotados")
            
    def guardar_archivo(self):
            with open("productos.txt", "w") as archivo:
                for prod in self.producto:
                    archivo.write(prod.mostrar_info()+"\n")
            print("Archivo guardado correctamente")
                
    def menu(self):
        while True:
            print("""\n
                === Menu: ====
                1. Registrar productos
                2. Mostrar productos
                3. Buscar productos
                4. Actualizar productos
                5. Eliminar productos
                6. Calcular total
                7. Productos agotados
                8. Guardar archivo
                9. Salir
                ===============
                """)

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                    self.registrar_producto()

            elif opcion == "2":
                    self.mostrar_productos()

            elif opcion == "3":
                    self.buscar_producto()

            elif opcion == "4":
                    self.actualizar_producto()

            elif opcion == "5":
                    self.eliminar_producto()

            elif opcion == "6":
                    self.calcular_total_inv()

            elif opcion == "7":
                    self.productos_agotados()

            elif opcion == "8":
                    self.guardar_archivo()

            elif opcion == "9":
                    print("Saliendo...")
                    break

            else:
                    print("Opcion invalida, intente nuevamente")

sistema = SistemaProducto()
sistema.menu()
