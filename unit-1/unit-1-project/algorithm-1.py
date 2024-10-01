import os
import random
from PIL import Image

# Define paths to the folders containing images for each category
sky_folder = "sky"
middleground_folder = "middleground"
foreground_folder = "foreground"

# folder_path = folder to look in
# category = sky, middleground, or foreground
def select_random_image(folder_path, category):

    # os.listdir = lists out all of the files in the folder and filters by category 
    files = [f for f in os.listdir(folder_path) if f.startswith(category) and os.path.isfile(os.path.join(folder_path, f))]
    
    # If no files are found, error message 
    if not files:
        raise FileNotFoundError(f"No {category} images found in {folder_path}")

    # If there are files, it will randomly select one 
    return os.path.join(folder_path, random.choice(files))

def create_collage():
    # select images from their folders
    sky_image_path = select_random_image(sky_folder, "sky_")
    middleground_image_path = select_random_image(middleground_folder, "middleground_")
    foreground_image_path = select_random_image(foreground_folder, "foreground_")

    # open the images and convert to RGBA which is PNG compatible/ ensures the image has alpha transparency
    sky_img = Image.open(sky_image_path).convert("RGBA")
    middleground_img = Image.open(middleground_image_path).convert("RGBA")
    foreground_img = Image.open(foreground_image_path).convert("RGBA")

    # resizing the images so I can customize the look
    sky_img = sky_img.resize((800, 800))  
    middleground_img = middleground_img.resize((800, 800)) 
    foreground_img = foreground_img.resize((400, 400))  

    # created a base image that matches the size of the sky, w/ transparent background
    collage_image = Image.new('RGBA', sky_img.size, (0, 0, 0, 0))  

    # made the sky image the base
    collage_image.paste(sky_img, (0, 0), sky_img)

    # layered middle ground on top of the sky
    collage_image.paste(middleground_img, (0, 200), middleground_img)

    # lastly put the foreground on top of the middle ground and sky
    collage_image.paste(foreground_img, (200, 250), foreground_img)

    # Generates a random 4-digit number to create unique file names
    random_number = random.randint(1000, 9999) 
    filename = f"collage_output_{random_number}.png"

    # Save the collage with the unique filename
    collage_image.save(filename, "PNG")
    print(f"Collage created and saved as {filename}")

    # I had to research this last part because I didn't fully understand its' purpose, but from what I've read it allows you to be able to use this code directly in the terminal as well as import it to another python file without running the entire script

if __name__ == "__main__":
    create_collage()