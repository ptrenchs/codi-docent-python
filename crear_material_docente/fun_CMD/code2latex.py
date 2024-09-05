import random

class areglar_strings:
    def __init__(self, strings = '', operadores = '+,-,*,^,/,(,),='):
        self.strings = strings
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


class codigo_cifrado:
    def __init__(self, strings = '', var = [], var_cif = [], otras_listas = [], operadores = '+,-,*,^,/,(,),='):
        self.strings = areglar_strings(strings.replace('**','^')).eliminar_espacios_laterales()
        self.var = var
        self.var_cif = var_cif
        self.otras_listas = otras_listas
        self.operadores = operadores

    def acondicionar_strings(self):
        return self.strings.replace('\t','').replace(' ','')

    def extraer_variables(self):
        new_string = self.strings
        inicio = 0
        for i in range(len(new_string)):
            if new_string[i] in  (self.operadores.replace(' ','').replace('\t','')).split(','):
                if inicio != 0:
                    segmento = new_string[inicio+1:i].replace('\t','').replace(' ','')
                else:
                    segmento = new_string[inicio:i].replace('\t','').replace(' ','')
                if segmento != '' and segmento not in self.var_cif:
                    self.var.append(segmento)
                inicio = i
        segmento = new_string[inicio+1:].replace('\t','').replace(' ','')
        if segmento != '' and segmento not in self.var_cif:
            self.var.append(segmento)
        return self.var
    
    def codificar_variables(self):
        cifrado  = ['!?¿¡', '·$%', '|@#~']
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
                new_line += line[j:]
        if inicio == 0:
            new_line = line
        return new_line
                    
class acondicionar_operaciones:
    def __init__(self, strings, var = [], var_cif = [], operadores = '+,-,*,^,/,=,(,)'):
        self.strings = areglar_strings(strings.replace('**','^')).eliminar_espacios_laterales()
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
                list_intervalos.append(line[inicio:i+1])
                car_inicio = ''
                car_fin = ''

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
                elif line[i] in '+-*' and line[inicio+1:i] != '':
                    init_var = ''
                    segmentos.append(line[inicio+1:i])
            if init_var != '' and line[inicio+1:] != '':
                segmentos.append(line[inicio+1:])
            for seg in segmentos:
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
                elif init_var and line_reverse[i] in '+-' and line_reverse[inicio+1:i] != '':
                    segmentos.append(line_reverse[inicio+1:i])
                    init_var = False
                elif init_var and line_reverse[i] in '/' and line_reverse[inicio+1:mult_pos] != '':
                    segmentos.append(line_reverse[inicio+1:mult_pos])
                    inicio = i
            if init_var and line_reverse[inicio+1:] != '':
                segmentos.append(line_reverse[inicio+1:])

            for seg in segmentos:
                seg = areglar_strings(seg).eliminar_espacios_laterales()
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
                seg = areglar_strings(seg).eliminar_espacios_laterales()
                line = line.replace(seg, '{ ' + seg.replace('^','^ {') + ' }' +''.join([' }' for i in seg if i == '^']))
                # if len([' }' for i in seg if i == '^']) == 0:
                #     line = line.replace(seg, '{ ' + seg.replace('^','^ {') + ' }')
                # else:
                #     line = line.replace(seg, '{ ' + seg.replace('^','^ {') + ''.join([' }' for i in seg if i == '^']))
                # line = line.replace(seg, '{ ' + seg + ' }')
            # print(line)
        return line




# strings = '(5 * 3) ** 3 / (4 + 3)'
line_old = '50 / 130 * 5 * 3 ^ 2 / 4 / 7 + 6 / 8 / 9 + 129 ^ (3 + 4 + 5 * (3+2)) ^ -5 ^ 7 + (88 + 99) / (100 +4) + 40 ^ 5'
# line_old = '50 / 130 * 5 * 3 ^ 2 / 4 / 7 + 6 / 8 / 9 + 129 ^ (3 + 4 + 5 ) ^ -5 ^ 7 + (88 + 99) / (100 +4) + 40 ^ 5'
cifrado = []
no_cifrado = []


print(line_old)
# line = codigo_cifrado(strings = strings).acondicionar_strings()
no_cifrado += codigo_cifrado(strings = line_old,var = no_cifrado, var_cif = cifrado).extraer_variables()
cifrado += codigo_cifrado(strings = line_old, var = no_cifrado, var_cif = cifrado).codificar_variables()
line_cif = codigo_cifrado(strings = line_old, var = no_cifrado, var_cif = cifrado).cifrar_line()
segmentos = [line_cif]#[i for i in no_cifrado]
segmentos_cifrados = []#[i for i in cifrado]

while True:
    # segmentos = []#[i for i in no_cifrado]
    # segmentos_cifrados = []#[i for i in cifrado]
    new_segmentos = []
    for seg in segmentos:
        line = seg
        new_segmentos += acondicionar_operaciones(strings = line).intervalo()
        print(new_segmentos)
        segmentos_cifrados += codigo_cifrado(strings = line, var = new_segmentos, var_cif= segmentos_cifrados, otras_listas = cifrado).codificar_variables()
        line = codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados).cifrar_line()
        line = acondicionar_operaciones(strings = line).division()

        new_segmentos += acondicionar_operaciones(strings = line).intervalo()
        segmentos_cifrados += codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados, otras_listas = cifrado).codificar_variables()
        line = codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados).cifrar_line()
        line = acondicionar_operaciones(strings = line).exponenete()

        new_segmentos += acondicionar_operaciones(strings = line).intervalo()
        # print(new_segmentos)
        segmentos_cifrados += codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados, otras_listas = cifrado).codificar_variables()
        line = codigo_cifrado(strings = line, var = new_segmentos, var_cif = segmentos_cifrados).cifrar_line()
        line = line.replace(' / ','')
        line = line.replace('*','\\cdot')
        print(seg)
        print(line)
        line_cif = line_cif.replace(seg,line)
        for j in range(len(new_segmentos)):
            line_cif = line_cif.replace(segmentos_cifrados[j],new_segmentos[j])
    
    segmentos = []
    for seg in new_segmentos:
        for car in seg:
            if car in '*/^':
                break
        if car in '*/^':
            segmentos.append(seg)
            
    if segmentos == []:
        break
    else:
        segmentos = []#[i for i in no_cifrado]
        segmentos_cifrados = []#[i for i in cifrado]
    # for i in range(len(segmentos)):
    #     line_cif = line_cif.replace(segmentos_cifrados[i],segmentos[i])
for i in range(len(no_cifrado)):
    line_cif = line_cif.replace(cifrado[i],no_cifrado[i])
print(line_cif)


# mirar la funcion codificar variables