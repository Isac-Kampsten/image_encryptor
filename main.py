#Import libraries
from PIL import Image

#Choose a message that are to be encoded into the image
message = "banan"

#Create function that converts a string to binary equivalent

def stringToBinary(message):
    arr = []
    for i in message:
        arr.append((format(ord(f"{i}"), '08b')))
    return arr

#open image  
Input_Image = Image.open("./images/sol.png")

#get pixel matrix from image
pixel_matrix = Input_Image.load()

#getting image height and width
height, width = Input_Image.size

#calculate amount of pixels needed
pixels_needed = len(message) * 3



#Choose amount of pixels needed from the image and put them in an array

count = 0
chosen_pixels = []

for y in range(height):
    for x in range(width):
        if count < pixels_needed:
            chosen_pixels.append(pixel_matrix[x,y])
            count += 1
        


#loop through chosen pixels and change first three pixels according to letter

