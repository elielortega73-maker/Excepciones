# Menú de opciones con control de excepciones y bloque else

print("--- Menú Principal ---")
print("1. Consultar inventario")
print("2. Registrar nueva venta")
print("3. Salir del sistema")

try:
    entrada_usuario = input("\nSeleccione una opción numérica (1-3): ")
    opcion_menu = int(entrada_usuario)

except ValueError:
    print("\n❌ Error de entrada: Debe ingresar obligatoriamente un número entero, no letras ni decimales.")

else:
    # Este bloque se ejecuta ÚNICAMENTE cuando la conversión del try fue exitosa
    print(f"\n✅ Opción procesada correctamente: {opcion_menu}")

    if opcion_menu == 1:
        print("Abriendo el módulo de consulta de inventario...")
    elif opcion_menu == 2:
        print("Abriendo el módulo de registro de ventas...")
    elif opcion_menu == 3:
        print("Saliendo del sistema. ¡Hasta luego!")
    else:
        print("⚠️ Advertencia: El número ingresado está fuera de rango. Seleccione una opción entre 1 y 3.")