from typing import final
import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "rick.jpg"

def togray(rgb):
    return np.dot(rgb[...,:3], [0.2989,0.5870,0.1140])

def dodge(front,back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back==255] = 255
    return final_sketch.astype('uint8')


image = imageio.imread(img)    #read the given image
gray = togray(image)          #convert to black and white

i = 255-gray

# convert to blurry
blur = scipy.ndimage.filters.gaussian_filter(i,sigma=15)

r = dodge(blur,gray) #convert image to sketch

cv2.imwrite('sketch.png', r)