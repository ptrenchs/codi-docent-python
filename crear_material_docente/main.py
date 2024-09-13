from fun_CMD import contenido_directorio
from fun_CMD import manipulacion_archivos
import tkinter as tk
from tkinter import filedialog

# Crear una ventana raíz de tkinter (no visible)
root = tk.Tk()
root.withdraw()  # Ocultar la ventana raíz

# Abrir el diálogo para seleccionar carpeta
folder_path = filedialog.askdirectory()

# Mostrar la ruta seleccionada (puedes usarla según lo necesites)
if folder_path:
    print("Carpeta seleccionada:", folder_path)
else:
    print("No se seleccionó ninguna carpeta")



carpeta = contenido_directorio.Directorio(folder_path).all_archivos()
archivos_ipynb = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'ipynb').elejir()
archivos_ipynb = contenido_directorio.Filtros_carpetas(rutas = archivos_ipynb,carpetas = '.ipynb_checkpoints,2-ejercicio_resuelto,3-enunciados,4-resuelto_Alumnos,5-corretgit').eliminar()
crear_material = manipulacion_archivos.Material(rutas=archivos_ipynb,corregir=True,sub_indice='pu')

crear_material.Enunciados()
crear_material.ejercicio_resuelto()
