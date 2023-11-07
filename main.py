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
print(pixels_needed)


