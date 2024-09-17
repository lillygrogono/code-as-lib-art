##### part 3
# import sys

# data = [ 643, 452, 230, 219, 962, 532 ]

#check if the user did not enter an argument
# if len(sys.argv) < 2:
#     print("You forgot to type an argument")
#     exit()

# index = int(sys.argv[1])

# # check if the user entered an argument that is too large
# if index >= len(data):
#     print("You typed a number that's too large")
#     exit()

# print( data[index] )


import sys
from PIL import Image

img = Image.open( sys.argv[1] )

print("You typed the filename: " + sys.argv[1] )
print("This is a " + img.format)
print(img.format_description)
print("Size: " + str(img.size) )