import random

class codigo_cifrado:
    def __init__(self, strings = None, var = [], var_cif = [], operadores = '+,-,*,^,/,(,),='):
        self.strings = strings
        self.var = var
        self.var_cif = var_cif
        self.operadores = operadores

    def acondicionar_strings(self):
        return self.strings.replace('**','^').replace('\t','').replace(' ','')

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
                        if num not in self.var_cif:
                            break
                    self.var_cif.append(num)
        return self.var_cif
    
    def cifrar_line(self):
        inicio = 0
        line = self.strings.replace('**','^')#codigo_cifrado(self.strings).acondicionar_strings()
        if self.var == []:
            codigo_cifrado(var=codigo_cifrado(strings = line).extraer_variables()).codificar_variables()
        new_line = ''
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
        return new_line
                    
class acondicionar_operaciones:
    def __init__(self, strings, var = [], var_cif = [], operadores = '+,-,*,^,/'):
        self.strings = strings
        self.var = var
        self.var_cif = var_cif
        self.operadores = operadores

    def intervalo(self):
        list_intervalos = []
        tipos = ['[]','()']
        line = self.strings.replace('**','^') # codigo_cifrado(self.strings).acondicionar_strings()
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

            if len(car_fin) == len(car_inicio) and len(car_inicio) != 0:
                list_intervalos.append(line[inicio:i+1])
                car_inicio = ''
                car_fin = ''

        return list_intervalos
    
    def division(self):
        secmentos_den = []
        secmentos_num = []
        secmentos = []
        init_var = ''
        line = codigo_cifrado(self.strings).acondicionar_strings()
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
            elif line[i] in '+-*':
                init_var = ''
                secmentos.append(line[inicio+1:i])
        if init_var != '':
            secmentos.append(line[inicio+1:])
        for sec in secmentos:
            secmentos_den.append('( '+sec+' )')
            line = line.replace(sec, '( '+sec+' )')

        secmentos = []
        line_reverse = line[::-1]
        init_var = False
        for i in range(len(line_reverse)):
            if line_reverse[i]== '*':
                mult_pos = i
            if line_reverse[i] == '/' and not init_var:
                init_var = True
                inicio = i
            elif init_var and line_reverse[i] in '+-':
                secmentos.append(line_reverse[inicio+1:i])
                init_var = False
            elif init_var and line_reverse[i] in '/':
                secmentos.append(line_reverse[inicio+1:mult_pos])
                inicio = i
        if init_var:
            secmentos.append(line_reverse[inicio+1:])

        for sec in secmentos:
            secmentos_num.append(' { '+sec[::-1]+' } ')
            line = line.replace(sec[::-1], '\\frac{ '+sec[::-1]+' }')        
        return line
    # Se tiene que definir una fucnion para los exponentes!!!
    def exponenete(self):
        segmento = []
        init_exp = False
        line = self.strings.replace('**','^')
        for i in range(len(line)):
            if line[i] == '^' and not init_exp:
                inicio = i
                init_exp = True
            elif init_exp and line[i] in '/*':
                segmento.append(line[inicio+1:i-1])
                init_exp = False
            elif init_exp and line[i] in '+-':
                if line[i-1] != '^':
                    # print(line[inicio+1:i])
                    segmento.append(line[inicio+1:i])
                    init_exp = False
        if init_exp:
            segmento.append(line[inicio+1:])
        for seg  in segmento:
            line = line.replace(seg, '( ' + seg + ' )')
        return line




# strings = '(5 * 3) ** 3 / (4 + 3)'
line = '50 / 130 * 5 * 3 ^ 2 / 4 / 7 + 6 / 8 / 9 + 129 ^ (3 + 4) ^ -5 ^ 7 + (88 + 99) / (100 +4) + 40 ^ 5'
cifrado = []
no_cifrado = []


print(line)
# line = codigo_cifrado(strings = strings).acondicionar_strings()
no_cifrado += codigo_cifrado(strings = line,var = no_cifrado, var_cif = cifrado).extraer_variables()
cifrado += codigo_cifrado(strings = line, var = no_cifrado, var_cif = cifrado).codificar_variables()
line = codigo_cifrado(strings = line, var = no_cifrado, var_cif = cifrado).cifrar_line()

segmentos = []
segmentos_cifrados = []

segmentos += acondicionar_operaciones(strings = line).intervalo()
segmentos_cifrados += codigo_cifrado(strings = line, var = segmentos, var_cif= segmentos_cifrados).codificar_variables()
line = codigo_cifrado(strings = line, var = segmentos, var_cif = segmentos_cifrados).cifrar_line()
print(line)
line = acondicionar_operaciones(strings = line).division()
print(line)
segmentos += acondicionar_operaciones(strings = line).intervalo()
segmentos_cifrados += codigo_cifrado(strings = line, var = segmentos, var_cif = segmentos_cifrados).codificar_variables()
line = codigo_cifrado(strings = line, var = segmentos, var_cif = segmentos_cifrados).cifrar_line()
print(line)
line = acondicionar_operaciones(strings = line).exponenete()
segmentos += acondicionar_operaciones(strings = line).intervalo()
segmentos_cifrados += codigo_cifrado(strings = line, var = segmentos, var_cif = segmentos_cifrados).codificar_variables()
line = codigo_cifrado(strings = line, var = segmentos, var_cif = segmentos_cifrados).cifrar_line()

print(line)
# print(var)
# print(var_cod)
# print(intervalos)
# print(intervalos_cifrados)
# print(line)

    
# ¡¡¡ Se tiene que hacer una funcion para especificar que es parentesisi i que es corchete !!!
            



# def cifrar_strings(lista_str, lista_cifrada = []):
