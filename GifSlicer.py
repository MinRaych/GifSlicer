import os
from PIL import Image, ImageSequence
if not os.path.exists("sliced"): # if directory "sliced" doesn't exist
    os.mkdir("sliced") # create directory "sliced"

name = "name" # replace "name" with the name of the image
image = Image.open(name + '.gif')
i = 0
for frame in ImageSequence.Iterator(image):
    i += 1
    img = frame.resize((512, 512)) # size of gif (x, y)
    img.save("sliced\\" + name + "_" + str(i) + ".png")