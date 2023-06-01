import cv2
originalImage = cv2.imread("Assets/OriginalImage.bmp")
NNI_Image = cv2.imread("Output/Im_NNI.jpg")
BL_Image = cv2.imread("Output/Im_BI.jpg")

NNI_MSE, BI_MSE = 0,0

for i in range(512):
    for j in range(512):
        NNI_MSE += (originalImage[i,j] - NNI_Image[i,j])**2
NNI_MSE =NNI_MSE * 1/(512*512)
print(NNI_MSE)

for i in range(512):
    for j in range(512):
        BI_MSE += (originalImage[i,j] - BL_Image[i,j])**2
BI_MSE = BI_MSE * 1/(512*512)
print(BI_MSE)

for k in range(1):
    
        if (BI_MSE[k] < NNI_MSE[k]):
           print("Bilinear Interpolation is better")
        else:
           print("Nearest Neighbor Interpolation is better")