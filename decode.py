from PIL import Image 

# Import an image from directory: 
input_image = Image.open("./encrypted_image.png") 

# Extracting pixel map: 
pixel_matrix = input_image.load() 

# Extracting the width and height 
# of the image: 
width, height = input_image.size 

# loop through image to see when message ends


blue_values = []

for y in range(height):  
	for x in range(width):  
		r,g,b, _ = pixel_matrix[x,y]
		
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
	
print("letters:")
print(letters)
        