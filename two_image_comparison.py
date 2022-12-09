from PIL import Image

#This program uses the Python Image Library (PIL) to open the two images and get their dimensions
#It then loops through each pixel in the images and compares them 
#If any of the pixels are different, it prints a message indicating the location of the mismatch

# Open the two images
img1 = Image.open("image1.jpg")
img2 = Image.open("image2.jpg")

# Get the width and height of the images
width1, height1 = img1.size
width2, height2 = img2.size

# Make sure the images have the same dimensions
if width1 != width2 or height1 != height2:
    print("Error: Images must have the same dimensions")
    exit()

# Loop through each pixel and compare the two images
for x in range(width1):
    for y in range(height1):
        pix1 = img1.getpixel((x, y))
        pix2 = img2.getpixel((x, y))

        # Check if the pixels are the same
        if pix1 != pix2:
            print("Pixel at position ({},{}) does not match".format(x, y))
