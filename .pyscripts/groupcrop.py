import os
from PIL import Image

folder = os.path.dirname(os.path.abspath(__file__))

for name in os.listdir(folder):
    if not name.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    path = os.path.join(folder, name)
    img = Image.open(path)
    w, h = img.size

    left = 130
    right = w - 130
    top = 70
    bottom = h - 100

    cropped = img.crop((left, top, right, bottom))
    cropped.save(path)
