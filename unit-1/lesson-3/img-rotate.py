import sys
from PIL import Image

if len(sys.argv) != 3:
    print("Usage: python script.py <image_path> <rotation_degrees>")
    sys.exit(1)

try:
    img = Image.open(sys.argv[1])
    rotated_img = img.rotate(int(sys.argv[2]))
    rotated_img.save("rotated-" + sys.argv[1])
    print(f"Rotated image saved as: rotated-{sys.argv[1]}")
except FileNotFoundError:
    print(f"Error: File {sys.argv[1]} not found.")
except ValueError:
    print("Error: Rotation degrees must be an integer.")
except Exception as e:
    print(f"An error occurred: {e}")


