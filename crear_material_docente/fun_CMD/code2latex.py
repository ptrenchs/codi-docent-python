import random

class areglar_strings:
    def __init__(self, strings = '', operadores = '+,-,*,^,/,(,),='):
        self.strings = strings
        self.operadores = operadores
    
    def eliminar_espacios_laterales(self):
        new_strings = self.strings
        # print([new_strings])
        if new_strings == '':
            return new_strings
        for i in (self.operadores.replace(' ','').replace('\t','')).split(','):
            new_strings = new_strings.replace(i, ' ' + i + ' ')
        while True:
            if new_strings[0] == ' ':
                new_strings = new_strings[0+1:]
            if new_strings[-1] == ' ':
                new_strings = new_strings[:-1]
            if '  ' in new_strings:
                new_strings = new_strings.replace('  ',' ')
            if new_strings[0] != ' ' and new_strings[-1] !=  ' ' and '  ' not in new_strings:
                break

        return new_strings


class codigo_cifrado:
    def __init__(self, strings = '', var = [], var_cif = [], otras_listas = [], operadores = '+,-,*,^,/,(,),='):
        self.strings = areglar_strings(strings.replace('**','^')).eliminar_espacios_laterales()
        if type(var) == str:
            var = var.replace(' ','').replace('\t', '').split(',')
        if type(var_cif) == str:
            var_cif = var_cif.replace(' ','').replace('\t', '').split(',') 
        self.var = var
        self.var_cif = var_cif
        self.otras_listas = otras_listas
        self.operadores = operadores.replace(' ','').replace('\t','').split(',')

    def acondicionar_strings(self):
        return self.strings.replace('\t','').replace(' ','')
    

    def extraer_variables(self):
        new_string = self.strings
        inicio = 0
        for i in range(len(new_string)):
            if new_string[i] in  self.operadores:
                if inicio != 0:
                    segmento = new_string[inicio+1:i].replace('\t','').replace(' ','')
                else:
                    segmento = new_string[inicio:i].replace('\t','').replace(' ','')
                if segmento != '' and segmento not in self.var_cif and segmento not in  self.operadores:
                    self.var.append(segmento)
                inicio = i
        segmento = new_string[inicio+1:].replace('\t','').replace(' ','')
        if segmento != '' and segmento not in self.var_cif:
            self.var.append(segmento)
        return self.var
    
    def codificar_variables(self):
        cifrado  = ['!?¿¡', '·$%', '|@#~', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
        if len(self.var_cif) < len(self.var):
            for v in range(len(self.var_cif), len(self.var)):
                if len(self.var_cif) == 0:
                    self.var_cif.append(''.join([random.choice(j)for j in cifrado]))
                else:
                    while True:
                        num = ''.join([random.choice(j)for j in cifrado])
                        if num not in self.var_cif + self.otras_listas:
                            break
                    self.var_cif.append(num)
        return self.var_cif
    
    def cifrar_line(self):
        inicio = 0
        line = self.strings#codigo_cifrado(self.strings).acondicionar_strings()
        if self.var == []:
            codigo_cifrado(var=codigo_cifrado(strings = line).extraer_variables()).codificar_variables()
        new_line = ''
        # print(self.var)
        if len(self.var) != 0:
            for i in range(len(self.var)):
                j = len(self.var[i]) + inicio
                while j <= len(line):
                    if line[j-len(self.var[i]):j] == self.var[i]:
                        new_line += line[inicio:j-len(self.var[i])] + self.var_cif[i]
                        inicio = j
                        break
                    j += 1
                
            # if j == len(line) and 
            if j!=len(line):
                new_line += line[inicio:]
        if inicio == 0:
            new_line = line

        return new_line
    

                    
class acondicionar_operaciones:

    def __init__(self, strings, var = [], var_cif = [], operadores = '+,-,*,^,/,=,(,)'):
        self.strings = areglar_strings(strings.replace('**','^')).eliminar_espacios_laterales()
        if type(var) == str:
            var = var.replace(' ','').replace('\t', '').split(',')
        if type(var_cif) == str:
            var_cif = var_cif.replace(' ','').replace('\t', '').split(',')
        self.var = var
        self.var_cif = var_cif
        self.operadores = operadores

    def eliminar_espacios_laterales(self):
        new_strings = self.strings
        for i in (self.operadores.replace(' ','').replace('\t','')).split(','):
            new_strings = new_strings.replace(i, ' ' + i + ' ')
        while True:
            if new_strings[0] == ' ':
                new_strings = new_strings[0+1:]
            if new_strings[-1] == ' ':
                new_strings = new_strings[:-1]
            if '  ' in new_strings:
                new_strings = new_strings.replace('  ',' ')
            if new_strings[0] != ' ' and new_strings[-1] !=  ' ' and '  ' not in new_strings:
                break

        return new_strings


    def intervalo(self):
        list_intervalos = []
        tipos = ['()']
        line = self.strings # codigo_cifrado(self.strings).acondicionar_strings()
        # print(line)
        inicio = 0
        if '(' in line:
            car_inicio = ''
            car_fin = ''
            for i in range(len(line)):
                if car_inicio == '':
                    for j in range(len(tipos)):
                        for k in range(len(tipos[j])):
                            if line[i] == tipos[j][k]:
                                break
                        if line[i] == tipos[j][k]:
                            car_inicio += tipos[j][k]
                            inicio = i
                            break
                else:
                    for k in range(len(tipos[j])):
                        if line[i] == tipos[j][k]:
                            break

                    if car_inicio[0] == tipos[j][k]:
                        car_inicio += tipos[j][k]
                    elif line[i] == tipos[j][k]:
                        car_fin += tipos[j][k]                

                if len(car_fin) == len(car_inicio) and len(car_inicio) != 0 and line[inicio:i+1] != '':
                    # print(line[inicio:i+1])
                    list_intervalos.append(line[inicio:i+1])
                    car_inicio = ''
                    car_fin = ''
        if inicio != 0:
            list_intervalos.append(line[inicio:])
        # print(list_intervalos)
        return list_intervalos
    
    
    
    def division(self):
        segmentos_den = []
        segmentos_num = []
        segmentos = []
        init_var = ''
        line = self.strings # codigo_cifrado(self.strings).acondicionar_strings()
        if '/' in line:
            for i in range(len(line)):
                if line[i] == '/' and init_var == '':
                    init_var += line[i]
                    inicio = i
                elif line[i] == '/':
                    init_var += line[i]
                if 1 < len(init_var) and line[i] == '/':
                    line = [j for j in line]
                    line[i] = '*'
                    line = ''.join(line)
                elif init_var != '' and line[i] in '+-*=' and line[inicio+1:i] != '':
                    init_var = ''
                    segmentos.append(line[inicio+1:i])
            if init_var != '' and line[inicio+1:] != '':
                segmentos.append(line[inicio+1:])
            for seg in segmentos:
                # print(seg)
                seg = areglar_strings(seg).eliminar_espacios_laterales()
                segmentos_den.append('{ '+seg+' }')
                line = line.replace(seg, '{ '+seg+' }')

            segmentos = []
            line_reverse = line[::-1]
            init_var = False
            for i in range(len(line_reverse)):
                if line_reverse[i]== '*':
                    mult_pos = i
                if line_reverse[i] == '/' and not init_var:
                    init_var = True
                    inicio = i
                elif init_var and line_reverse[i] in '+-=' and line_reverse[inicio+1:i] != '':
                    segmentos.append(line_reverse[inicio+1:i])
                    init_var = False
                elif init_var and line_reverse[i] in '/' and line_reverse[inicio+1:mult_pos] != '':
                    segmentos.append(line_reverse[inicio+1:mult_pos])
                    inicio = i
            if init_var and line_reverse[inicio+1:] != '':
                segmentos.append(line_reverse[inicio+1:])

            for seg in segmentos:
                seg = areglar_strings(seg).eliminar_espacios_laterales()
                # print(seg)
                segmentos_num.append(' { '+seg[::-1]+' } ')
                line = line.replace(seg[::-1], '\\frac{ '+seg[::-1]+' }')  

        return line
    # Se tiene que definir una fucnion para los exponentes!!!
    def exponenete(self):
        segmento = []
        init_exp = False
        line = self.strings
        if '^' in line:
            for i in range(len(line)):
                if line[i] == '^' and not init_exp:
                    inicio = i
                    init_exp = True
                elif init_exp and line[i] in '/*}' and line[inicio+1:i-1] != '':
                    # print(line[inicio+1:i-1])
                    segmento.append(line[inicio+1:i-1])
                    init_exp = False
                elif init_exp and line[i] in '+-':
                    line_reverse = line[:i][::-1]
                    for j in range(len(line_reverse)):
                        if line_reverse[j] not in ' \t':
                            break
                    if line_reverse[j] != '^' and line[inicio+1:i] != '':
                        # print([line[inicio+1:i]])
                        segmento.append(line[inicio+1:i])
                        init_exp = False
            if init_exp and line[inicio+1:] != '':
                # print(line[inicio+1:])
                segmento.append(line[inicio+1:])
            for seg  in segmento:
                # print(seg)
                seg = areglar_strings(seg).eliminar_espacios_laterales()
                line = line.replace(seg, '{ ' + seg.replace('^','^ {') + ' }' +''.join([' }' for i in seg if i == '^']))

            # print(line)
        return line
    
class latex:

    def __init__(self, var = [], sub_indices = []):
        if type(var) == str:
            var = var.replace(' ','').replace('\t', '').split(',')
        
        if type(sub_indices) == str:
            sub_indices = sub_indices.replace(' ','').replace('\t', '').split(',') 
        self.sub_indices = sorted(sub_indices,key= lambda x: len(x),reverse=True)
        self.var = var



    def acondicionar_var(strings,sub_indices):
        strings_provisional = strings
        inicio = 0
        new_strings = ''
        seguencia = []
        for i in range(len(strings_provisional)):
            if strings_provisional[i].isnumeric():
                seguencia.append('num')
            if strings_provisional[i].islower():
                seguencia.append('min')
            if strings_provisional[i].isupper():
                seguencia.append('may')
            if strings_provisional[i] == '_':
                seguencia = []
            if 1 < len(seguencia):
                if 'num' in seguencia and len(seguencia) != len([1 for sec in seguencia if sec == 'num']):

                    new_strings = strings_provisional[inicio:i] + '_'
                    seguencia = seguencia[1:]
                    inicio = i
                else:
                    if 2 < len(seguencia):
                        if 2 * 'min' == ''.join(seguencia[:-1]) and seguencia[-1] == 'may':
                            new_strings = strings_provisional[inicio:i] + '_'
                            seguencia = seguencia[2:]
                            inicio = i
                        elif 2 * 'may' == ''.join(seguencia[:-1]) and seguencia[-1] == 'min':
                            new_strings = strings_provisional[inicio:i] + '_'
                            seguencia = seguencia[2:]
                            inicio = i
                        else:
                            seguencia = seguencia[1:]

        strings_provisional = new_strings + strings_provisional[inicio:]
        # print([strings_provisional])

        realizados = strings.split('_')
        if len(realizados) <= 1:
            realizados = []
        for sub in sub_indices:
            if sub in strings_provisional and len([1 for real in realizados if sub in real]) == 0:
                realizados.append(sub)
                new_strings = ''
                inicio = 0
                for i in range(len(sub),len(strings_provisional)):
                    if strings_provisional[i-len(sub):i] == sub:
                        if strings[i-1] != '_':
                            new_strings += strings_provisional[inicio:i-len(sub)] + '_' + strings_provisional[i-len(sub):i]
                            inicio = i
                        if i < len(strings_provisional)-2:
                            if strings[i+1] != '_':
                                new_strings += '_'
                new_strings += strings_provisional[inicio:]
                strings_provisional = new_strings
        
        # print(strings_provisional)
        return strings_provisional.replace('_','_{') + len([1 for i in strings_provisional if i == '_']) * '}'
    
    def var2latex(self):
        var_latex = []
        for var in self.var:
            # print(var)
            try:
                eval(var)
                if var in ('1j','1i'):
                    var_latex.append('i')
                elif 'i' in var or 'j' in var:
                    var_latex.append(var.replace('i','') + ' * i')
                else:
                    var_latex(var)
            except:
                var_latex.append(latex.acondicionar_var(strings = var, sub_indices = self.sub_indices))

        return var_latex

    def code2latex(line_old,sub_ind):
        cifrado = []
        no_cifrado = []

        no_cifrado += codigo_cifrado(strings = line_old,var = no_cifrado, var_cif = cifrado).extraer_variables()
        cifrado += codigo_cifrado(strings = line_old, var = no_cifrado, var_cif = cifrado).codificar_variables()
        var_latex = latex(var = no_cifrado,sub_indices = sub_ind).var2latex()
        line_cif = codigo_cifrado(strings = line_old, var = no_cifrado, var_cif = cifrado).cifrar_line()
        segmentos = [line_cif]

        segmentos_provisionales = []
        while True:

            new_segmentos = []
            segmentos_cifrados = []

            for seg in segmentos:
                line = seg
                new_segmentos += acondicionar_operaciones(strings = line).intervalo()
                segmentos_cifrados = codigo_cifrado(strings = line, var = new_segmentos, var_cif= segmentos_cifrados, otras_listas = cifrado).codificar_variables()
                line = codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados).cifrar_line()
                line = acondicionar_operaciones(strings = line).division()
                segmentos_cifrados = codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados, otras_listas = cifrado).codificar_variables()
                line = codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados).cifrar_line()
                line = acondicionar_operaciones(strings = line).exponenete()        
                segmentos_cifrados = codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados, otras_listas = cifrado).codificar_variables()
                line = codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados).cifrar_line()
                line_cif = line_cif.replace(seg,line)

            for j in range(len(new_segmentos)):      
                line_cif = line_cif.replace(segmentos_cifrados[j],new_segmentos[j])
        
            segmentos_provisionales = []

            for seg in new_segmentos:
                if seg not in segmentos:
                    for car in seg:
                        if car in '*/^':
                            break
                if car in '*/^' and seg not in segmentos:
                    segmentos_provisionales.append(seg[1:-1])
            segmentos = segmentos_provisionales
                    
            if segmentos == []:
                break
            else:
                segmentos_cifrados = []

        for i in range(len(no_cifrado)):
            line_cif = line_cif.replace(cifrado[i],var_latex[i])

        line_cif = line_cif.replace(' / ','/')
        
        segmentos = []
        for pos in [i for i in range(len(line_cif)) if line_cif[i] == '/']:
            pos_num_in = pos
            pos_num_fin = pos
            
            corchetes_opne = ''
            corchetes_close = ''
            while pos_num_in:
                if line_cif[pos_num_in] == '{':
                    corchetes_opne += line_cif[pos_num_in]
                if line_cif[pos_num_in] == '}':
                    corchetes_close += line_cif[pos_num_in]
                if len(corchetes_opne) == len(corchetes_close) and len(corchetes_opne) != 0 and line_cif[pos_num_in+1:pos_num_fin-1] != '':
                    segmentos.append(areglar_strings(line_cif[pos_num_in+1:pos_num_fin-1]).eliminar_espacios_laterales())
                    break
                pos_num_in -= 1

            pos_den_in = pos
            pos_den_fin = pos
            corchetes_opne = ''
            corchetes_close = ''
            while pos_num_in:
                if line_cif[pos_den_fin] == '}':
                    corchetes_close += line_cif[pos_den_fin]
                if line_cif[pos_den_fin] == '{':
                    corchetes_opne += line_cif[pos_den_fin]
                if len(corchetes_opne) == len(corchetes_close) and len(corchetes_opne) != 0 and line_cif[pos_den_in+2:pos_den_fin] != '':
                    segmentos.append(areglar_strings(line_cif[pos_den_in+2:pos_den_fin]).eliminar_espacios_laterales())
                    break   
                pos_den_fin += 1
        
        for seg in segmentos:
            if seg[0] == '(' and seg[-1] == ')' and len([i for i in seg if i in '*/^']) == 0:
                line_cif = line_cif.replace(seg,seg[1:-1])
        line_cif = areglar_strings(line_cif.replace('/','')).eliminar_espacios_laterales()
        line_cif = line_cif.replace('(','\\left(')
        line_cif = line_cif.replace(')','\\right)')
        line_cif = line_cif.replace('*','\\cdot')
        # print(no_cifrado)
        # print(cifrado)
        # print(var_latex)
        return line_cif

