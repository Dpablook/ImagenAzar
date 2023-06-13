import os
import random
import subprocess
import time

def open_in_brave(image_path):
    subprocess.run(["brave", image_path])

def open_directory_in_file_manager(directory_path):
    subprocess.run(["xdg-open", directory_path])

# Directorio principal
directorio_principal = "/media/pablo/f13b3bca-07cf-4563-87b8-056459d3e032/lubuntupablo/Documentos/Mangas"

# Obtener una lista de todos los archivos con extensión .png y sus directorios correspondientes
archivos_png = []
for directorio_raiz, directorios, archivos in os.walk(directorio_principal):
    # Excluir directorios con el nombre "instagram"
    """if "instagram" in directorios:
        directorios.remove("instagram")
        continue """

    for archivo in archivos:
        if archivo.lower().endswith(".png"):
            ruta_archivo = os.path.join(directorio_raiz, archivo)
            archivos_png.append((ruta_archivo, directorio_raiz))

# Seleccionar una imagen al azar
imagen_aleatoria, directorio_imagen = random.choice(archivos_png)

# Imprimir la ruta del directorio
print("Ruta del directorio:", directorio_imagen)

# Abrir la imagen en el navegador Brave
open_in_brave(imagen_aleatoria)

# Esperar 3 segundos
time.sleep(3)

# Abrir el directorio en el explorador de archivos
open_directory_in_file_manager(directorio_imagen)







