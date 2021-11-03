import cv2


# 트랙바 콜백 함수 호출
def onChange(value):
    th1 = cv2.getTrackbarPos('th1', title)
    th2 = cv2.getTrackbarPos('th2', title)

    # 임계값 th1, th2에 따라 캐니 에지 수행
    edge = cv2.Canny(gray_image, th1, th2)
    cv2.imshow("canny edge", edge)


image = cv2.imread("images/cannay_tset.jpg", cv2.IMREAD_COLOR)  # 이미지 읽기
th1, th2 = 50, 50  # th1, th2 초기화
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환

title = 'canny edge'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)  # 윈도우 생성
cv2.createTrackbar("th1", title, th1, 255, onChange)  # 트랙바1 생성
cv2.createTrackbar("th2", title, th2, 255, onChange)  # 트랙바2 생성
cv2.waitKey(0)
