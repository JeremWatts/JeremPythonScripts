
from pathlib import Path
from PIL import Image
import shutil

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "output"

converted = 0
skipped = 0
errors = 0

for path in SCRIPT_DIR.rglob("*"):
    if not path.is_file() or path.suffix.lower() != ".png":
        continue

    # Ignore the output folder to prevent recursive processing
    if OUTPUT_DIR in path.parents:
        continue

    relative_path = path.relative_to(SCRIPT_DIR)
    destination = OUTPUT_DIR / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)

    try:
        with Image.open(path) as image:
            image.load()

            # Detect alpha transparency and indexed PNG transparency
            has_transparency = (
                "A" in image.getbands()
                and image.getchannel("A").getextrema()[0] < 255
            ) or ("transparency" in image.info)

            if has_transparency:
                shutil.copy2(path, destination)
                skipped += 1
                print(f"COPIED (transparency): {relative_path}")
                continue

            # Convert to 16 colours maximum (4-bit indexed PNG)
            image = image.convert("RGB").quantize(colors=16)
            image.save(destination, format="PNG", bits=4)

            converted += 1
            print(f"CONVERTED: {relative_path}")

    except Exception as e:
        errors += 1
        print(f"ERROR: {relative_path} — {e}")

print("\nFinished.")
print(f"Converted: {converted}")
print(f"Copied unchanged (transparency): {skipped}")
print(f"Errors: {errors}")
print(f"Output folder: {OUTPUT_DIR}")
