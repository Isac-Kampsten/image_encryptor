#import libraries
from PIL import Image

#open image  
Input_Image = Image.open("./images/test_image.jpg")

#get pixel matrix from image
pixel_matrix = Input_Image.load()

#getting image height and width
height, width = Input_Image.size

