import sys
from PIL import Image 

if len(sys.argv) != 5:
    exit("This program requires four arguments: the name of four image files to combine.")

# open all images
img1 = Image.open(sys.argv[1])
img2 = Image.open(sys.argv[2])
img3 = Image.open(sys.argv[3])
img4 = Image.open(sys.argv[4])

# resize the images
img1.thumbnail((400, 400))
img2.thumbnail((400, 400))
img3.thumbnail((100, 100))
img4.thumbnail((300, 300))

# convert images to RGBA for transparency handling
img3 = img3.convert("RGBA")
img4 = img4.convert("RGBA")

new_image = img1.convert("RGBA")  # use img4 as the base (no checkered transparency)

# set the transparency for the other images
img1.putalpha(255)
img2.putalpha(100)

# paste the images into the new image
new_image.paste(img1, (0, 0), img1)
new_image.alpha_composite(img2, (0, -250))
new_image.paste(img3, (130, 110), img3)  # paste with mask for transparency
new_image.paste(img4, (-60, -20), img4) 

new_image.save("image-4.png", format="PNG")
