import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.utils import get_column_letter

def adjust_column_width(worksheet):
    for column in worksheet.columns:
        max_length = 0
        column_letter = get_column_letter(column[0].column)
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        worksheet.column_dimensions[column_letter].width = adjusted_width

def convert_csv_to_excel(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            csv_file = os.path.join(folder_path, filename)
            excel_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.xlsx')

            df = pd.read_csv(csv_file)

            # Guarda el DataFrame en Excel
            df.to_excel(excel_file, index=False)

            # Carga el archivo Excel para ajustar el formato
            wb = load_workbook(excel_file)
            ws = wb.active

            # Ajusta el ancho de las columnas
            adjust_column_width(ws)

            # Ajusta la altura de las filas
            for row in ws.iter_rows():
                ws.row_dimensions[row[0].row].auto_size = True

            # Guarda los cambios
            wb.save(excel_file)
            print(f'Convertido y ajustado {csv_file} a {excel_file}')

# Directorio que contiene los archivos CSV
csv_directory = 'archivos/'

# Carpeta donde se guardarán los archivos Excel convertidos
output_folder = 'archivos_excel/'

# Llama a la función para convertir los archivos
convert_csv_to_excel(csv_directory, output_folder)