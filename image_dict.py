import os
from PIL import Image

dict = {}
index = 1
directory_new = './dataset/normal_resized/'
directory_new_pot = './dataset/potholes_resized/'
for filename in os.listdir(directory_new):
    image = Image.open(directory_new + filename)
    dict[index] = [image, 0]
    index += 1

for filename in os.listdir(directory_new_pot):
    image = Image.open(directory_new_pot + filename)
    dict[index] = [image, 1]
    index += 1

print(dict)
