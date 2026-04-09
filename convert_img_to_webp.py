


import os
from PIL import Image

# carpeta raíz imágenes
BASE_FOLDER = "../static/img"

# extensions a convertir
VALID_EXTENSIONS = (".png", ".jpg", ".jpeg")

# calidad webp
QUALITY = 80

def convert_image(path):
    try:
        img = Image.open(path)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # nombre nuevo
        base = os.path.splitext(path)[0]
        new_path = base + ".webp"

        # evitar reconvertir si ya existe
        if os.path.exists(new_path):
            print(f"Skip (exists): {new_path}")
            return

        img.save(new_path, "webp", quality=QUALITY, optimize=True)

        print(f"Converted: {path} -> {new_path}")

    except Exception as e:
        print(f"Error with {path}: {e}")


def walk_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(VALID_EXTENSIONS):
                full_path = os.path.join(root, file)
                convert_image(full_path)


if __name__ == "__main__":
    print("Starting WebP conversion...")
    walk_folder(BASE_FOLDER)
    print("Done.")

    print("BASE_FOLDER exists?", os.path.exists(BASE_FOLDER))
    print("ABS PATH:", os.path.abspath(BASE_FOLDER))    