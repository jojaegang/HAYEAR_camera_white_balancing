import time
import os
from PIL import Image
import numpy as np
from PIL import ImageFilter

file_list = os.listdir()
file_list_jpg = [file for file in file_list if file.endswith('.jpg') and not file.endswith('_wb.jpg')]
print("file_list_jpg: {}".format(file_list_jpg))
file_list_png = [file for file in file_list if file.endswith('.png') and not file.endswith('_wb.png') and not file.endswith('ref.png')]
print("file_list_png: {}".format(file_list_png))

ref_img = Image.open('trans_ref.png')
# ref_img_arr = np.array(ref_img.filter(ImageFilter.GaussianBlur(100)))
ref_img_arr = np.array(ref_img)

# White balancing (R, G, B) should be less than 1.0


for file in file_list_png or file_list_jpg:
    img = Image.open(file)
    arr = np.array(img)
    arr = np.round(arr/ref_img_arr*150)
    arr[arr > 255] = 255
    img = Image.fromarray(arr.astype(np.uint8))
    # save image with different name by adding "_wb"
    img.save(file.split('.')[0] + '_wb.png')

print('White banlancing done.')
while True:
    n = input('Please press Enter to exit : ')
    if n == '':
        break