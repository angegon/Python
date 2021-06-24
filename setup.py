# Describe la configuración del paquete distribuible
# una vez relleno hay que ejecutar en consola python "setup.py sdist"
# Una vez creado el paquete se instala con "pip3 install paquete_distribuible-0.1.tar.gz"
# con lo cual se consigue que los métodos etc, se puedan usar desde cualquier ruta
# Para desinstalar el paquete sería con "pip3 uninstall paquete_distribuible"

from setuptools import setup

setup(
    name = "paquete_distribuible",
    version = "0.01",
    descripción = "ejemplo de paquete distribuible con funciones de redonde y potencia",
    author = "angegon",
    author_email = "angegon@gmail.com",
    url = "https://github.com/angegon",
    packages = ["paquete", "paquete.redondeo_potencia"]
)