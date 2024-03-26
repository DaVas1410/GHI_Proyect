import pandas as pd

archivos_csv = ["Balao 01-01-24 08-01-24.csv", "Basbasquillo 01-01-24 08-01-24.csv", "Beaterio01-01-24 08-01-24.csv", "Guajalo 01-01-24 08-01-24.csv", "Monteverde 01-01-24 08-01-24.csv", "Riobamba 01-01-24 08-01-24.csv"]

for archivo in archivos_csv:
    try:
      
        df = pd.read_csv(archivo)

       
        columnas_necesarias = ['dni', 'ghi', 'period_end']
        if all(columna in df.columns for columna in columnas_necesarias):
           
            df['time'] = pd.to_datetime(df['time'], errors='coerce')

         
            df = df[['ghi', 'time', 'period']]

          
            df = df.sort_values(by=['time', 'period'])

           
            nombre_archivo = archivo.split(".csv")[0]
            df.to_csv(f"{nombre_archivo}_ordenado.csv", index=False)
        else:
            print(f"Las columnas necesarias no están presentes en el archivo {archivo}. No se procesará este archivo.")
    except Exception as e:
        print(f"Error al procesar el archivo {archivo}: {e}")