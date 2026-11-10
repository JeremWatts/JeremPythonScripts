from pathlib import Path

import numpy as np
from PIL import Image, ImageChops

# Settings
OPAQUE_RADIUS = 0.20  # Fully opaque centre radius
FEATHER_WIDTH = 0.30  # Distance over which transparency increases

OUTPUT_FOLDER = "radial_erased"


def apply_radial_erase(image):
    image = image.convert("RGBA")
    width, height = image.size

    # Distance from image centre.
    y, x = np.ogrid[:height, :width]
    center_x = width / 2
    center_y = height / 2

    distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

    # Scale settings relative to the smaller image dimension.
    reference_size = min(width, height)
    opaque_radius = OPAQUE_RADIUS * reference_size
    feather_width = FEATHER_WIDTH * reference_size

    # Calculate outward transparency gradient.
    t = np.clip(
        (distance - opaque_radius) / feather_width,
        0.0,
        1.0
    )

    # Smooth transition from opaque to transparent.
    smooth = t * t * (3.0 - 2.0 * t)

    # Invert: opaque centre, transparent outside.
    alpha_array = ((1.0 - smooth) * 255).astype(np.uint8)

    mask = Image.fromarray(alpha_array)

    # Preserve existing transparency.
    original_alpha = image.getchannel("A")
    image.putalpha(ImageChops.multiply(original_alpha, mask))

    return image


def main():
    folder = Path(__file__).parent
    output_folder = folder / OUTPUT_FOLDER
    output_folder.mkdir(exist_ok=True)

    png_files = [
        file for file in folder.iterdir()
        if file.is_file() and file.suffix.lower() == ".png"
    ]

    for file in png_files:
        try:
            with Image.open(file) as image:
                result = apply_radial_erase(image)
                result.save(output_folder / file.name, "PNG")
                print(f"Processed: {file.name}")

        except Exception as error:
            print(f"Failed: {file.name} — {error}")

    print(f"\nFinished processing {len(png_files)} images.")


if __name__ == "__main__":
    main()
