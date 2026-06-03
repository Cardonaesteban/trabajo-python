class Usuarios:
    def __init__(self, documento, nombre, correo, rol, estado):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo
        self.rol = rol
        self.estado = estado

    def mostrar_info(self):
        return f"Documento: {self.documento}, Nombre: {self.nombre}, Correo: {self.correo}, Rol: {self.rol}, Estado: {self.estado}"
    

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    
    def registrar_usuario(self):
        documento = input("Ingresar documento: ")
        nombre = input("Ingresar nombre: ")
        correo = input("Ingresar correo: ")
        rol = input("Ingresar rol: ")
        estado = input("Ingresar estado: ")

        for usuario in self.usuarios:
            if usuario.documento == documento:
                print("El documento ya está registrado.")
                return
            
        for usuario in self.usuarios:
            if usuario.correo == correo:
                print("El correo ya está registrado.")
                return

        nuevo_usuario = Usuarios(documento, nombre, correo, rol, estado)
        self.usuarios.append(nuevo_usuario)
        print("Usuario registrado con éxito.")

    def mostrar_usuarios(self):
        if len(self.usuarios) == 0:
            print("No hay usuarios registrados")
            return
        
        print("Lista de usuarios: ")
        for usuario in self.usuarios:
            print(usuario.mostrar_info())

    def buscar_usuario(self):
        documento_buscar = input("Ingrese el documento del usuario a buscar: ")

        for usuario in self.usuarios:
            if usuario.documento == documento_buscar:
                print("Usuario encontrado: ")
                print(usuario.mostrar_info())
                return
        print("Usuario no encontrado.")

    def actualizar_usuario(self):
        documento_actualizar = input("Ingrese el documento del usuario a actualizar: ")

        for usuario in self.usuarios:
            if usuario.documento == documento_actualizar:
                print("Usuario encontrado: ")
                print(usuario.mostrar_info())

                usuario.nombre = input("Ingrese el nuevo nombre: ")
                usuario.correo = input("Ingrese el nuevo correo: ")
                usuario.rol = input("Ingrese el nuevo rol: ")
                usuario.estado = input("Ingrese el nuevo estado: ")
                print("Usuario actualizado con éxito.")
                return
        print("Usuario no encontrado.")

        while True:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            if nuevo_nombre:
                usuario.nombre = nuevo_nombre
                print("Nombre actualizado")
                return
            elif nuevo_nombre == "":
                print("Nombre no puede estar vacio")

        while True:
            nuevo_correo = input("Ingrese el nuevo correo: ")
            if nuevo_correo:
                usuario.correo = nuevo_correo
                print("Correo actualizado")
                return
            elif nuevo_correo == "":
                print("Correo no puede estar vacio")

        while True:
            nuevo_rol = input("Ingrese el nuevo rol: ")
            if nuevo_rol:
                usuario.rol = nuevo_rol
                print("Rol actualizado")
                return
            elif nuevo_rol == "":
                print("Rol no puede estar vacio")

        while True:
            nuevo_estado = input("Ingrese el nuevo estado: ")
            if nuevo_estado:
                usuario.estado = nuevo_estado
                print("Estado actualizado")
                return
            elif nuevo_estado == "":
                print("Estado no puede estar vacio")

    def eliminar_usuario(self):
        documento_eliminar = input ("Ingrese el documento del usuario a eliminar: ")

        for usuario in self.usuarios:
            if usuario.documento == documento_eliminar:
                self.usuarios.remove(usuario)
                print("Usuario eliminado con éxito.")
                return
        print("Usuario no encontrado.")

    def mostrar_activos(self):
        if len(self.usuarios) == 0:
            print("No hay usuarios registrados")
            return
        print("Lista de usuarios activos: ")
        
        for usuario in self.usuarios:
            if usuario.estado.lower() == "activo":
                print(usuario.mostrar_info())
    
    
        
    def contar_roles(self):
        roles = {}

        for usuario in self.usuarios:
            if usuario.rol in roles:
                roles[usuario.rol] += 1
        else:
            roles[usuario.rol] = 1

        for rol in roles:
            print(rol, ":", roles[rol])
    

    def guardar_archivo(self):
        with open("usuarios.txt", "w") as archivo:
            for usuario in self.usuarios:
                archivo.write(usuario.mostrar_info()+"\n")
        print("Archivo guardado correctamente.")

    def menu(self):
        while True:
            print("""\n
                === Menu: ====
                1. Registrar Usuarios
                2. Mostrar Usuarios
                3. Buscar Usuarios  
                4. Actualizar Usuarios
                5. Eliminar Usuarios
                6. Mostrar usuarios activos
                7. Contar roles
                8. Guardar archivo
                9. Salir
                ===============
                """)

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                    self.registrar_usuario()

            elif opcion == "2":
                    self.mostrar_usuarios()

            elif opcion == "3":
                    self.buscar_usuario ()

            elif opcion == "4":
                    self.actualizar_usuario()

            elif opcion == "5":
                    self.eliminar_usuario()

            elif opcion == "6":
                    self.mostrar_activos()

            elif opcion == "7":
                    self.contar_roles()

            elif opcion == "8":
                    self.guardar_archivo()

            elif opcion == "9":
                    print("Saliendo...")
                    break

            else:
                    print("Opcion invalida, intente nuevamente")

sistema = SistemaUsuarios()
sistema.menu()
