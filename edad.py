# Validación de edad para registro usando un bucle para evitar avanzar con errores

print("--- Sistema de Registro ---")

while True:
    try:
        entrada_edad = input("Ingrese su edad: ")
        edad_registro = int(entrada_edad)
        
        # Validación lógica (una edad no debe ser negativa ni exageradamente alta)
        if 0 <= edad_registro <= 120:
            print(f"✅ Edad registrada correctamente: {edad_registro} años.")
            break  # Rompe el ciclo while, permitiendo que el programa continúe
        else:
            print("⚠️ Edad fuera de rango lógico. Ingrese una edad real (0 - 120).")
            
    except ValueError:
        print("❌ Entrada no válida: Por favor ingrese únicamente números enteros (ejemplo: 25).")

# El programa SOLO llegará a esta línea si el usuario ingresó una edad válida y se ejecutó el "break"
print("\nContinuando con el siguiente paso del registro...")