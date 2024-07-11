import nbformat as nbf

class converitr:

    def py_to_ipynb(py_file_path, ipynb_file_path):
        # Crear un nuevo cuaderno
        nb = nbf.v4.new_notebook()
        
        # Leer el archivo .py
        with open(py_file_path, 'r') as py_file:
            code = py_file.read()
        
        # Crear una nueva celda de código con el contenido del archivo .py
        code_cell = nbf.v4.new_code_cell(code)
        
        # Agregar la celda al cuaderno
        nb.cells.append(code_cell)
        
        # Escribir el cuaderno en un archivo .ipynb
        with open(ipynb_file_path, 'w') as ipynb_file:
            nbf.write(nb, ipynb_file)


    def py_to_ipynb(py_file_path, ipynb_file_path):
        # Crear un nuevo cuaderno
        nb = nbf.v4.new_notebook()
        
        # Leer el archivo .py
        with open(py_file_path, 'r') as py_file:
            lines = py_file.readlines()
        
        cells = []
        code_cell = []
        
        for line in lines:
            # Dividir en celdas en base a líneas en blanco o comentarios especiales
            if line.strip() == "" or line.startswith("#"):
                if code_cell:
                    cells.append(nbf.v4.new_code_cell("".join(code_cell)))
                    code_cell = []
                if line.startswith("#"):
                    cells.append(nbf.v4.new_markdown_cell(line.strip("#").strip()))
            else:
                code_cell.append(line)
        
        # Agregar la última celda si existe
        if code_cell:
            cells.append(nbf.v4.new_code_cell("".join(code_cell)))
        
        # Agregar todas las celdas al cuaderno
        nb.cells.extend(cells)
        
        # Escribir el cuaderno en un archivo .ipynb
        with open(ipynb_file_path, 'w') as ipynb_file:
            nbf.write(nb, ipynb_file)