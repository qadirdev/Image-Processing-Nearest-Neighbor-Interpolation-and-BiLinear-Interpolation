import numpy as np
import cv2
  
image = cv2.imread("Assets/InputImage.bmp");
w, h = image.shape[:2];

xNew = int(w * 512/ 220);
yNew = int(h * 512 / 260);
  
xScale = xNew/(w-1);
yScale = yNew/(h-1);
  
newImage = np.zeros([xNew, yNew, 3]);
  
for i in range(xNew-1):
   for j in range(yNew-1):
       newImage[i + 1, j + 1]= image[1 + int(i / xScale),1 + int(j / yScale)]

cv2.imwrite('Output/Im_NNI.jpg', newImage)