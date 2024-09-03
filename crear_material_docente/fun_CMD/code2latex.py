import random

class codigo_cifrado:
    def __init__(self, strings, var = [], var_cif = [], operadores = '+,-,*,^,/'):
        self.strings = strings
        self.var = var
        self.var_cif = var_cif
        self.operadores = operadores

    def acondicionar_strings(self):
        return self.strings.replace('**','^').replace('\t','').replace(' ','')

    def extraer_variables(self):
        # new_stirng = self.strings.replace('**','^').replace('\t','').replace(' ','')
        new_string = codigo_cifrado(self.strings).acondicionar_strings()
        if '=' in new_string:
            left, rigth = new_string.split('=')
            self.var.append(left)
        else:
            rigth = new_string

        i = 0
        while i < len(rigth):
            for op in (self.operadores.replace(' ','').replace('\t','')).split(','):
                if rigth[i] == op:
                    break
            if rigth[i] == op:
                rigth = rigth[:i] + '$@#$' + rigth[i+1:]
                i += len('$@#$')
            i += 1
        [self.var.append(i) for i in rigth.split('$@#$')]
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
        new_line = ''
        for i in range(len(self.var)):
            j = len(self.var[i]) + inicio
            while j <= len(line):
                if line[j-len(self.var[i]):j] == self.var[i]:
                    new_line += line[inicio:j-len(self.var[i])] + self.var_cif[i]
                    break
                j += 1
            inicio = j
        # if j == len(line) and 
        return new_line
                    
class acondicionar_operaciones:
    def __init__(self, strings, var = [], var_cif = [], operadores = '+,-,*,^,/'):
        self.strings = strings
        self.var = var
        self.var_cif = var_cif
        self.operadores = operadores

    def intervalo(self):
        list_intervalos = []
        tipos = ['[]','()','{}']
        line = codigo_cifrado(self.strings).acondicionar_strings()
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
            secmentos_den.append(' { '+sec+' } ')
            line = line.replace(sec, ' { '+sec+' } ')

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
            line = line.replace(sec[::-1], ' { '+sec[::-1]+' } ')        
        return line
    # Se tiene que definir una fucnion para los exponentes!!!


# strings = '(5 * 3) ** 3 / (4 + 3)'
strings = '50 / 130 * 5 * 3 ^ 2 / 4 / 7 + 6 / 8 / 9'
line = codigo_cifrado(strings = strings).acondicionar_strings()
var = codigo_cifrado(strings = strings).extraer_variables()
var_cod = codigo_cifrado(strings = strings, var=var).codificar_variables()
intervalos = acondicionar_operaciones(strings = strings).intervalo()
line_cifrada = codigo_cifrado(strings = strings).cifrar_line()
new_line = acondicionar_operaciones(strings = strings).division()

# print(var)
# print(var_cod)
print(new_line)

    

            



# def cifrar_strings(lista_str, lista_cifrada = []):
