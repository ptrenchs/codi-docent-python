import random

class codigo_cifrado:
    def __init__(self, strings, var = [], var_cif = [], operadores = '+,-,*,^,/'):
        self.strings = strings
        self.var = var
        self.var_cif = var_cif
        self.operadores = operadores

    def extraer_variables(self):
        new_stirng = self.strings.replace('**','^').replace('\t','').replace(' ','')
        if '=' in new_stirng:
            left, rigth = new_stirng.split('=')
            self.var.append(left)
        else:
            rigth = new_stirng

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

var = codigo_cifrado(strings = '5 * 3 ** 3 / 4').extraer_variables()
var_cod = codigo_cifrado(strings = '5 * 3 ** 3 / 4', var=var).codificar_variables()
print(var)
print(var_cod)
    

            



# def cifrar_strings(lista_str, lista_cifrada = []):
