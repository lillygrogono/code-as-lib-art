import sys
from PIL import Image

if len(sys.argv) != 3:
    print("Usage: python script.py <image1> <image2>")
    sys.exit(1)

try:
    # opens first image
    img1 = Image.open(sys.argv[1])

    # opens second image
    img2 = Image.open(sys.argv[2])

    # makes sure both images have the same size before blending
    if img1.size != img2.size:
        print("Error: Both images must be the same size to blend.")
        sys.exit(1)

    # blending the two images with equal transparency (0.5)
    blended_img = Image.blend(img1, img2, 0.5)

    blended_img.save("blended.jpg")
    print("Blended image saved as: blended.jpg")

# error messages

except FileNotFoundError:
    print(f"Error: One of the files {sys.argv[1]} or {sys.argv[2]} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
