import cv2
import numpy as np

# 좌표가 범위안에 있나
def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

# 영상 평행이동
def translate(img, pt):
    global pts
    dst = np.zeros(image.shape, image.dtype)  # 목적영상 생성
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            x, y = np.subtract((j, i), pt)
            if contain((y, x), image.shape):
                dst[i, j] = image[y, x]
    cv2.line(dst, pts[1], pts[0], (0, 0, 255), 3)  # 직선 생성
    return dst

def onMouse(event, x, y, flags, param):
    global image, pts
    # 마우스 좌표 저장
    if event == cv2.EVENT_LBUTTONDOWN:
        pts[0] = [x, y]
    if event == cv2.EVENT_LBUTTONUP:
        pts[1] = [x, y]
        pt = np.subtract(pts[1], pts[0])  # 두 좌표 차분 계산
        image = translate(image, pt)  # 평행이동 함수 호출
        cv2.imshow("image", image)

pts = [[0, 0], [0, 0]]
image = cv2.imread("images/10.jpg", cv2.IMREAD_COLOR)
cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()
