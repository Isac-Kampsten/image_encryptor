#Import libraries
from PIL import Image

#Choose a message that are to be encoded into the image
message = "banan"

#Create function that converts a string to binary equivalent

def stringToBinary(message):
    string = ""
    for i in message:
        string += (format(ord(f"{i}"), '08b'))
    return string

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
        


# Print the original pixels for debugging
#print("Original Pixels:")
#for pixel in chosen_pixels:
   # print(pixel)

# Loop through chosen pixels in sets of three and modify the RGB values
binary_message = stringToBinary(message)
message_index = 0

print(chosen_pixels)

for i in range(0, len(chosen_pixels), 3):
    set_of_pixels = []
    for j in range(3):
        pixel = chosen_pixels[i + j]
        set_of_pixels.append(pixel)
    #get all rgb values for the set of pixels



        





        



# Print the modified pixels for debugging
#print("\nModified Pixels:")
#for pixel in chosen_pixels:
   # print(pixel)

#print (binary_message)