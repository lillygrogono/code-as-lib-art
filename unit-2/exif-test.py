from os import listdir, path
from PIL import Image, ExifTags

files = listdir("images")
img = Image.open(path.join("images", "0.jpg"))
exifData = img.getexif()

print(exifData)
for key in img.getexif().keys():
    print(key, ExifTags.TAGS[key])

else:
        print("No EXIF data found.")

# PART TWO:
# I added this error handling at the bottom because the first photo I tried I got off the internet and it had no exif data... so then I emailed myself a photo from my camera roll and got exif data back!