# strings = '(5 * 3) ** 3 / (4 + 3)'
# line_old = 'r = 50 / 130 * 5 * 3 ^ 2 / 4 / 7 + 6 / 8 / 9 + 129 ^ (3 + 4 + 5 * (3+2)) ^ -5 ^ (7/(40 + 50)) + (88 + 99) / (100 +4) + 40 ^ 5'
# line_old = '50 / 130 * 5 * 3 ^ 2 / 4 / 7 + 6 / 8 / 9 + 129 ^ (3 + 4 + 5 ) ^ -5 ^ 7 + (88 + 99) / (100 +4) + 40 ^ 5'
# line_old = 'zth3 = (z_t1 +z_g1) * (z_l+r_c*(z_t2+z_g2)/(r_c + (z_t2+z_g2))) / ((z_t1 +z_g1) + (z_l +r_c*(z_t2+z_g2)/(r_c + (z_t2+z_g2))))'
# line_old = '((ar**2+r**2)/2)**0.5'
# print('$$ ' + latex.code2latex(line_old, 'th,g,t') + ' $$')
# ---------------------------------------------------------

    # 

# # mirar la funcion codificar variables
# # zth3 = \frac{ ( zt1 + zg1 ) * (zl + \frac{ rc * ( zt2 + zg2 ) }/{  rc + ( zt2 + zg2 )  }) }/{ (( zt1 + zg1 ) + (zl + \frac{ rc * ( zt2 + zg2 ) }/{  rc + ( zt2 + zg2 )  })) }


# # ---------------------------------------------------------

# Se tiene que terminar la funcion var2latex