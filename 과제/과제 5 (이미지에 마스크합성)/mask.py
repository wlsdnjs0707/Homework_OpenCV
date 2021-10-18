import numpy as np
import cv2

# 이미지 불러오기
image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)
# 사이즈가 같은 검은색 행렬 생성
black = np.zeros((360, 480, 3), np.uint8)

# 타원모양 그리기 (두께 = -1)
cv2.ellipse(black, (180, 180), (50, 80), 0, 360, 0, (255, 255, 255), -1)

# 이미지 비트연산 and
dst = cv2.bitwise_and(image, black)

cv2.imshow('dst', dst)
cv2.waitKey(0)
