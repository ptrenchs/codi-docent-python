from fun_CMD import contenido_directorio
from fun_CMD import fucniones_strings
import json
import os


# carpeta = contenido_directorio.Directorio('/home/pol/Escritorio/carpeta_prova').all_archivos()
# archivos_ipynb = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'ipynb').elejir()
# archivos_ipynb = contenido_directorio.Filtros_carpetas(rutas = archivos_ipynb,carpetas = '.ipynb_checkpoints').eliminar()
# archivos_ipynb = contenido_directorio.ordenar_directorio(rutas=archivos_ipynb).ordenar()

# archivos_py = convertir.converitr.ipynb_to_py(archivos_ipynb)

carpeta = contenido_directorio.Directorio('/home/ptrenchs/Escritorio/carpeta_probas').all_archivos()
archivos_ipynb = contenido_directorio.Filtros_formato(rutas = carpeta,formatos = 'ipynb').elejir()
archivos_ipynb = contenido_directorio.Filtros_carpetas(rutas = archivos_ipynb,carpetas = '.ipynb_checkpoints').eliminar()


## bucle for
for i in range(len(archivos_ipynb)):
    ruta_archivo = archivos_ipynb[i]
    with open(ruta_archivo,'r',encoding='utf-8') as archivo:
        datos_clase = json.load(archivo)
    with open(ruta_archivo,'r',encoding='utf-8') as archivo:
        datos_alumno = json.load(archivo)

    nom_format = os.path.basename(ruta_archivo)
    ruta_carp_principal = '/'.join(ruta_archivo.split('/')[:-2])

    for pos,cell in enumerate(datos_alumno['cells']):
        if cell['cell_type'] == 'code':
            datos_clase['cells'][pos]['execution_count'] = None
            datos_clase['cells'][pos]['outputs'] = []

            datos_alumno['cells'][pos]['execution_count'] = None
            datos_alumno['cells'][pos]['outputs'] = []
            v_d_0 = ''
            v_i_0 = ''
            for i in range(len(cell['source'])):
                line = cell['source'][i]
                line_class= fucniones_strings.linea(line=line)
                com,v_i, v_d, l_e, v_v = [line_class.comentario(), line_class.var_indepe(), line_class.var_dep(), line_class.line_especial(),line_class.ver_valor()]
                if 'import' in v_v:
                    datos_alumno['cells'][pos]['source'][i] =  v_v
                else:
                    if v_i_0 != '' and v_v != '':
                        datos_alumno['cells'][pos]['source'][i] =  v_v
                    else:
                        if v_d != '':
                            left = ((v_d.split('=')[0]).replace('\t','')).replace(' ','')
                            datos_alumno['cells'][pos]['source'][i] = com + v_i + f'# Encuentra variable que debe ser {left}\n'
                        else:
                            datos_alumno['cells'][pos]['source'][i] = com + v_i
                v_i_0 = v_i
            # print(cell['source'])
    # print(datos_alumno['cells'])
    os.makedirs(ruta_carp_principal + '/2-carpeta_clase', exist_ok=True)
    ruta_clase = ruta_carp_principal + '/2-carpeta_clase' + '/' + nom_format

    with open(ruta_clase, 'w', encoding='utf-8') as nuevo_archivo:
        json.dump(datos_clase, nuevo_archivo, ensure_ascii=False, indent=4)


    os.makedirs(ruta_carp_principal + '/3-carpeta_alumnos', exist_ok=True)
    ruta_alumnos = ruta_carp_principal + '/3-carpeta_alumnos' + '/' + nom_format

    with open(ruta_alumnos, 'w', encoding='utf-8') as nuevo_archivo:
        json.dump(datos_alumno, nuevo_archivo, ensure_ascii=False, indent=4)


