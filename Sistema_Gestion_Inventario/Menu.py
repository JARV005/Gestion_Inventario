from G_Inventario import *

def Menu():
    while True:
        print("\n     MENU    ")
        print(" 1. Añadir producto")
        print(" 2. Consultar producto")
        print(" 3. Actualizar precio producto")
        print(" 4. Eliminar producto")
        print(" 5. Calcular valor total de inventario")
        print(" 6. Ver inventario")
        print(" 7. Salir")
        Accion = int(input("Ingrese una opción del 1 al 7: "))
        
        if Accion == 1:
            AñadirP()
        elif Accion==2:
            ConsultarP()
        elif Accion==3:
            ActualizarP()
        elif Accion==4:
            EliminarP()
        elif Accion==5:
            CalcularValorTotal()
        elif Accion==6:
            imprimirI()    
        elif Accion == 7:
            print("Adiós")
            break
        



Menu()
