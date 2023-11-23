from PIL import Image 

# Import an image from directory: 
input_image = Image.open("./encrypted_image.png") 

# Extracting pixel map: 
pixel_matrix = input_image.load() 

# Extracting the width and height 
# of the image: 
width, height = input_image.size 
print("hej")
# loop through image to see when message ends
print("hej igen")

blue_values = []

for y in range(1):  
	for x in range(0,20):  
		r,g,b, _ = pixel_matrix[x,y]
		
        #select all the third blue values
		blue_values.append(b)
		
        
print(blue_values)
        
        