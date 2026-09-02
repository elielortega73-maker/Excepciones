# Manejo de archivos controlando FileNotFoundError y utilizando finally

nombre_archivo = "reportes.txt"

try:
    print(f"Intentando abrir el archivo '{nombre_archivo}'...")
    archivo_reporte = open(nombre_archivo, "r", encoding="utf-8")
    contenido_reporte = archivo_reporte.read()
    print("✅ Archivo abierto y leído correctamente.")
    archivo_reporte.close()

except FileNotFoundError:
    print(f"❌ Error (FileNotFoundError): No se encontró el archivo '{nombre_archivo}' en la ruta especificada.")

finally:
    # Este bloque se ejecuta siempre, sin importar si hubo error o éxito
    print("🔄 Operación de acceso al archivo finalizada.")