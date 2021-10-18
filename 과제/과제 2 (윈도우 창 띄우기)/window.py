# 라이브러리 임포트
import numpy as np
import cv2

# 행렬 2개 생성
mat1 = np.full((200, 300), 100, np.uint8)
mat2 = np.full((200, 300), 100, np.uint8)

# 타이틀 설정
title1, title2 = 'win mode1', 'win mode2'

# 윈도우 생성
cv2.namedWindow(title1)
cv2.namedWindow(title2)

# 윈도우 위치 지정
cv2.moveWindow(title1, 0, 0)
cv2.moveWindow(title2, 300, 200)

# 행렬을 영상으로 표시
cv2.imshow(title1, mat1)
cv2.imshow(title2, mat2)

# 대기
cv2.waitKey(0)
cv2.destroyAllWindows()
