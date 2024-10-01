import os
import random
from PIL import Image

# Define paths to the folders containing images
foreground_folder = "foreground"
middleground_folder = "middleground"
sky_folder = "sky"

def select_random_image(folder, prefix):
    """Randomly select an image from the specified folder with a given prefix."""
    # List all files in the folder for debugging
    all_files = os.listdir(folder)
    print(f"Files in {folder}: {all_files}")
    
    # Filter files by prefix and file type (.jpg instead of .png)
    files = [f for f in all_files if f.startswith(prefix) and f.endswith(('.png', '.jpg'))]
    
    # Print the filtered list of files
    print(f"Filtered files with prefix '{prefix}' in {folder}: {files}")
    
    if not files:
        raise FileNotFoundError(f"No images found with prefix '{prefix}' in {folder}")
    
    return os.path.join(folder, random.choice(files))

def create_random_gif(num_frames=10):
    """Create a GIF by randomly pulling images from each folder and overlaying them."""
    frames = []
    
    for _ in range(num_frames):
        # Randomly select one image from each folder
        sky_img_path = select_random_image(sky_folder, "sky_image")
        middleground_img_path = select_random_image(middleground_folder, "middleground_image")
        foreground_img_path = select_random_image(foreground_folder, "foreground_image")
        
        # Load the images
        sky_img = Image.open(sky_img_path).convert("RGBA")
        middleground_img = Image.open(middleground_img_path).convert("RGBA")
        foreground_img = Image.open(foreground_img_path).convert("RGBA")

     # resizing the images so I can customize the look
        sky_img = sky_img.resize((800, 800))  
        middleground_img = middleground_img.resize((800, 800)) 
        foreground_img = foreground_img.resize((400, 400))  

        
        # Create a new image to overlay the layers
        combined_image = Image.new("RGBA", (800, 800))
        
        # Paste the sky, middleground, and foreground in that order
        combined_image.paste(sky_img, (0, 0), sky_img)
        combined_image.paste(middleground_img, (0, 200), middleground_img)
        combined_image.paste(foreground_img, (200, 300), foreground_img)
        
        # Add the combined image as a frame to the GIF
        frames.append(combined_image)
    
    # Save the frames as a GIF
    frames[0].save("random_gif2.gif", save_all=True, append_images=frames[1:], duration=400, loop=0)
    print("GIF created and saved as random_gif.gif")

if __name__ == "__main__":
    create_random_gif()
