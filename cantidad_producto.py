# Validación de cantidad de productos a comprar

try:
    entrada_cantidad = input("Ingrese la cantidad de unidades que desea comprar: ")
    cantidad_productos = int(entrada_cantidad)
    
    if cantidad_productos > 0:
        print(f"✅ Cantidad registrada correctamente: {cantidad_productos} unidad(es).")
    elif cantidad_productos == 0:
        print("⚠️ Ha ingresado 0 unidades. No se procesará ninguna compra.")
    else:
        print("⚠️ Advertencia: No puede comprar cantidades negativas.")
        
except ValueError:
    print("❌ Entrada no válida: Por favor ingrese únicamente números enteros (ejemplo: 3). No se permiten letras ni números con decimales.")