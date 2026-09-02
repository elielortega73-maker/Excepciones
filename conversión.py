# Conversión de moneda controlando errores de entrada de datos

try:
    monto_ingresado = float(input("Ingrese el monto que desea convertir: "))
    tasa_cambio = float(input("Ingrese la tasa de cambio actual: "))

    # Validación lógica adicional para evitar conversiones sin sentido
    if tasa_cambio <= 0:
        print("\n⚠️ Error lógico: La tasa de cambio debe ser un número mayor a cero.")
    else:
        monto_equivalente = monto_ingresado * tasa_cambio
        print("\n✅ Conversión exitosa:")
        print(f"El monto equivalente es: {monto_equivalente:.2f}")

except ValueError:
    print("\n❌ Error de conversión de tipo (ValueError):")
    print("Asegúrese de ingresar solo números. No incluya letras, comas ni símbolos como '$' o 'C$'.")