# Misión 1

## Introducción a python

Comandos         | Utilidad
-----------------|------------------------------------------------------
python --version | Muestra la versión de Python instalada
cd               | Cambia el directorio de trabajo
dir o ls         | Lista los archivos y carpetas en el directorio actual
py nombre.py     | Ejecuta un script de Python
mkdir nombre     | Crea una nueva carpeta
rmdir nombre     | Elimina una carpeta vacía
del nombre.ext   | Elimina un archivo específico

## Instalación de paquetes con pip

pip install numpy

Creamos entorno virtual:

python -m venv nombre_del_entorno
Activamos el entorno virtual:

- En Windows: nombre_del_entorno\Scripts\activate

Si hay problemas con la activación en Windows, ejecutar:
Set-ExecutionPolicy Unrestricted
luego Sí y después salir de PowerShell.

Instalamos paquetes desde un archivo requirements.txt del git del proyecto ejemplo:

pip install -r requirements.txt

Desactivamos el entorno virtual:

- En Windows: deactivate
