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
        cifrado  = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', '&#@$', '0123456789']
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
    
    def intervalo(self):
        list_intervalos = []
        tipos = ['[]','()','{}']
        line = codigo_cifrado(self.strings).acondicionar_strings()
        car_inicio = ''
        car_fin = ''
        for j in range(len(line)):
            if car_inicio == '':
                for tip in tipos:
                    for i in range(len(tip)):
                        if line[j] == tip[i]:
                            break
                    if line[j] == tip[i]:
                        car_inicio += tip[i]
                        inicio = j
                        break
            else:
                for tip in tipos:
                    for i in range(len(tip)):
                        if line[j] == tip[i]:
                            break
                    if car_inicio[0] == tip[i]:
                        car_inicio += tip[i]
                    else:
                        car_fin += tip[i-1]
                        break
            if len(car_fin) == len(car_inicio) and len(car_inicio) != 0:
                # print(line[inicio:j+1])
                list_intervalos.append(line[inicio:j+1])
                car_inicio = ''
                car_fin = ''
        return list_intervalos

strings = '(5 * 3) ** 3 / 4'
var = codigo_cifrado(strings = strings).extraer_variables()
var_cod = codigo_cifrado(strings = strings, var=var).codificar_variables()
intervalos = codigo_cifrado(strings = strings).intervalo()
print(var)
print(var_cod)
print(intervalos)

    

            



# def cifrar_strings(lista_str, lista_cifrada = []):
