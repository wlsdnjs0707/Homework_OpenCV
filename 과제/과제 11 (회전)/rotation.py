import numpy as np
import cv2
import math

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def onMouse(event, x, y, flags, param):
    global dst
    if event == cv2.EVENT_LBUTTONDOWN:
        dst = rotate_pt(dst, 20, center)
        cv2.imshow("image", dst)

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1]-1:
        x = x-1
    if y >= img.shape[0]-1:
        y = y-1
    P1 = float(img[y, x])
    P2 = float(img[y+0, x+1])
    P3 = float(img[y+1, x+0])
    P4 = float(img[y+1, x+1])
    alpha, beta = pt[1]-y, pt[0]-x
    M1 = P1 + alpha * (P3-P1)
    M2 = P2 + alpha * (P4-P2)
    P = M1 + beta * (M2-M1)
    return np.clip(P, 0, 255)

def scaling_bilinear(img, size):
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])

    dst = [[bilinear_value(img, (j/ratioX, i/ratioY)) for j in range(size[0])] for i in range(size[1])]

    return np.array(dst, img.dtype)

def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin = math.sin(radian)
    cos = math.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x, y = np.add((x, y), pt)
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, (x, y))

    return dst

image = cv2.imread("images/10.jpg", cv2.IMREAD_GRAYSCALE)
image = scaling_bilinear(image, (214, 159))
center = np.divmod(image.shape[::-1], 2)[0]
dst = rotate_pt(image, 20, center)
cv2.imshow("image", dst)
cv2.setMouseCallback("image", onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
