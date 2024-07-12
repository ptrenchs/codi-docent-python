#!/bin/bash

# Directorio donde se creará el entorno virtual
VENV_DIR="~/.venvs"

# Asegúrate de expandir la tilde correctamente para el directorio de entornos virtuales
VENV_DIR=$(eval echo "$VENV_DIR")

# Nombre del entorno virtual (será el nombre de la carpeta donde se encuentra este script)
script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
VENV_NAME=$(basename "$script_dir")

# Verificar si el directorio VENV_DIR existe, si no, crearlo
if [ ! -d "$VENV_DIR" ]; then
    echo "Creando directorio $VENV_DIR..."
    mkdir -p "$VENV_DIR"
fi

echo "El directorio de entornos virtuales es: $VENV_DIR"

# Construir la ruta completa del entorno virtual
ruta_completa="$VENV_DIR/$VENV_NAME"
echo "La ruta completa del entorno virtual es: $ruta_completa"

# Comprobar si el entorno virtual ya existe dentro del directorio
if [ ! -d "$ruta_completa" ]; then
    echo "Creando entorno virtual $VENV_NAME en $VENV_DIR..."
    python3 -m venv "$ruta_completa"
fi

# Activar el entorno virtual
source "$ruta_completa/bin/activate"

# Instalar dependencias desde requirements.txt en el mismo directorio que este script
echo "Instalando dependencias desde requirements.txt en $(dirname "$0")..."
pip install -r "$(dirname "$0")/requirements.txt"

echo "Entorno virtual configurado y dependencias instaladas."
