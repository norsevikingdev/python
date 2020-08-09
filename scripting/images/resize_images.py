from PIL import Image
import sys
import os

# grab first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not (os.path.exists(output_folder)):
    os.mkdir(output_folder)

for item in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{item}")
    img.thumbnail((400, 400))
    clean_name = os.path.splitext(item)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")

# run : python resize_images.py images_file\ new\
