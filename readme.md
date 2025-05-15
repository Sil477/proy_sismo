# Proyecto de Detección Automática de Sismos
   
   Este proyecto realiza un proceso de ETL (Extracción, Transformación, Carga) sobre registros sismológicos de la estación TRVA para detectar automáticamente la ocurrencia de sismos y determinar su momento exacto.
   
   ## 1. Objetivos
   
   * Desarrollar un método para la detección automática de sismos basado en el aumento de la amplitud de la señal. [cite: 24]
   * Filtrar los registros en una banda de 1 a 5 Hz para reducir el ruido sísmico y mejorar la detección. [cite: 25]
   * Determinar el momento (día, hora, minuto, segundo) de cada sismo detectado. [cite: 26]
   
   ## 2. Estructura del Proyecto
   MiProyectoSismico/
├── README.md
├── data/
│   ├── raw/
│   │   └── TRVA.201502.E.N.Z.txt  (Datos originales)
│   ├── processed/
│   │   └── sismos_detectados.csv (Datos procesados)
│   └── catalog/
│       └── catalogo_sismos.csv (Catálogo de referencia)
├── src/
│   ├── main.py          (Script principal)
│   ├── processing.py    (Funciones de procesamiento)
│   └── utils.py         (Funciones auxiliares)
├── reports/
│   └── informe.pdf      (Informe de resultados)
├── notebooks/
│   └── exploracion.ipynb (Exploración inicial)
└── requirements.txt   (Dependencias de Python)
## 3. Datos

* **Fuente:** Registros sismológicos de la estación TRVA. [cite: 21]
* **Archivo:** `TRVA.201502.E.N.Z.txt` (en `data/raw/`). [cite: 21]
* **Formato:** ASCII, tres columnas (E, N, Z). [cite: 21, 22]
* **Datación:** Implícita, primer registro: 00:00:00 del 01 de febrero de 2015 (TUC), frecuencia: 40 Hz. [cite: 22]
* **Catálogo de referencia:** Disponible en el enlace del documento "uno.pdf" (en `data/catalog/`). [cite: 27]

## 4. Dependencias

* Python 3.x
* Bibliotecas de Python (instalar con `pip install -r requirements.txt`):
     * pandas
     * numpy
     * scipy
     * matplotlib (opcional, para visualización en Python)

## 5.  Uso

1.  Clonar el repositorio: `git clone <URL_del_repositorio>`
2.  Navegar al directorio: `cd MiProyectoSismico`
3.  Instalar dependencias: `pip install -r requirements.txt`
4.  Ejecutar el script: `python src/main.py`
5.  Los resultados se guardan en `data/processed/sismos_detectados.csv`

## 6.  Configuración

Las variables de configuración están en `src/main.py`:

* `archivo_entrada`: Ruta al archivo de datos.
* `frecuencia_muestreo`: Frecuencia de muestreo (Hz).
* `frecuencia_corte`: Frecuencias de corte del filtro (Hz).
* `umbral_amplitud`: Umbral para detectar sismos.

## 7.  Salida

Archivo CSV (`data/processed/sismos_detectados.csv`) con las columnas:

* `Tiempo`: Momento del registro.
* `Amplitud`: Amplitud de la señal.
* `Sismo`: 1 si se detectó sismo, 0 si no.

## 8.  Autor

Grupo sismo

## 9.  Agradecimientos

A la organización co-formadora por proporcionar los datos y la guía técnica. [cite: 21, 23]