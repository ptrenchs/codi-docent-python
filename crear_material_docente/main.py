from fun_CMD import contenido_directorio
from fun_CMD import manipulacion_archivos



# carpeta = contenido_directorio.Directorio('/home/pol/Escritorio/carpeta_prova').all_archivos()
# archivos_ipynb = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'ipynb').elejir()
# archivos_ipynb = contenido_directorio.Filtros_carpetas(rutas = archivos_ipynb,carpetas = '.ipynb_checkpoints').eliminar()
# archivos_ipynb = contenido_directorio.ordenar_directorio(rutas=archivos_ipynb).ordenar()

# archivos_py = convertir.converitr.ipynb_to_py(archivos_ipynb)

carpeta = contenido_directorio.Directorio('/home/ptrenchs/Escritorio/carpeta_probas').all_archivos()
archivos_ipynb = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'ipynb').elejir()
archivos_ipynb = contenido_directorio.Filtros_carpetas(rutas = archivos_ipynb,carpetas = '.ipynb_checkpoints,2-carpeta_clase,3-carpeta_enunciados,4-corregir').eliminar()
print(archivos_ipynb)
manipulacion_archivos.Enunciados(rutas=archivos_ipynb,corregir=True).crear_enunciados_clase_alumno()


