# CSV to Excel Converter

Este script de Python convierte archivos CSV a formato Excel (XLSX), ajustando automáticamente el ancho de las columnas y la altura de las filas para mejorar la legibilidad. Además, incluye una barra de progreso interactiva para visualizar el avance del proceso en tiempo real.

## Características

- 🔁 Convierte múltiples archivos CSV a Excel en lote
- 📏 Ajusta automáticamente el ancho de las columnas basado en el contenido
- 📐 Ajusta la altura de las filas para una mejor visualización
- 🧾 Preserva los nombres de los archivos originales, cambiando solo la extensión
- ⏱ Muestra una barra de progreso dinámica con tiempo transcurrido, archivo actual y filas procesadas

## Requisitos

- Python 3.x
- pandas
- openpyxl
- tqdm

## Instalación

1. Clona este repositorio o descarga el script.
2. Instala las dependencias:

```
pip install pandas openpyxl
```

## Uso

1. Coloca tus archivos CSV en la carpeta `archivos/`.
2. Ejecuta el script:

```
python programa.py
```

3. Los archivos Excel convertidos se guardarán en la carpeta `archivos_excel/`.

## Estructura del Proyecto

```
└── 📁archivos  # Carpeta para los archivos CSV de entrada
└── 📁archivos_excel # Carpeta donde se guardan los archivos Excel convertidos
└── programa.py # Script principal
```

## Personalización

Puedes modificar las variables `csv_directory` y `output_folder` en el script para cambiar las ubicaciones de entrada y salida de los archivos.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de enviar un pull request.


