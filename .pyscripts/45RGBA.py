import os
from PIL import Image

# Set the number of colours in the palette
num_colors = 45

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create output folder
output_directory = os.path.join(current_directory, "output")
os.makedirs(output_directory, exist_ok=True)

# Valid image extensions
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# Process all images in the directory
for filename in os.listdir(current_directory):
    if filename.lower().endswith(valid_extensions):

        image_path = os.path.join(current_directory, filename)

        try:
            # Load image
            image = Image.open(image_path)

            # Convert to P mode with reduced colour palette
            image = image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)

            # Preserve original filename, but save as PNG
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_directory, output_filename)

            # Save converted image
            image.save(output_path)

            print(f"Converted: {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"\nFinished! Converted images saved in: {output_directory}")
