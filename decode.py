from PIL import Image 

# Import an image from directory: 
input_image = Image.open("./encrypted_image.png") 

# Extracting pixel map: 
pixel_matrix = input_image.load() 

# Extracting the width and height 
# of the image: 
width, height = input_image.size 

# loop through image to see when message ends

#define functions

def binaryToString(binary_message):
  string = ""
  for i in range(0, len(binary_message), 8):
    byte = binary_message[i:i+8]
    string += chr(int(byte, 2))
  return string

blue_values = []

for y in range(height):  
	for x in range(width):  
		r,g,b, *rest = pixel_matrix[x,y]
		
        #select all the third blue values
		blue_values.append(b)

		
		
        
#print(blue_values)


#calculate how many pixels contain message data
letters = 0
for i in range(2,len(blue_values),3):
	if blue_values[i] % 2 == 0:
		letters += 1
	else:
		letters += 1
		break

print(" ")
print("letters:")
print(letters)
print(" ")
        
chosen_pixels = []
count = 0

for y in range(height):
    for x in range(width):
        if count < letters*3:
            chosen_pixels.append(pixel_matrix[x,y])
            count += 1
        


#loop through chosen pixels in sets of three

binary_message = ""
message_ended = False

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
          
        #if value is even add a zero to the string,else add a one
        if rgb_values[rgb_index] % 2 == 0:
            binary_message = binary_message + "0"
        else:
            binary_message = binary_message + "1"


print("Hidden message is:")  
print(binaryToString(binary_message))
print(" ")
    
    	
	

    
	
