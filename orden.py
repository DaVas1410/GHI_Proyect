import pandas as pd

archivos_csv = ["Balao 01-01-24 08-01-24.csv", "Basbasquillo 01-01-24 08-01-24.csv", "Beaterio01-01-24 08-01-24.csv", "Guajalo 01-01-24 08-01-24.csv", "Monteverde 01-01-24 08-01-24.csv", "Riobamba 01-01-24 08-01-24.csv"]

for archivo in archivos_csv:
    try:
        df = pd.read_csv(archivo)

        # Verificar si las columnas necesarias están presentes
        columnas_necesarias = ['ghi', 'time', 'period']
        if all(columna in df.columns for columna in columnas_necesarias):
            # Convertir la columna 'time' al formato datetime
            df['time'] = pd.to_datetime(df['time'], errors='coerce')
            # Extraer solo la fecha de 'time' y usarla como nombre de columna
            df['date'] = df['time'].dt.strftime('%d/%m/%Y')
            df['time'] = df['time'].dt.strftime('%H:%M')
            # Pivotar los datos para obtener el formato deseado
            pivot_df = df.pivot_table(index='time', columns='date', values='ghi', aggfunc='sum')
            # Escribir el DataFrame pivotado en un archivo CSV separado
            nombre_archivo = archivo.split(".csv")[0]
            pivot_df.to_csv(f"{nombre_archivo}_pivotado.csv")
        else:
            print(f"Las columnas necesarias no están presentes en el archivo {archivo}. No se procesará este archivo.")
    except Exception as e:
        print(f"Error al procesar el archivo {archivo}: {e}")
