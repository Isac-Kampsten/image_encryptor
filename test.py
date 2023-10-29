#import libraries
from PIL import Image

#Message to be encoded in image

msg = "Rolle"

#Convert message to binary and put in an array


#open image  
Input_Image = Image.open("./images/sol.png")

#get pixel matrix from image
pixel_matrix = Input_Image.load()

#getting image height and width
height, width = Input_Image.size


#loop through image without going outisde boundries

print(f"image height:{height}, image width:{width}")

for i in range(height):
    for j in range(width):
        print(pixel_matrix[i,j])
        print(i,j)

print(width + height)
            




                

            
