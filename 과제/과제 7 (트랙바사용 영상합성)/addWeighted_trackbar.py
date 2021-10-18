import numpy as np
import cv2


# 트랙바 이벤트
def onchange(value):
    global image, image1, image2, image3

    # image1_rate = 이미지1의 비율 (100으로 나눠줌)
    # image2_rate = 이미지2의 비율 (100으로 나눠줌)
    image1_rate = cv2.getTrackbarPos('image1', 'dst')/100
    image2_rate = cv2.getTrackbarPos('image2', 'dst')/100

    # image3은 이미지1의 비율과 이미지2의 비율에 따라 addWeighted 함수 사용
    image3 = cv2.addWeighted(image1, image1_rate, image2, image2_rate, 0)
    image = np.concatenate((image1, image3, image2), axis=1)

    cv2.imshow(title, image)


# image3 = image1과 image2 합성한 이미지
# image = image1, image3, image2 순으로 한 윈도우에 출력하기 위해 합친 이미지
image1 = cv2.imread("images/add1.jpg")
image2 = cv2.imread("images/add2.jpg")
image3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
image = np.concatenate((image1, image3, image2), axis=1)

# 이미지 출력
title = "dst"
cv2.imshow(title, image)

# 트랙바 2개 생성 (image1의 비율 0~100, image2의 비율 0~100)
cv2.createTrackbar('image1', title, 0, 100, onchange)
cv2.createTrackbar('image2', title, 0, 100, onchange)

cv2.waitKey(0)
cv2.destroyAllWindows()
