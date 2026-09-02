# Validación de calificación numérica y verificación de rango (0 a 100)

try:
    entrada_calificacion = input("Ingrese la calificación obtenida (0 a 100): ")
    calificacion = float(entrada_calificacion)

    if 0 <= calificacion <= 100:
        print(f"✅ Calificación válida: {calificacion:.2f}. Se encuentra dentro del rango de 0 a 100.")
    else:
        print(f"⚠️ La calificación ({calificacion:.2f}) es un número válido, pero está FUERA del rango permitido (0 a 100).")

except ValueError:
    print("❌ Entrada no válida: Por favor ingrese únicamente valores numéricos (ejemplo: 85 o 92.5).")