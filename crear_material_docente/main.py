from fun_CMD import contenido_directorio
from fun_CMD import convertir


# carpeta = contenido_directorio.Directorio('/home/pol/Escritorio/carpeta_prova').all_archivos()
# archivos_ipynb = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'ipynb').elejir()
# archivos_ipynb = contenido_directorio.Filtros_carpetas(rutas = archivos_ipynb,carpetas = '.ipynb_checkpoints').eliminar()
# archivos_ipynb = contenido_directorio.ordenar_directorio(rutas=archivos_ipynb).ordenar()

# archivos_py = convertir.converitr.ipynb_to_py(archivos_ipynb)

carpeta = contenido_directorio.Directorio('/home/pol/Escritorio/carpeta_prova').all_archivos()
archivos_py = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'py').elejir()
archivos_py = contenido_directorio.Filtros_carpetas(rutas = archivos_py,carpetas = '.ipynb_checkpoints').eliminar()
archivos_py = contenido_directorio.ordenar_directorio(rutas=archivos_py).ordenar()

archivos_ipynb = convertir.converitr.py_to_ipynb(archivos_py)

print(archivos_ipynb)

