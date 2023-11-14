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

new_pixels = []
letter_count = 0

for index, pixel in enumerate(chosen_pixels):
    if index <= pixels_needed-3:
        pixel1, pixel2, pixel3 = chosen_pixels[index], chosen_pixels[index+1], chosen_pixels[index+2]
        setOfPixels = [pixel1,pixel2,pixel3]

        for binary_letter_index, binary_number in enumerate(stringToBinary(message)[letter_count]):
            if binary_letter_index <= 2:
                #change values of first pixel
                if binary_number == 0:
                    #make pixel value even
                    if setOfPixels[0][binary_letter_index]%2 != 0:
                        setOfPixels[0][binary_letter_index] -= 1
                else:
                    #binary number is a 1 and we want to make pixel value uneven
                    if setOfPixels[0][binary_letter_index]%2 == 0:
                        setOfPixels[0][binary_letter_index] -= 1
                    
                        
                
 
                    
                        

