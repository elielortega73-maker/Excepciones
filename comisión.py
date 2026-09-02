# Cálculo de comisión por ventas con manejo de excepciones

try:
    # Se solicitan los datos. Se espera que el usuario ingrese números válidos.
    entrada_ventas = input("Ingrese el monto total de ventas (C$): ")
    monto_ventas = float(entrada_ventas)
    
    entrada_porcentaje = input("Ingrese el porcentaje de comisión (%): ")
    porcentaje_comision = float(entrada_porcentaje)
    
    # Cálculo de la comisión
    comision_obtenida = monto_ventas * (porcentaje_comision / 100)
    
    print("\n✅ Cálculo exitoso:")
    print(f"Total en ventas: C${monto_ventas:.2f}")
    print(f"Comisión a recibir ({porcentaje_comision}%): C${comision_obtenida:.2f}")

except ValueError:
    # EXCEPCIÓN ESPERADA (ValueError):
    # Esta excepción se captura específicamente cuando la función float() 
    # intenta convertir una cadena de texto (str) a un número decimal, 
    # pero el usuario ingresa letras, espacios en blanco o símbolos 
    # incompatibles (como 'C$' o '%').
    
    print("\n❌ Error de entrada (ValueError):")
    print("Asegúrese de ingresar solo números. Evite incluir símbolos como 'C$' o '%'.")