import os
os.environ['path'] += r';D:\Dev\qlik-cloud-icons\libvips\bin'
import pyvips
import shutil

# Convert the SVG to a PNG of size
def svg_to_png(svg_path, png_path, size):
    image = pyvips.Image.thumbnail(svg_path, size, height=10000000)
    image.write_to_file(png_path)

# Size variants to create
sizes = [16, 32, 64, 128, 256, 512]

# Get list of SVGs
items = os.listdir('./svg')

# Remove PNG folder if it exists
if os.path.isdir('./png'):
    shutil.rmtree('./png')

# Create PNG folder
os.makedirs('./png')

# For each size
for size in sizes:
    output_path = './png/%sx%s/' % (size, size)
    os.makedirs(output_path)
    print("Generating PNG %sx%s" % (size, size))

    # Convert the image
    for item in items:
        source_file = './svg/' + item
        target_file = output_path + item.replace('svg', 'png')
        svg_to_png(source_file, target_file, size)