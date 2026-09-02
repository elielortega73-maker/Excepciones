# Demostración y corrección de tipos incompatibles (TypeError)

nombre_producto = "Memoria RAM 16GB"
cantidad_inventario = 5

print("--- 1. Provocando el error ---")
try:
    # Intento incorrecto de unir (concatenar) texto con un número entero
    mensaje_incorrecto = "Tenemos en inventario: " + cantidad_inventario + " unidades de " + nombre_producto
    print(mensaje_incorrecto)

except TypeError as error_generado:
    print("❌ ¡Se ha producido un TypeError!")
    print(f"Mensaje del sistema: {error_generado}")

print("\n--- 2. Aplicando la corrección ---")
# Corrección: Se utiliza str() para convertir el número a texto antes de concatenarlo
mensaje_corregido = "Tenemos en inventario: " + str(cantidad_inventario) + " unidades de " + nombre_producto
print(f"✅ Éxito: {mensaje_corregido}")

# Alternativa moderna en Python (usando f-strings que hacen la conversión automáticamente):
# print(f"✅ Alternativa: Tenemos en inventario {cantidad_inventario} unidades de {nombre_producto}")