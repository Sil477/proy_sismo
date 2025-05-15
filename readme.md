   # Proyecto de Detección Automática de Sismos

   Este proyecto realiza un proceso de ETL (Extracción, Transformación, Carga) sobre registros sismológicos de la estación TRVA para detectar automáticamente la ocurrencia de sismos y determinar su momento exacto.

   ## 1. Objetivos

   * Desarrollar un método para la detección automática de sismos basado en el aumento de la amplitud de la señal. [cite: 11]
   * Filtrar los registros en una banda de 1 a 5 Hz para reducir el ruido sísmico y mejorar la detección. [cite: 12]
   * Determinar el momento (día, hora, minuto, segundo) de cada sismo detectado. [cite: 13]

   ## 2. Estructura del Proyecto
<pre>
MiProyectoSismico/
├── README.md           (Este archivo)
├── data/               (Datos)
│   ├── raw/            (Datos originales)
│   │   └── TRVA.201502.E.N.Z.txt
│   ├── processed/      (Datos procesados)
│   │   └── sismos_detectados.csv
│   └── catalog/        (Catálogo de referencia)
│       └── catalogo_sismos.csv
├── src/                (Código fuente)
│   ├── main.py         (Script principal)
│   ├── processing.py   (Funciones de procesamiento)
│   └── utils.py        (Funciones auxiliares)
├── reports/            (Informes)
│   └── informe.pdf
├── notebooks/          (Exploración)
│   └── exploracion.ipynb
└── requirements.txt    (Dependencias)
</pre>

## 3. Datos

* **Fuente:** Registros sismológicos de la estación TRVA. [cite: 8]
* **Archivo:** `TRVA.201502.E.N.Z.txt` (en `data/raw/`). [cite: 8]
* **Formato:** ASCII, tres columnas (E, N, Z). [cite: 8, 9]
* **Datación:** Implícita, primer registro: 00:00:00 del 01 de febrero de 2015 (TUC), frecuencia: 40 Hz. [cite: 9]
* **Catálogo de referencia:** Disponible en el enlace del documento "uno.pdf" (en `data/catalog/`). [cite: 14]

## 4. Dependencias

Python 3.x

Bibliotecas de Python (instalar con `pip install -r requirements.txt`):

* pandas
* numpy
* scipy
* matplotlib (opcional, para visualización en Python)

## 5. Uso

1.  Clonar el repositorio: `git clone <URL_del_repositorio>`
2.  Navegar al directorio: `cd MiProyectoSismico`
3.  Instalar dependencias: `pip install -r requirements.txt`
4.  Ejecutar el script: `python src/main.py`
5.  Los resultados se guardan en `data/processed/sismos_detectados.csv`

## 6. Configuración

Las variables de configuración están en `src/main.py`:

* `archivo_entrada`: Ruta al archivo de datos.
* `frecuencia_muestreo`: Frecuencia de muestreo (Hz).
* `frecuencia_corte`: Frecuencias de corte del filtro (Hz).
* `umbral_amplitud`: Umbral para detectar sismos.

## 7. Salida

Archivo CSV (`data/processed/sismos_detectados.csv`) con las columnas:

* `Tiempo`: Momento del registro.
* `Amplitud`: Amplitud de la señal.
* `Sismo`: 1 si se detectó sismo, 0 si no.

## 8. Autor

Grupo sismo

## 9. Agradecimientos

A la organización co-formadora por proporcionar los datos y la guía técnica. [cite: 5, 6, 7]

## proy_sismo