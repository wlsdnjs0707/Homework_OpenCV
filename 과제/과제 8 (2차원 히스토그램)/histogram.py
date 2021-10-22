import numpy as np
import cv2

# 색상배경
hsvmap = np.zeros((180, 256, 3), np.uint8)
h, s = np.indices(hsvmap.shape[:2])
hsvmap[:, :, 0] = h
hsvmap[:, :, 1] = s
hsvmap[:, :, 2] = 255
hsvmap = cv2.cvtColor(hsvmap, cv2.COLOR_HSV2BGR)

# 읽어서 HSV 컬러공간으로 변환
image = cv2.imread("images/10.jpg")
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 히스토그램
hist = cv2.calcHist([hsv_img], [0, 1], None, [180, 256], [0, 180, 0, 256])

# 색상입히기
hist = np.clip(hist * 0.005 * 10, 0, 1)
hist = hsvmap*hist[:, :, np.newaxis] / 256.0

cv2.imshow("hist", hist)
cv2.waitKey(0)
cv2.destroyAllWindows()
