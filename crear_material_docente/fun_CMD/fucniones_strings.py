class linea:
    def __init__(self, line, coment = '#', sep_enter = ' ,\t,\n', especiales = 'if,else,break,for,while'):
        self.line = line
        self.coment = coment
        self.sep_enter = sep_enter
        self.especiales = especiales
    def var_indepe(self):
        cometario = linea(line=self.line).comentario()
        new_line = self.line.replace(cometario,'')
        for sep in self.sep_enter.split(','):
            new_line = new_line.replace(sep,'')
        if new_line != '':
            new_line = self.line.replace(cometario,'')
            for i,car in enumerate(new_line):
                if not (car in self.sep_enter.split(',')[:-1]):
                    break
            new_line = new_line[i:]
            for esp in self.especiales.split(','):
                if new_line.startswith(esp):
                    break
            if not new_line.startswith(esp):
                left = new_line.split('=')[0]
                rigth = new_line.split('=')[1]
                try:
                    eval(rigth)
                    return self.line.replace(cometario,'')
                except:
                    pass
            else:
                return ''

        else:
            return ''
        
    def var_dep(self):
        cometario = linea(line=self.line).comentario()
        new_line = self.line.replace(cometario,'')
        for sep in self.sep_enter.split(','):
            new_line = new_line.replace(sep,'')
        if new_line != '':
            new_line = self.line.replace(cometario,'')
            for i,car in enumerate(new_line):
                if not (car in self.sep_enter.split(',')[:-1]):
                    break
            new_line = new_line[i:]
            for esp in self.especiales.split(','):
                if new_line.startswith(esp):
                    break
            if not new_line.startswith(esp):
                # left = new_line.split('=')[0]
                rigth = new_line.split('=')[1]
                try:
                    eval(rigth)
                    return ''
                except:
                    pass
            else:
                return self.line.replace(cometario,'')

        else:
            return ''

    def comentario(self):
        for i,car in enumerate(self.line):
            for com in self.coment.split(','):
                if com == car:
                    break
            if com == car:
                break
        if com == car:
            comentario = self.line[i+1:]
            for i,car in enumerate(comentario):
                if not (car in self.sep_enter.split(',')[:-1]):
                    break
            return '# ' + comentario[i:]
        else:
            return ''
        
# print(linea(line='x = 1 # hola').var_dep())