import numpy as np
import cv2
import math
  
image = cv2.imread("Assets/InputImage.bmp");
w, h = image.shape[:2];  
xNew = int(w * 512/ 220);
yNew = int(h * 512 / 260);
  
height, width = image.shape[:2]

newImage = np.zeros([512, 512,3])

xScale = float(width - 1) / (512 - 1)
yScale = float(height - 1) / (512 - 1)

for i in range(511):
    for j in range(511):

        x_l, y_l = math.floor(xScale * (j+1)), math.floor(yScale * (i+1))
        x_h, y_h = math.ceil(xScale * (j+1)), math.ceil(yScale * (i+1))

        x_weight = (xScale * (j+1)) - x_l
        y_weight = (yScale * (i+1)) - y_l
 
        a = image[y_l, x_l]
        b = image[y_l, x_h]
        c = image[y_h, x_l]
        d = image[y_h, x_h]

        newImage[i+1,j+1]  = a * (1 - x_weight) * (1 - y_weight) + b * (x_weight) * (1 - y_weight) + c * (y_weight) * (1 - x_weight) + d * (x_weight) * (y_weight
        )
       
cv2.imwrite('Output/Im_BI.jpg', newImage)       