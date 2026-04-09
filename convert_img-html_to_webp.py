

import os
import re

BASE_FOLDER = "."

def convert_html(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original = content

        # reemplazos seguros SOLO en rutas de imagen
        content = re.sub(r'(\.jpg|\.jpeg|\.png)', '.webp', content, flags=re.IGNORECASE)

        if content != original:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated: {file_path}")
        else:
            print(f"No changes: {file_path}")

    except Exception as e:
        print(f"Error in {file_path}: {e}")


def walk():
    for root, dirs, files in os.walk(BASE_FOLDER):
        for file in files:
            if file.endswith(".html"):
                convert_html(os.path.join(root, file))


if __name__ == "__main__":
    print("Starting HTML update to WebP...")
    walk()
    print("Done.")