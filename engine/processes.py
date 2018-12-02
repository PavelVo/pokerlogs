import cv2
import pickle
import numpy as np
import win32gui
import win32ui
from ctypes import windll
from PIL import Image

with open('models/chips/model.pickle', 'rb') as f:
    model = pickle.load(f)
with open('models/chips/answer.pickle', 'rb') as f:
    answer = pickle.load(f)
    
    
knn = cv2.ml.KNearest_create()
knn.train(model,cv2.ml.ROW_SAMPLE,answer)

def chips(image):
    img = np.array(image)
    # image.save('img/tmp/input.png')
    # img = cv2.imread('img/tmp/input.png')
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image, 100,255,0)

    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
    l=[]
    n=[]
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        area = int(rect[1][0]*rect[1][1])
        if area > 30:
            img = cv2.drawContours(img, [box], 0, (255,0,0), 1)
            x, y, width, height = cv2.boundingRect(cnt)
            roi = thresh[y:y+height, x:x+width]
            l.append(roi)

            roismall = cv2.resize(roi,(10,10))
            num = roismall.reshape((1,100))
            newcomer = num.astype(np.float32)

            ret, results, neighbours, dist = knn.findNearest(newcomer, 1)
            n.append(str(int(ret)))
    n = int("".join(map(str, n)))
    return n

with open('models/walk/model_walk.pickle', 'rb') as f:
    model_wolk = pickle.load(f)
with open('models/walk/result_walk.pickle', 'rb') as f:
    result_walk = pickle.load(f)
with open('models/walk/convert_walk.pickle', 'rb') as f:
    convert_walk = pickle.load(f)
with open('models/walk/names_list.pickle', 'rb') as f:
    names_list = pickle.load(f)

knn_walk = cv2.ml.KNearest_create()
knn_walk.train(model_wolk,cv2.ml.ROW_SAMPLE, result_walk)

def walk(image):
    img = np.array(image)
    # image.save('img/tmp/in_tmp.png')
    # img = cv2.imread('img/tmp/in_tmp.png')

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_pt = np.array([ 0,  0, 120], dtype='uint8')
    hsv_min = (hsv_pt * 0.01).astype('uint8')
    hsv_max = (hsv_pt - 1).astype('uint8')
    result = cv2.inRange(hsv_img, hsv_min, hsv_max)
    cv2.imwrite('img/tmp/output_tmp.png', result)
    img = cv2.imread('img/tmp/output_tmp.png')
    imgx = np.invert(np.array(img, dtype='uint8'))
    image = cv2.cvtColor(imgx, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image, 200,255,0)

    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
    l=[]
    n=[]
    f = []
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        area = int(rect[1][0]*rect[1][1])
        if area > 10:
            img = cv2.drawContours(img, [box], 0, (0,255,0), 1)
            x, y, width, height = cv2.boundingRect(cnt)
            roi = thresh[y:y+height, x:x+width]
            l.append(roi)

            roismall = cv2.resize(roi,(10,10))
            num = roismall.reshape((1,100))
            newcomer = num.astype(np.float32)

            ret, results, neighbours, dist = knn_walk.findNearest(newcomer, 1)
            n.append(ret)


    for xx in n:
        s = convert_walk[int(xx)]
        f.append(s)
    ff = "".join(map(str, f))
    ff
    
    if ff in names_list:
        return ff


def scrshot(crop_left, crop_top, crop_right, crop_bot):

    hwnd = win32gui.FindWindow('PokerStarsTableFrameClass', None)

    left, top, right, bot = win32gui.GetWindowRect(hwnd)
  
    w = right - left
    h = bot - top
    

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    im = im.crop((crop_left, crop_top, crop_right, crop_bot))
    return im