# Consulta de inventario por posición controlando ValueError e IndexError

lista_productos = ["Arroz", "Frijoles", "Aceite", "Azúcar", "Café", "Sal", "Harina"]

print("--- Catálogo de Inventario ---")
for indice, producto in enumerate(lista_productos):
    print(f"[{indice}] {producto}")

try:
    entrada_posicion = input("\nIngrese la posición numérica del producto que desea buscar: ")
    posicion = int(entrada_posicion)
    
    # Intenta acceder a la posición (puede lanzar IndexError si no existe)
    producto_seleccionado = lista_productos[posicion]
    print(f"\n✅ Producto consultado: '{producto_seleccionado}' (ubicado en el índice {posicion}).")

except ValueError:
    # Captura cuando el usuario ingresa letras o símbolos en lugar de un número entero
    print("\n❌ Error de entrada (ValueError): Debe ingresar obligatoriamente un número entero válido, no letras ni decimales.")

except IndexError:
    # Captura cuando el número está fuera del rango de la lista (ejemplo: -1 o 10)
    print("\n❌ Error de rango (IndexError): La posición ingresada no existe en el inventario. Elija un índice dentro de la lista.")