from PIL import Image
import numpy as np
import os

PATH = './Dataset_cleaned/train'
DST_EXTENSION = "jpg"

def extension_coverter(path, extension):
    extensions = []
    full_path = []
    print(f"Buscando archivos NO {extension.upper()}...")
    print("---------------------------------------------")
    for root, folder, files in os.walk(path):
        for f in files:
            if not f.endswith(".jpg"):
                full_path.append(os.path.join(root, f))
                extensions.append(f.split('.')[-1])

    print(f"Extensiones Detectadas: {np.unique(extensions)}")
    print("---------------------------------------------")
    print(f"Convirtiendo archivos a {extension.upper()}...")

    for file in full_path:
        #get original extension
        ext = os.path.split(file)[-1].split(".")[-1]

        #load image
        img = Image.open(file)
        img.save(file.replace(ext, extension))

        os.remove(file)
    print("---------------------------------------------")
    print("Conversión Completa.")

extension_coverter(PATH, DST_EXTENSION)

