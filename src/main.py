import pandas as pd
   import numpy as np
   
   # Datos de ejemplo (reemplazar con la ruta real del archivo)
archivo_entrada = 'data/raw/TRVA.201502.E.N.Z.txt'
   -9990 -9206 -13443
   -10032 -9333 -13335
   -10073 -9454 -13223
   -10124 -9567 -13106
   ...
   """  # Usamos un string multilínea para los datos de ejemplo
   
   from io import StringIO
   
   data_file = StringIO(data) # Convertimos el string en un "archivo"
   
   # Leer los datos desde el string
   df = pd.read_csv(data_file, sep='\s+', header=None)
   
   # Nombrar las columnas
   df.columns = ['E', 'N', 'Z']
   
   # Generar la columna de tiempo
   inicio_tiempo = pd.to_datetime('2015-02-01 00:00:00')
   frecuencia_muestreo = 40  # Hz
   num_registros = len(df)
   
   df['Tiempo'] = pd.date_range(start=inicio_tiempo, periods=num_registros, freq=f'{1/frecuencia_muestreo}S')
   
   # Mostrar las primeras filas del DataFrame
   print(df.head())
   
   # Mostrar información del DataFrame
   print(df.info())