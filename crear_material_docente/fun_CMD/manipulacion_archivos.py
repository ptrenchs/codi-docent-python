from fun_CMD import fucniones_strings
from fun_CMD import code2latex
import uuid
import json
import os

class Material:
    def __init__(self, rutas, corregir = False, sub_indice = ''):
        self.rutas = rutas
        self.corregir = corregir
        self.sub_indice = sub_indice

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
                                    # datos_ref['cells'][pos]['source'][i] = com + v_i + f'# Encuentra variable que debe ser {left}\n' + v_d
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
        id_s = []
        for ruta_archivo in self.rutas:
            with open(ruta_archivo,'r',encoding='utf-8') as archivo:
                datos_ref = json.load(archivo)
            with open(ruta_archivo,'r',encoding='utf-8') as archivo:
                datos_respuestas= json.load(archivo)

            nom_format = os.path.basename(ruta_archivo)
            ruta_carp_principal = '/'.join(ruta_archivo.split('/')[:-2])
            datos_respuestas['cells'] = []
            for pos,cell in enumerate(datos_ref['cells']):
                datos_respuestas['cells'].append(cell)
                id_s.append(datos_ref['cells'][pos]['id'])
                if cell['cell_type'] == 'code':
                    datos_respuestas['cells'][-1]['execution_count'] = None
                    datos_respuestas['cells'][-1]['outputs'] = []                    
                    new_lines = []
                    new_lines_m = []
                    for i in range(len(cell['source'])):
                        line = cell['source'][i]
                        line_class= fucniones_strings.linea(line=line)
                        com,v_i, v_d, l_e, v_v = [line_class.comentario(), line_class.var_indepe(), line_class.var_dep(), line_class.line_especial(),line_class.ver_valor()]
                        
                        if v_d != '':
                            left = ((v_d.split('=')[0]).replace('\t','')).replace(' ','')
                            # datos_ref['cells'][pos]['source'][i] = com + f'# Encuentra variable que debe ser {left}\n' + v_d
                            new_lines.append(com + f'# Encuentra variable que debe ser {left}\n')
                            new_lines.append(v_d)
                            # '$$ ' + code2latex.latex.code2latex(line_old,sub_ind='th') + ' $$'
                            new_lines_m.append(com + '# Encuentra variable que debe ser $ '+ code2latex.latex.code2latex(left,sub_ind=self.sub_indice) + ' $\n')
                            new_lines_m.append('$$ ' + code2latex.latex.code2latex(v_d,sub_ind=self.sub_indice) + ' $$')
                        else:
                            # datos_ref['cells'][pos]['source'][i] = com + v_i + v_v
                            new_lines.append(com + v_i + v_v)
                            new_lines_m.append(com + '$$ ' + code2latex.latex.code2latex(v_i + v_v,sub_ind=self.sub_indice) + ' $$')
                    # print(new_lines)
                    datos_respuestas['cells'][-1]['source'] = new_lines
                    while True:
                        new_id_s = str(uuid.uuid4())
                        if new_id_s not in id_s:
                            break
                    for i in range(len(new_lines_m)):
                        # print(new_lines_m[i])
                        if 'import' in new_lines_m[i] :#or code2latex.areglar_strings(new_lines_m[i].replace('$$ ','').replace(' $$','')).eliminar_espacios_laterales().split(' ') == 1 and '#' not in new_lines_m[i]:
                            print(new_lines_m[i])
                            new_lines_m[i] = ''
                        if len(code2latex.areglar_strings(new_lines_m[i].replace('$$ ','').replace(' $$','')).eliminar_espacios_laterales().split(' ')) == 1 :
                            print(new_lines_m[i])
                            new_lines_m[i] = ''
                        if '\n' in new_lines_m[i]:
                            new_lines_m[i] = new_lines_m[i].replace('\n','') + '\n'
                        new_lines_m[i] = new_lines_m[i].replace('#','')
                    # print(new_lines_m)  
                    if ''.join(new_lines_m).replace('\n','')!='':
                        datos_respuestas['cells'] = datos_respuestas['cells'][:-1] + [{"cell_type": "markdown","id": new_id_s,"metadata": {},"source": new_lines_m}] + [datos_respuestas['cells'][-1]]



            os.makedirs(ruta_carp_principal + '/2-ejercicio_resuelto', exist_ok=True)
            ruta_respuestas = ruta_carp_principal + '/2-ejercicio_resuelto' + '/' + nom_format

            with open(ruta_respuestas, 'w', encoding='utf-8') as nuevo_archivo:
                json.dump(datos_respuestas, nuevo_archivo, ensure_ascii=False, indent=4)