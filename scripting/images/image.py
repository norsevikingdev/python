from PIL import Image, ImageFilter
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
img1_png = os.path.join(THIS_FOLDER, 'images\img1.png')

img1 = Image.open(img1_png)
# filtered_img1 = img1.filter(ImageFilter.GaussianBlur)
# filtered_img1.save("blured.png", "png")

# box = (100, 100, 400, 400)
# region = img1.crop(box)
# region.save("cropped.png", "png")
# filtered_img1 = img1.resize((300, 300))
# filtered_img1.save("resize.png", "png")

img1.thumbnail((400, 400))
img1.save("thumbnail.png")
