import os

class  directorio:
    # def filtrar_formato(rutas,formatos):
    #     new_lista = []
    #     for ruta in rutas:
    #         for formato in (formatos.replace(' ','')).split(','):
    #             formato_ruta = ruta.split('.')[-1]
    #             if formato_ruta.lower() == formato.lower():
    #                 new_lista.append(ruta)
    #                 break


    
    def archivos(ruta):
        return [os.path.join(ruta, item) for item in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, item))]
    
    def carpetas(ruta):
        return [os.path.join(ruta, item) for item in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, item))]
    
print(directorio.archivos(ruta = '/home/pol'))
