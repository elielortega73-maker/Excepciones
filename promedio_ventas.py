# Cálculo del promedio de ventas con manejo de excepciones

try:
    venta_1 = float(input("Ingrese el monto de la primera venta (C$): "))
    venta_2 = float(input("Ingrese el monto de la segunda venta (C$): "))
    venta_3 = float(input("Ingrese el monto de la tercera venta (C$): "))

    # Se define la cantidad de registros procesados
    cantidad_ventas = 3

    total_ventas = venta_1 + venta_2 + venta_3
    promedio_ventas = total_ventas / cantidad_ventas

    print("\n✅ Cálculo realizado correctamente:")
    print(f"Total recaudado: C${total_ventas:.2f}")
    print(f"Promedio por venta: C${promedio_ventas:.2f}")

except ValueError:
    print("\n❌ Error de entrada: Asegúrese de ingresar únicamente valores numéricos en cada venta.")

except ZeroDivisionError:
    print("\n❌ Error matemático: Se intentó dividir entre cero. La cantidad de ventas debe ser mayor a 0.")