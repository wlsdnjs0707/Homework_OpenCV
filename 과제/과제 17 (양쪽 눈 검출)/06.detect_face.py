import cv2, numpy as np

def preprocessing(no):  # 검출 전처리
    image1 = cv2.imread('images/face/%2d.jpg' % no, cv2.IMREAD_COLOR)
    image2 = cv2.imread('images/face/%2d.jpg' % no, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환
    gray = cv2.equalizeHist(gray)  # 히스토그램 평활화
    return image1, image2, gray

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")  # 정면 검출기
lefteye_cascade = cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")  # 왼쪽 눈 검출기
righteye_cascade = cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")  # 오른쪽 눈 검출기
image1, image2, gray = preprocessing(34)  # 전처리

faces = face_cascade.detectMultiScale(gray, 1.1, 2, 0, (100, 100))  # 얼굴 검출

if faces.any():
    x, y, w, h = faces[0]
    count = 0
    face_image = image1[y:y + h, x:x + w]  # 얼굴 영역 영상 가져오기
    lefteye = lefteye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (25, 20))  # 눈 검출 수행
    righteye = righteye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (25, 20))  # 눈 검출 수행

    if len(lefteye) == 1:  # 눈 사각형이 검출되면
        for ex, ey, ew, eh in lefteye:
            center = (x + ex + ew // 2, y + ey + eh // 2)
            cv2.circle(image1, center, 10, (0, 255, 0), 2)  # 눈 중심에 원 그리기
    else:
        print("눈 미검출")

    if len(righteye) >= 1:  # 눈 사각형이 검출되면
        for ex, ey, ew, eh in righteye:
            if count == 1:
                center = (x + ex + ew // 2, y + ey + eh // 2)
                cv2.circle(image2, center, 10, (0, 255, 0), 2)  # 눈 중심에 원 그리기
            else:
                count += 1
    else:
        print("눈 미검출")

    cv2.rectangle(image1, faces[0], (255, 0, 0), 2)  # 얼굴 검출 사각형 그리기
    cv2.rectangle(image2, faces[0], (255, 0, 0), 2)  # 얼굴 검출 사각형 그리기
    cv2.imshow("image1", image1)
    cv2.imshow("image2", image2)

else:
    print("얼굴 미검출")
cv2.waitKey(0)
