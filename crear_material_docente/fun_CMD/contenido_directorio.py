import os

class  Directorio:

    def __init__(self, ruta):
        self.ruta = ruta

    def archivos(self):
        return [os.path.join(self.ruta, item) for item in os.listdir(self.ruta) if os.path.isfile(os.path.join(self.ruta, item))]
    
    def carpetas(self):
        return [os.path.join(self.ruta, item) for item in os.listdir(self.ruta) if os.path.isdir(os.path.join(self.ruta, item))]
    
    def all_archivos(self):
        if type(self.ruta)==str:
            rutas = [self.ruta]
        archivos_all = []
        carpetas_finales = []
        while rutas != []:
            for ruta in rutas:
                archivos_all += Directorio(ruta=ruta).archivos()
                carpetas_finales += Directorio(ruta=ruta).carpetas()
            rutas = carpetas_finales
            carpetas_finales = []
        return archivos_all
    
    def all_carpetas(self):
        if type(self.ruta)==str:
            rutas = [self.ruta]
        carpetas_all = []
        carpetas_finales = []
        while rutas != []:
            for ruta in rutas:
                carpetas_finales += Directorio(ruta=ruta).carpetas()
            rutas = carpetas_finales
            carpetas_all += carpetas_finales
            carpetas_finales = []
        return carpetas_all
    
class Filtros_formato:
    def __init__(self, rutas, formatos_elejidos = '', formatos_eliminados = ''):
        self.rutas = rutas
        self.formatos_elejidos = formatos_elejidos
        self.formatos_eliminados = formatos_eliminados
    

    def elejir(self):
        new_lista = []
        if self.formatos_elejidos == '':
            return new_lista
        else:
            for ruta in self.rutas:
                for formato in (self.formatos_elejidos.replace(' ','')).split(','):
                    formato_ruta = ruta.split('.')[-1]
                    if formato_ruta.lower() == formato.lower():
                        new_lista.append(ruta)
                        break
            return new_lista
    
    def eliminar(self):
        new_lista = []
        if self.formatos_eliminados == '':
            return new_lista
        else:
            for ruta in self.rutas:
                for formato in (self.formatos_eliminados.replace(' ','')).split(','):
                    formato_ruta = ruta.split('.')[-1]
                    if formato_ruta.lower() != formato.lower():
                        new_lista.append(ruta)
                        break
            return new_lista


class Filtros_carpetas:

    def __init__(self, rutas, carpetas_elejidas = '', carpetas_eliminadas = ''):
        self.rutas = rutas
        self.carpetas_elejidas = carpetas_elejidas
        self.carpetas_eliminadas = carpetas_eliminadas


    def elejir(self):
        new_lista = []
        if self.carpetas_elejidas == '':
            return new_lista
        else:
            for ruta in self.rutas:
                for carpeta in (self.carpetas_elejidas.replace(' ','')).split(','):
                    if '/' + carpeta +'/' in ruta:
                        new_lista.append(ruta)
                        break
            return new_lista
        
    def eliminar(self):
        new_lista = []
        if self.carpetas_elejidas == '':
            return new_lista
        else:
            for ruta in self.rutas:
                for carpeta in (self.carpetas_elejidas.replace(' ','')).split(','):
                    if not ('/' + carpeta +'/' in ruta):
                        new_lista.append(ruta)
                        break
            return new_lista
        
    
        
class Filtros_archivos:

    def __init__(self, rutas, archivos_elejidos = '', archivos_eliminados = ''):
        self.rutas = rutas
        self.archivos_elejidos = archivos_elejidos
        self.archivos_eliminados = archivos_eliminados

    def elejir(self):
        new_lista = []
        if self.archivos_elejidos == '':
            return new_lista
        else:
            for ruta in self.rutas:
                for arch in (self.archivos_elejidos.replace(' ','')).split(','):
                    nombre_archivo = '.'.join(os.path.basename(ruta).split('.')[:-1])
                    if nombre_archivo == arch:
                        new_lista.append(ruta)
                        break
            return new_lista
    
    def eliminar(self):
        new_lista = []
        if self.archivos_eliminados == '':
            return new_lista
        else:
            for ruta in self.rutas:
                for arch in (self.archivos_eliminados.replace(' ','')).split(','):
                    nombre_archivo = '.'.join(os.path.basename(ruta).split('.')[:-1])
                    if nombre_archivo == arch:
                        new_lista.append(ruta)
                        break
            return new_lista
    
# archivos = Directorio(ruta = '/home/pol/Escritorio/carpeta_prova').all_archivos()
# archivos_txt = Filtros_formato(rutas=archivos,formatos_elejidos='ipynb')

# print(Directorio(ruta = '/home/pol/Escritorio/carpeta_prova').archivos())
