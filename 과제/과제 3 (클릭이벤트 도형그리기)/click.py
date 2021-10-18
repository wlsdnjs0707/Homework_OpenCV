import numpy as np
import cv2


def onMouse(event, x, y, flags, param):
    global title

    # 마우스 왼쪽 버튼 클릭 시
    if event == cv2.EVENT_LBUTTONDOWN:
        # 클릭 좌표에서 30 X 30 크기의 사각형 그리기
        cv2.rectangle(image, (x, y), (x+30, y+30), (255, 0, 0))
        cv2.imshow(title, image)
    # 마우스 오른쪽 버튼 클릭 시
    elif event == cv2.EVENT_RBUTTONDOWN:
        # 클릭 좌표에서 반지름 20 화소의 원 그리기
        cv2.circle(image, (x, y), 20, (0, 0, 255))
        cv2.imshow(title, image)


# 3채널 정수형 행렬을 생성하고 흰색(255)로 채운다.
image = np.zeros((500, 500, 3), np.uint8)
image.fill(255)

title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
