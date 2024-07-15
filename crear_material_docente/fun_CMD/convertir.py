import nbformat as nbf
import os

class converitr:
    
    # def py_to_ipynb(py_file_path, ipynb_file_path):
    def py_to_ipynb(rutas):
        if type(rutas)==str:
            rutas = [rutas]
        lista_ipynb = []
        for ruta in rutas:
            formato = ruta.split('.')[-1]
            if formato.lower() == 'py':
                ruta_py = ruta
                carpeta_py = ruta_py.split('/')[-2]
                carpeta_formato = 'Carpeta_' + formato
                archivo = os.path.basename(ruta_py)
                nombre = '.'.join(archivo.split('.')[:-1])
                if carpeta_py == carpeta_formato:
                    carpeta_ipynb = '/'.join(ruta_py.split('/')[:-2]) + '/Carpeta_ipynb'
                else:
                    carpeta_ipynb = '/'.join(ruta_py.split('/')[:-2]) + '/Carpeta_ipynb'
                os.makedirs(carpeta_ipynb, exist_ok=True)
                ruta_ipynb = carpeta_ipynb + '/' + nombre + '.ipynb'
                # Crear un nuevo cuaderno
                nb = nbf.v4.new_notebook()
                
                # Leer el archivo .py
                with open(ruta_py, 'r') as py_file:
                    code = py_file.read()
                
                # Crear una nueva celda de código con el contenido del archivo .py
                code_cell = nbf.v4.new_code_cell(code)
                
                # Agregar la celda al cuaderno
                nb.cells.append(code_cell)
                
                # Escribir el cuaderno en un archivo .ipynb
                with open(ruta_ipynb, 'w') as ipynb_file:
                    nbf.write(nb, ipynb_file)
                lista_ipynb.append(ruta_ipynb)
        return lista_ipynb

    def ipynb_to_py(rutas):
        if type(rutas)==str:
            rutas = [rutas]
        lista_py = []
        for ruta in rutas:
            formato = ruta.split('.')[-1]
            if formato.lower() == 'ipynb':
                ruta_ipynb = ruta
                carpeta_ipynb = ruta_ipynb.split('/')[-2]
                carpeta_formato = 'Carpeta_' + formato
                archivo = os.path.basename(ruta_ipynb)
                nombre = '.'.join(archivo.split('.')[:-1])
                if carpeta_ipynb == carpeta_formato:
                    carpeta_py= '/'.join(ruta_ipynb.split('/')[:-2]) + '/Carpeta_py'
                else:
                    carpeta_py = '/'.join(ruta_ipynb.split('/')[:-1]) + '/Carpeta_py'
                print(carpeta_py,ruta_ipynb)
                os.makedirs(carpeta_py, exist_ok=True)
                ruta_py = carpeta_py + '/' + nombre + '.py'
                # Lee el notebook
                with open(ruta_ipynb, 'r', encoding='utf-8') as f:
                    nb = nbf.read(f, as_version=4)

                # Abre el archivo .py para escribir
                with open(ruta_py, 'w', encoding='utf-8') as f:
                    for cell in nb.cells:
                        if cell.cell_type == 'code':
                            # Escribe el contenido de la celda de código en el archivo .py
                            f.write(cell.source + '\n\n')
                lista_py.append(ruta_py)
        return lista_py