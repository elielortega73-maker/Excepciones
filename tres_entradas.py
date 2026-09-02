# Registro de empleado controlando excepciones específicas

nombre_empleado = input("Ingrese el nombre: ")

try:
    # Primera conversión que puede fallar
    entrada_edad = input("Ingrese la edad: ")
    edad_empleado = int(entrada_edad)
    
    try:
        # Segunda conversión que puede fallar
        entrada_salario = input("Ingrese el salario (C$): ")
        salario_empleado = float(entrada_salario)
        
        # Si el programa llega a esta línea, ambas conversiones fueron exitosas
        print("\n✅ Datos registrados correctamente:")
        print(f"Nombre: {nombre_empleado} | Edad: {edad_empleado} | Salario: C${salario_empleado:.2f}")
        
    except ValueError:
        print("\n❌ Error: El SALARIO debe corregirse. Asegúrese de ingresar solo números o decimales (ejemplo: 4500.50).")
        
except ValueError:
    print("\n❌ Error: La EDAD debe corregirse. Asegúrese de ingresar un número entero (ejemplo: 25).")