# Validación del precio de un producto mediante control de excepciones

try:
    entrada_precio = input("Ingrese el precio del producto (C$): ")
    precio_producto = float(entrada_precio)

    if precio_producto >= 0:
        print(f"✅ Precio registrado correctamente: C${precio_producto:.2f}")
    else:
        print("⚠️ Advertencia: El número ingresado es negativo, pero el formato es válido.")

except ValueError:
    print("❌ Entrada no válida: Por favor ingrese únicamente valores numéricos (ejemplo: 45 o 12.50).")