import cv2
import numpy as np

O = cv2.imread("../lena.bmp")
G0 = O
G1 = cv2.pyrDown(G0)
L0 = G0 - cv2.pyrUp(G1)
RO = L0 + cv2.pyrUp(G1)

print("O.shape=", O.shape)
print("RO.shape=", RO.shape)
result = O - RO
result = abs(result)
print("原始图像O与恢复图像RO差值的绝对值和：", np.sum(result))
