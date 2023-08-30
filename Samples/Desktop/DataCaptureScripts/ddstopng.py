import os
from wand import image

def convert_dds_to_png(dds_file):
    with image.Image(filename=dds_file) as img:
        img.compression = "no"
        img.save(filename=dds_file.replace('.dds', '.png'))

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith('.dds'):
            output_file = os.path.join(root, file)
            print(output_file)
            convert_dds_to_png(output_file)