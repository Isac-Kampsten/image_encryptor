#Import libraries
from PIL import Image

#Choose a message that are to be encoded into the image
message = "rolle"

#Create function that converts a string to binary equivalent

def stringToBinary(message):
    string = ""
    for i in message:
        string += (format(ord(f"{i}"), '08b'))
    return string

#open image  
Input_Image = Image.open("./images/test_image.jpg")

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
        


#Print the original pixels for debugging
#print("Original Pixels:")
#for pixel in chosen_pixels:
    #print(pixel)

# Loop through chosen pixels in sets of three and modify the RGB values
binary_message = stringToBinary(message)
message_index = 0
new_pixels = []



for i in range(0, len(chosen_pixels), 3):
    set_of_pixels = []

    for j in range(3):
        pixel = chosen_pixels[i + j]
        set_of_pixels.append(pixel)

    #get all rgb values for the set of pixels
    r1, r2, r3 = set_of_pixels[0][0], set_of_pixels[1][0], set_of_pixels[2][0]
    g1, g2, g3 = set_of_pixels[0][1], set_of_pixels[1][1], set_of_pixels[2][1]
    b1, b2, b3 = set_of_pixels[0][2], set_of_pixels[1][2], set_of_pixels[2][2]



    rgb_values = [r1, g1, b1, r2, g2, b2, r3, g3, b3]

    #modify every value accordingly except the last blue value, since it will be used to determine if the message continues or not
    
    for rgb_index in range(0,8):

        #check if the current bit in the binary message is a 0 or a 1

        if binary_message[message_index] == "0":
            #make the current rgb value even

            #check if rgb value already is even, if it is do nothing else check if it is 255 or 0, then choose wheter to subract one or add one

            if rgb_values[rgb_index] % 2 == 0:
                rgb_values[rgb_index] = rgb_values[rgb_index]
                
            else:
                rgb_values[rgb_index] = (rgb_values[rgb_index] - 1)
                

        if binary_message[message_index] == "1":
            #make the current rgb value odd

            #check if rgb value already is odd, if it is do nothing, else add 1
            if rgb_values[rgb_index] % 2 == 1:
                rgb_values[rgb_index] = rgb_values[rgb_index]
                
            else:
                rgb_values[rgb_index] = (rgb_values[rgb_index] + 1)
        message_index += 1
    
    #check if we're on the last charachter in the message, if so, make the value odd, else make it even

    if message_index == len(binary_message):
        #make b3 odd 
        
        #if it's already odd do nothing

        if rgb_values[8] % 2 == 1:
            rgb_values[8] = rgb_values[8]
        else:
            rgb_values[8] = (rgb_values[8] + 1)
    else:

        #make b3 even

        #check if b3 already is even

        if rgb_values[8] % 2 == 0: 
            rgb_values[8] = rgb_values[8]
        else:
            rgb_values[8] = (rgb_values[8] - 1)

    #append modified rgb_values to new_pixels array
    new_pixels.append((rgb_values[0],rgb_values[1],rgb_values[2],255))
    new_pixels.append((rgb_values[3],rgb_values[4],rgb_values[5],255))
    new_pixels.append((rgb_values[6],rgb_values[7],rgb_values[8],255))



    
#print new_pixels after modification

#print("new_pixels:")
#for i in new_pixels:
    #print(i)
         
inserted_pixels_index = 0

for y in range(height):
    for x in range(width):
        if inserted_pixels_index < len(new_pixels):
            pixel_matrix[x,y] = new_pixels[inserted_pixels_index]
            inserted_pixels_index += 1

Input_Image.save("encrypted_image.png", format="png")