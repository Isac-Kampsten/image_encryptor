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
    for y in range(height+1):
        for x in range(width+1):
            
            #declare an array of placeholders to hold the values of the changed pixel values
            new_pixels = [[0,0,0],[0,0,0],[0,0,0]]

            #select first three pixels
            if (x+2) < width: #To make sure we don't go outside the array
                pixel1 = pixel_matrix[x,y]
                pixel2 = pixel_matrix[(x+1),y]
                pixel3 = pixel_matrix[(x+2),y]
                arr = [pixel1,pixel2,pixel3]
              

                #loop through array with pixels and loop through the values of each pixel

                for pixel_index, pixel in enumerate(arr):
                    for rgb_index, rgb in enumerate(pixel):
                        #check if number should be even
                        if message[letter][rgb_index] == 0:
                            if pixel != 2 & rgb != 2: 
                                #make rgb value even
                                if rgb%2 != 0:
                                    rgb = rgb + 1
                            else:
                                #rgb should be odd
                                if rgb%2 == 0:
                                    rgb = rgb + 1
                        #after rgb value is changed, assign the new value to a new array with placeholders
                        new_pixels[pixel_index][rgb_index] = pixel





                

            
print(encrypt(pixel_matrix, height, width, Input_Image, convert_message(msg)))