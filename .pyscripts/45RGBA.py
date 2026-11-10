import os
from PIL import Image

# Set the number of colors in the palette
num_colors = 45

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# List of valid image extensions
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# Search for an image file in the directory
image_path = None
for filename in os.listdir(current_directory):
    if filename.lower().endswith(valid_extensions):
        image_path = os.path.join(current_directory, filename)
        break

if image_path is None:
    print(f"Error: No valid image file found in the directory '{current_directory}'.")
    exit(1)

# Load the image
image = Image.open(image_path)

# Convert the image to P mode to reduce colors to the specified palette size
image = image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)

# Save the new image with the reduced color palette
output_path = os.path.join(current_directory, 'output_image.png')
image.save(output_path)

print(f"Image saved with a palette of {num_colors} colors to {output_path}.")
