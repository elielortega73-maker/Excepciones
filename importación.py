# Simulación de importación controlada de un módulo inexistente

try:
    # Intentamos importar un módulo que deliberadamente no existe en el proyecto
    import modulo_inventario_avanzado
    
except ModuleNotFoundError as error_modulo:
    print(f"❌ Error detectado: {error_modulo}")
    print("\n🔍 Guía de revisión para la persona desarrolladora:")
    print("• Verifique que el nombre del módulo o librería esté escrito correctamente (sin errores tipográficos).")
    print("• Compruebe si la dependencia externa está instalada en el entorno virtual actual (ejecute 'pip list' en la terminal).")
    print("• Si se trata de un paquete externo nuevo, instálelo usando el comando correspondiente (ejemplo: 'pip install nombre_paquete').")
    print("• Asegúrese de que los archivos locales o carpetas personalizados formen parte del directorio del proyecto y tengan el archivo '__init__.py' si es necesario.")