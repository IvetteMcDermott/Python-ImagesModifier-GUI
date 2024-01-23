from rembg import remove
from PIL import Image

old_image = "us-kerry.jpg"
output_image = "rmv-us-kerry.png"

orig_img = Image.open(old_image)
new_img = remove(orig_img)

new_img.save(output_image)