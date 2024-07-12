import os
import json
from fun_CMD import contenido_directorio
import subprocess

def cambiar_jason():

    script_path = os.path.abspath(__file__)
    split_path = script_path.split('/')
    for i in range(len(split_path)):
        if 'codi-docent-python' == split_path[i]:
            break
    carpeta_principal_codigo = '/'.join(split_path[:i+1])

    for carp in contenido_directorio.Directorio(carpeta_principal_codigo).all_carpetas():
        if os.path.basename(carp).split('.')[0] == 'python3':
            break

    for carp_activ in contenido_directorio.Directorio(carpeta_principal_codigo).all_archivos():
        if os.path.basename(carp_activ) == 'activate':
            break

    # Ruta al archivo settings.json
    # Esta es la ruta típica en Windows; ajusta según tu sistema operativo y configuración
    # settings_path = os.path.expanduser("~/.config/Code/User/settings.json")
    settings_path = os.path.expanduser("~/.vscode/settings.json")
    # Intérprete de Python que deseas establecer
    new_interpreter_path = carp

    antigua_configuracion = {}

    # Lee el contenido actual del archivo settings.json
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as file:
            settings = json.load(file)
        antigua_configuracion = settings
    else:
        settings = {}

    # Modifica o agrega la configuración del intérprete de Python
    settings["python.pythonPath"] = new_interpreter_path

    # Escribe los cambios de vuelta al archivo settings.json
    with open(settings_path, 'w') as file:
        json.dump(settings, file, indent=4)

    if antigua_configuracion == {}:
        antigua_configuracion = settings

    # Ruta al entorno virtual (ajústala según tu configuración)
    ruta_entorno_virtual = carp_activ

    # Comando para activar el entorno virtual
    comando_activacion = f'. {ruta_entorno_virtual}'
    print(comando_activacion)
    # Ejecutar el comando en la terminal
    resultado = subprocess.run(comando_activacion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # resultado = subprocess.run(['bash', '-c', comando_activacion], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Mostrar salida y posibles errores
    if resultado.returncode == 0:
        print("Entorno virtual activado correctamente.")
        print(resultado.stdout)
    else:
        print("Error al activar el entorno virtual:")
        print(resultado.stderr)

    return antigua_configuracion