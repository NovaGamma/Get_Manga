import os
from PIL import Image

relative_path = "trample_on_the_river_of_immortality"
path = 'static/' + relative_path

image_list = [[image,image.size] for image in [Image.open(f"{path}/{img}") for img in os.listdir(path)]]
print(image_list)
sum_x = 0
for image in image_list:
    sum_x += image[1][0]
average = int(sum_x/len(image_list))
print(average)
input()
for image in image_list:
    ratio = image[1][0]/average
    new_size = (average,int(image[1][1]*ratio))
    image[0].resize(new_size)
    image[0].save(image[0].filename)
