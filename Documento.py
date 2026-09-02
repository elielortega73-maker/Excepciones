# Cálculo de descuento proporcional controlando ValueError y ZeroDivisionError

try:
    monto_descuento = float(input("Ingrese el monto del descuento (C$): "))
    precio_base = float(input("Ingrese el precio base del producto (C$): "))

    # Cálculo del porcentaje. Si precio_base es 0.0, Python lanzará ZeroDivisionError automáticamente
    porcentaje_descuento = (monto_descuento / precio_base) * 100

    print(f"\n✅ Cálculo exitoso:")
    print(f"El descuento de C${monto_descuento:.2f} representa un {porcentaje_descuento:.2f}% del precio base (C${precio_base:.2f}).")

except ValueError:
    print("\n❌ Error de entrada: Los valores ingresados deben ser numéricos. Evite usar letras o caracteres especiales.")

except ZeroDivisionError:
    print("\n❌ Error matemático: El precio base no puede ser igual a cero (0). No es posible calcular una proporción dividiendo entre cero.")