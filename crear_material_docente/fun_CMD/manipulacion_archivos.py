from fun_CMD import fucniones_strings
import json
import os

class Material:
    def __init__(self, rutas, corregir = False):
        self.rutas = rutas
        self.corregir = corregir

    def Enunciados(self):
        for ruta_archivo in self.rutas:
            with open(ruta_archivo,'r',encoding='utf-8') as archivo:
                datos_enuciado = json.load(archivo)

            nom_format = os.path.basename(ruta_archivo)
            ruta_carp_principal = '/'.join(ruta_archivo.split('/')[:-2])

            for pos,cell in enumerate(datos_enuciado['cells']):
                if cell['cell_type'] == 'code':

                    datos_enuciado['cells'][pos]['execution_count'] = None
                    datos_enuciado['cells'][pos]['outputs'] = []
                    v_d_0 = ''
                    v_i_0 = ''
                    for i in range(len(cell['source'])):
                        line = cell['source'][i]
                        line_class= fucniones_strings.linea(line=line)
                        com,v_i, v_d, l_e, v_v = [line_class.comentario(), line_class.var_indepe(), line_class.var_dep(), line_class.line_especial(),line_class.ver_valor()]
                        if 'import' in v_v:
                            datos_enuciado['cells'][pos]['source'][i] =  v_v
                        else:
                            if v_i_0 != '' and v_v != '':
                                datos_enuciado['cells'][pos]['source'][i] =  v_v
                            else:
                                if v_d != '':
                                    left = ((v_d.split('=')[0]).replace('\t','')).replace(' ','')
                                    datos_enuciado['cells'][pos]['source'][i] = com + v_i + f'# Encuentra variable que debe ser {left}\n'
                                    # datos_respuestas['cells'][pos]['source'][i] = com + v_i + f'# Encuentra variable que debe ser {left}\n' + v_d
                                else:
                                    datos_enuciado['cells'][pos]['source'][i] = com + v_i
                        v_i_0 = v_i



            os.makedirs(ruta_carp_principal + '/3-enunciados', exist_ok=True)
            ruta_enucnados = ruta_carp_principal + '/3-enunciados' + '/' + nom_format

            with open(ruta_enucnados, 'w', encoding='utf-8') as nuevo_archivo:
                json.dump(datos_enuciado, nuevo_archivo, ensure_ascii=False, indent=4)
            if self.corregir:
                os.makedirs(ruta_carp_principal + '/4-resuelto_Alumnos', exist_ok=True)
    
    def ejercicio_resuelto(self):
        for ruta_archivo in self.rutas:
            with open(ruta_archivo,'r',encoding='utf-8') as archivo:
                datos_respuestas = json.load(archivo)

            nom_format = os.path.basename(ruta_archivo)
            ruta_carp_principal = '/'.join(ruta_archivo.split('/')[:-2])

            for pos,cell in enumerate(datos_respuestas['cells']):
                if cell['cell_type'] == 'code':
                    datos_respuestas['cells'][pos]['execution_count'] = None
                    datos_respuestas['cells'][pos]['outputs'] = []

                    for i in range(len(cell['source'])):
                        line = cell['source'][i]
                        line_class= fucniones_strings.linea(line=line)
                        com,v_i, v_d, l_e, v_v = [line_class.comentario(), line_class.var_indepe(), line_class.var_dep(), line_class.line_especial(),line_class.ver_valor()]
                        
                        if v_d != '':
                            left = ((v_d.split('=')[0]).replace('\t','')).replace(' ','')
                            datos_respuestas['cells'][pos]['source'][i] = com + f'# Encuentra variable que debe ser {left}\n' + v_d
                        else:
                            datos_respuestas['cells'][pos]['source'][i] = com + v_i + v_v

            os.makedirs(ruta_carp_principal + '/2-ejercicio_resuelto', exist_ok=True)
            ruta_respuestas = ruta_carp_principal + '/2-ejercicio_resuelto' + '/' + nom_format

            with open(ruta_respuestas, 'w', encoding='utf-8') as nuevo_archivo:
                json.dump(datos_respuestas, nuevo_archivo, ensure_ascii=False, indent=4)