import pandas as pd

# Ruta del archivo Excel (ajústala según tu ubicación real)
archivo_excel = r"C:\Users\LENOVO\Documents\tutoriales_python\Pagados excel.xlsx"

# Cargar el archivo Excel
df = pd.read_excel(archivo_excel)

# Eliminar columnas completamente vacías
df = df.dropna(how="all", axis=1)

# Contar cuántas columnas con datos tiene cada fila
df["num_datos"] = df.notna().sum(axis=1)

# Omitir la primera fila del archivo
df = df.iloc[1:].reset_index(drop=True)  # Resetear el índice para evitar problemas

# Filtrar filas con 5 o más columnas con datos
filtrado = df[df["num_datos"] >= 5].reset_index(drop=True)  # Resetear índice nuevamente

# Omitir la primera fila que cumple la condición
if not filtrado.empty:
    filtrado = filtrado.iloc[1:]  # Ahora sí se elimina correctamente

if filtrado.empty:
    print("No hay filas con más de 5 columnas con datos.")
else:
    # Seleccionar las columnas 1, 2 y 4 (correspondientes a los índices 0, 11, 5)
    seleccion = filtrado.iloc[:, [0, 11, 5]].copy()
    
    # Renombrar las columnas seleccionadas
    seleccion.columns = ["nombre", "identificacion", "pagado"]
    
    # Reordenar las columnas para que queden en el orden deseado
    resultado = seleccion[["nombre", "identificacion", "pagado"]]
    
    # Definir el encabezado deseado como una cadena
    encabezado = "nombre,identificacion,pagado"
    
    # Escribir el CSV agregando la fila del encabezado manualmente
    with open("resultado.csv", "w", encoding="utf-8", newline="") as f:
        f.write(encabezado + "\n")  # Escribir la fila del encabezado
        resultado.to_csv(f, index=False, header=False)  # Escribir los datos

    print("Archivo CSV exportado exitosamente como 'resultado.csv'.")
