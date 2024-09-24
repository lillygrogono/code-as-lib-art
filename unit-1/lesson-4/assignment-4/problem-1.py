# import sys
# from PIL import Image

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400, 400))

# # Loop through each pixel
# for y in range(400):
#     for x in range(400):
#         # Create pink stripes for every 40 pixels
#         if y % 40 < 20:
#             r, g, b = 255, 163, 191  # Light pink color
#         else:
#             r, g, b = 146, 173, 120  # Green color

#         # Set the pixel color
#         pixel = (r, g, b)
#         img.putpixel((x, y), pixel)

# # Save the image with the filename from the command line argument
# img.save(sys.argv[1])

import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# new 400x400 image (has to be in RGBA to use alpha composite)
img = Image.new("RGBA", (400, 400))

# loop through each pixel
for y in range(400):
    for x in range(400):
        # horizontal stripes (alternating pink and green every 20 pixels)
        if y % 40 < 20:
            r, g, b = 255, 172, 215  
        else:
            r, g, b = 125, 197, 120  

        # set the pixel color
        pixel = (r, g, b)
        img.putpixel((x, y), pixel)

# create a separate image for the blue stripes
blue_stripes = Image.new("RGBA", (600, 600), (0, 0, 0, 0))  # transparent background

# add vertical blue stripes
for y in range(400):
    for x in range(400):
        # add blue stripes every 40 pixels
        if x % 40 < 20:
            r, g, b, a = 97, 109, 237, 150  
            blue_stripes.putpixel((x, y), (r, g, b, a))

# blend the blue stripes onto the background
img = Image.alpha_composite(img, blue_stripes)

img.save(sys.argv[1])

