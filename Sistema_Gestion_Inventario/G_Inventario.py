#añadir 
#consultar
# actualizar 
# eliminar 

# Diccionario que almacena los productos del inventario.
Inventario = {}

#Funcion para añadir productos
def AñadirP():
    print("     AÑADIR PRODUCTO     ")
    while True:#Ingresa nombre de producto
        while True:
            Nombre = input("Ingrese el nombre del producto: ").strip().lower()
            if not Nombre:
                print("El nombre no puede estar vacío.")
            elif not Nombre.replace(" ", "").isalpha():
                print("El nombre solo puede contener letras. No se permiten números ni caracteres especiales.")
            elif Nombre in Inventario:
                print(f"El producto '{Nombre}' ya existe en el inventario. No se puede agregar nuevamente.")
            else:
                break
#Validacion
        while True:#Ingresa y validar precio de producto 
            try:
                Precio = float(input("Ingrese el precio del producto: "))
                if Precio <= 0:
                    print("El precio debe ser un número positivo.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Ingrese un número válido para el precio.")

        while True:#Ingresa y validar cantidad de producto
            try:
                Cantidad = int(input("Ingrese la cantidad disponible: "))
                if Cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Ingrese un número entero para la cantidad.")

        Inventario[Nombre] = {'Precio': Precio, 'Cantidad': Cantidad}
        print(f"Producto '{Nombre}' añadido correctamente.")
        print(Inventario)
        #Pregunta si desea añadir otro producto
        while True:
            continuar = input("¿Desea ingresar otro producto? si/no ").strip().lower()
            if continuar in ["si", "s", "sí"]:
                break
            elif continuar in ["no", "n"]:
                return  
            else:
                print("Por favor, responda solo con 'sí' o 'no'.")
        
            
    

# Función para imprimir todos los productos del inventario.
def imprimirI():
    print("\n     INVENTARIO DISPONIBLE       ")
    if Inventario:#Ingresar y validar precio de producto 
        for nombre, datos in Inventario.items():
            print(f"Nombre: {nombre}, Precio: {datos['Precio']}, Cantidad: {datos['Cantidad']}")
    else:
        print("El inventario está vacío.")

# Función para consultar un producto específico en el inventario.
def ConsultarP():
    print("\n     CONSULTAR PRODUCTO      ")
    while True:#Ingresa y validar precio de producto 
        NombreP = input("Ingrese el nombre del producto: ").strip().lower()
        if not NombreP:
            print("El nombre no puede estar vacío.")
            continue
        if not NombreP.replace("","").isalpha():
            print("El nombre solo puede contener letras. No ingrese números ni carateres especiales")
            continue
        if NombreP in Inventario:
            ProductoCons = Inventario[NombreP]
            print("\nProducto encontrado:")
            print(f"Nombre: {NombreP}")
            print(f"Precio: {ProductoCons['Precio']}")
            print(f"Cantidad: {ProductoCons['Cantidad']}")
        else:
            print("No se encontró un producto con ese nombre.")
        # Pregunta si se desea consultar otro producto.
        while True:
            continuar = input("¿Desea consultar otro producto? si/no ").strip().lower()
            if continuar in ["si", "s", "sí"]:
                break
            elif continuar in ["no", "n"]:
                return  
            else:
                print("Por favor, responda solo con 'sí' o 'no'.")

# Función para actualizar el precio de un producto existente.
def ActualizarP():
    print("\n   ACTUALIZAR PRODUCTO   ")
    while True:#Ingresa y validar precio de producto 
        NombreP = input("Ingrese el nombre del producto a modificar: ").strip().lower()
        if not NombreP:
            print("El nombre no puede estar vacío.")
            continue
        if not NombreP.replace("","").isalpha():
            print("El nombre solo puede contener letras. No ingrese números ni carateres especiales")
            continue
        if NombreP in Inventario:
            ProductoMod = Inventario[NombreP]
            print("\nInformación actual del producto:")
            print(f"Nombre: {NombreP}")
            print(f"Precio: {ProductoMod['Precio']}")
            print(f"Cantidad: {ProductoMod['Cantidad']}")

            # Solicita el nuevo precio y validar su valor.
            try:
                nuevo_valor = float(input("Ingrese el nuevo precio del producto: "))
                if nuevo_valor <= 0:
                    print("El precio debe ser un número positivo.")
                    continue
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")
                continue

            # Actualiza el precio del producto.
            ProductoMod['Precio'] = nuevo_valor
            print(f"Precio de {NombreP} actualizado con éxito!")
            print(f"Nombre: {NombreP}")
            print(f"Precio: {ProductoMod['Precio']}")
            print(f"Cantidad: {ProductoMod['Cantidad']}")
        else:
            print("No se encontró un producto con ese nombre.")
        # Pregunta si se desea actualizar otro producto.
        
        while True:
            continuar = input("¿Desea actualizar otro producto? si/no ").strip().lower()
            if continuar in ["si", "s", "sí"]:
                break
            elif continuar in ["no", "n"]:
                return  
            else:
                print("Por favor, responda solo con 'sí' o 'no'.")

# Función para eliminar un producto del inventario.
def EliminarP():
    print("\n   ELIMINAR PRODUCTO   ")
    while True:
        NombreP = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
        if not NombreP:
            print("El nombre no puede estar vacío.")
            continue
        if not NombreP.replace("","").isalpha():
            print("El nombre solo puede contener letras. No ingrese números ni carateres especiales")
            continue
        if NombreP in Inventario:
            print("\nProducto encontrado")
            # Elimina el producto del diccionario.
            del Inventario[NombreP]
            print(f"{NombreP} eliminado con éxito.")
        else:
            print("No se encontró un producto con ese nombre.")
        # Pregunta si se desea eliminar otro producto.
        while True:
            continuar = input("¿Desea eliminar otro producto? si/no ").strip().lower()
            if continuar in ["si", "s", "sí"]:
                break
            elif continuar in ["no", "n"]:
                return  
            else:
                print("Por favor, responda solo con 'sí' o 'no'.")

# Función para calcular el valor total del inventario.
def CalcularValorTotal():
    print("\n     VALOR TOTAL DEL INVENTARIO     ")
    if not Inventario:
        print("El inventario está vacío.")
        return
    # Define una función lambda para multiplicar precio y cantidad.
    calcular_producto = lambda precio, cantidad: precio * cantidad
    valor_total = 0
    # Recorre los productos y suma su valor total.
    for datos in Inventario.values():
        valor_total += calcular_producto(datos['Precio'], datos['Cantidad'])
    print(f"El valor total del inventario es: {valor_total} pesos")
