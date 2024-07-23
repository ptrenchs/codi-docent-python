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
        # Caracteres que se entienden como comentarios
        coment = '#'
        for i in range(len(cell['source'])):
            line = cell['source'][i]
            for j,caracter in enumerate(line):
                for cm in coment.split(','):
                    if cm == caracter:
                        break
                if cm == caracter:
                    break
            if cm == caracter:
                sep_enter = ' ,\t,\n'
                principio = line[:j]
                coment = line[j:]
                for sep in sep_enter.split(','):
                    principio = principio.replace(sep,'')
                if principio != '':
                    left_left = principio.split('=')[0]
                    rigth_rigth = principio.split('=')[1]
                    eval()
            else:

        print(cell['source'])

