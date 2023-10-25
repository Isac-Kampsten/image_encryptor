#import libraries
from PIL import Image

#Message to be encoded in image

msg = "Rolle"

#Convert message to binary and put in an array

def convert_message(message):
    arr = []
    for i in message:
        arr.append((format(ord(f"{i}"), '8b')))
    return arr


#open image  
Input_Image = Image.open("./images/test_image.jpg")

#get pixel matrix from image
pixel_matrix = Input_Image.load()

#getting image height and width
height, width = Input_Image.size

def encrypt(pixel_matrix, height, width, input_image, message):
    letter = 0
    for x in range(width+1):
        for y in range(height+1):
            
            #declare an array of placeholders to hold the values of the changed pixel values
            new_pixels = [[0,0,0],[0,0,0],[0,0,0]]

            #select first three pixels
            if (x+2) < width+1: #To make sure we don't go outside the array
                pixel1 = pixel_matrix[x,y]
                pixel2 = pixel_matrix[(x+1),y]
                pixel3 = pixel_matrix[(x+2),y]






                

            
print(encrypt(pixel_matrix, height, width, Input_Image, convert_message(msg)))