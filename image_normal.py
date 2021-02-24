import os
from PIL import Image

directory = './dataset/normal/'
directory_new = './dataset/normal_resized/'
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        print(directory + filename)
        print('file found')
        image = Image.open(directory + filename).convert('RGB')
        print(f' image is {image}')
        print(image.archive)
        print(image.format)
        print(image.mode)
        new_image = image.resize((200, 200))
        new_image.save(directory_new + filename)
        continue
    else:
        continue

