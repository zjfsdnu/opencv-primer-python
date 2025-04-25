import cv2
import numpy as np

O = cv2.imread("../lena.bmp")

G0 = O
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)

L0 = G0 - cv2.pyrUp(G1)
L1 = G1 - cv2.pyrUp(G2)
L2 = G2 - cv2.pyrUp(G3)

RG0 = L0 + cv2.pyrUp(G1)
print("G0.shape=", G0.shape)
print("RG0.shape=", RG0.shape)
result = abs(G0 - RG0)
print("原始图像G0与恢复图像RG0差值的绝对值和：", np.sum(result))

RG1 = L1 + cv2.pyrUp(G2)
print("G1.shape=", G1.shape)
print("RG1.shape=", RG1.shape)
result = abs(G1 - RG1)
print("原始图像G1与恢复图像RG1差值的绝对值和：", np.sum(result))

RG2 = L2 + cv2.pyrUp(G3)
print("G2.shape=", G2.shape)
print("RG2.shape=", RG2.shape)
result = abs(G2 - RG2)
print("原始图像G2与恢复图像RG2差值的绝对值和：", np.sum(result))
