from fun_CMD import contenido_directorio
import json


# carpeta = contenido_directorio.Directorio('/home/pol/Escritorio/carpeta_prova').all_archivos()
# archivos_ipynb = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'ipynb').elejir()
# archivos_ipynb = contenido_directorio.Filtros_carpetas(rutas = archivos_ipynb,carpetas = '.ipynb_checkpoints').eliminar()
# archivos_ipynb = contenido_directorio.ordenar_directorio(rutas=archivos_ipynb).ordenar()

# archivos_py = convertir.converitr.ipynb_to_py(archivos_ipynb)

carpeta = contenido_directorio.Directorio('/home/ptrenchs/Escritorio/carpeta_probas').all_archivos()
archivos_ipynb = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'ipynb').elejir()
archivos_ipynb = contenido_directorio.Filtros_carpetas(rutas = archivos_ipynb,carpetas = '.ipynb_checkpoints').eliminar()

with open(archivos_ipynb[0],'r',encoding='utf-8') as archivo:
    datos = json.load(archivo)


for cell in datos['cells']:
    if cell['cell_type'] == 'code':
        for i in range(len(cell['source'])):
            line = cell['source'][i]
            
        print(cell['source'])

