from fun_CMD import contenido_directorio
from fun_CMD import manipulacion_archivos



carpeta = contenido_directorio.Directorio('/home/ptrenchs/Escritorio/carpeta_probas').all_archivos()
archivos_ipynb = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'ipynb').elejir()
archivos_ipynb = contenido_directorio.Filtros_carpetas(rutas = archivos_ipynb,carpetas = '.ipynb_checkpoints,2-ejercicio_resuelto,3-enunciados,4-resuelto_Alumnos,5-corretgit').eliminar()
crear_material = manipulacion_archivos.Material(rutas=archivos_ipynb,corregir=True)

crear_material.Enunciados()
crear_material.ejercicio_resuelto()
