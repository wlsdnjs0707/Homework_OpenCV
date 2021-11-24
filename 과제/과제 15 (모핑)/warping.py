import numpy as np, cv2

def morphing():
    h, w = image.shape[:2]
    dst = np.zeros((h, w), image.dtype)
    ys = np.arange(0, image.shape[0], 0.1)
    xs = np.arange(0, image.shape[1], 0.1)

    x1, x10 = pt1[0], pt1[0]*10
    ratios1 = xs / x1
    ratios1[x10:] = (w - xs[x10:]) / (w-x1)

    y1, y10 = pt1[1], pt1[1]*10
    ratios2 = ys / y1
    ratios2[y10:] = (h - ys[y10:]) / (h-y1)

    dxs = xs + ratios1 * (pt2[0] - pt1[0])
    xs, dxs = xs.astype(int), dxs.astype(int)

    dys = ys + ratios2 * (pt2[1] - pt1[1])
    ys, dys = ys.astype(int), dys.astype(int)

    ym, xm = np.meshgrid(ys, xs)
    dym, dxm = np.meshgrid(dys, dxs)
    dst[dym, dxm] = image[ym, xm]
    cv2.imshow("image", dst)

def onMouse(event, x, y, flags, param):
    global pt1, pt2
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x, y)                               # 드래그 시작 좌표
    elif event == cv2.EVENT_LBUTTONUP:
        pt2 = (x, y)                               # 드래그 종료 좌표
        morphing()                                 # 드래그 종료 시 워핑 변환 수행
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        pt1 = pt2 = (-1, -1)
        cv2.imshow("image", image)                 # 오른쪽 버튼 더블 클릭 시 원복

image = cv2.imread('images/warp.jpg', cv2.IMREAD_GRAYSCALE)

pt1 = pt2 = (-1, -1)
cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)          # 마우스 콜백 함수 등록
cv2.waitKey(0)
