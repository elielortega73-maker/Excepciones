# Diccionario de empleados y consulta con control de errores y get()

empleados = {
    "EMP001": {"nombre": "Ana Pérez", "puesto": "Desarrolladora C#", "salario": 15000.0},
    "EMP002": {"nombre": "Carlos Gómez", "puesto": "Soporte Técnico", "salario": 11000.0},
    "EMP003": {"nombre": "María Ruiz", "puesto": "Administradora de Redes", "salario": 14000.0}
}

print("--- 1. Consulta controlando KeyError ---")
clave_buscada = input("Ingrese el código del empleado (ej. EMP001): ").strip().upper()

try:
    # Intenta acceder directamente. Lanza KeyError si la clave no existe.
    info_empleado = empleados[clave_buscada]
    print(f"\n✅ Empleado encontrado:")
    print(f"Nombre: {info_empleado['nombre']}")
    print(f"Puesto: {info_empleado['puesto']}")
    print(f"Salario: C${info_empleado['salario']:.2f}")

except KeyError:
    print(f"\n❌ Error (KeyError): La clave '{clave_buscada}' no está registrada en el sistema.")


print("\n--- 2. Alternativa eficiente usando .get() ---")
clave_alternativa = input("Ingrese la clave a buscar usando .get(): ").strip().upper()

# .get() devuelve None si la clave no existe, evitando la excepción por completo.
resultado = empleados.get(clave_alternativa)

if resultado is not None:
    print(f"\n✅ Empleado encontrado con .get():")
    print(f"Nombre: {resultado['nombre']} | Puesto: {resultado['puesto']}")
else:
    print(f"\n⚠️ Aviso: La clave '{clave_alternativa}' no existe. El método .get() previno el fallo.")