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

    # cv2.imwrite('tst.png', img)
    # return
    
    for xx in n:
        s = convert_walk[int(xx)]
        f.append(s)
    ff = "".join(map(str, f))
    ff
    
    if ff in names_list:
        return ff

def scrshot(p, act):
    
    if act == 'walk':
        if p == 'p1':
            crop_left = 46
            crop_top = 157
            crop_right = 135
            crop_bot = 177
            # img= scrshot(46, 157, 135, 177) #p1 walk
        elif p == 'p2':
            crop_left = 350
            crop_top = 90
            crop_right = 435
            crop_bot = 110
            # img= scrshot(350, 90, 435, 110) #p2 walk
        elif p == 'p3':
            crop_left = 673
            crop_top = 157
            crop_right = 762
            crop_bot = 176
            # img= scrshot(673, 157, 762, 176) #p3 walk
        elif p == 'p4':
            crop_left = 675
            crop_top = 329
            crop_right = 767
            crop_bot = 348
            # img= scrshot(675, 329, 767, 348) #p4 walk
        elif p == 'p5':
            crop_left = 374
            crop_top = 425
            crop_right = 465
            crop_bot = 444
            # img= scrshot(374, 425, 465, 444) #p5 walk
        elif p == 'p6':
            crop_left = 46
            crop_top = 329
            crop_right = 135
            crop_bot = 348
            # img= scrshot(46, 329, 135, 348) #p6 walk
    
    elif act == 'chips':
        if p == 'p1':
            crop_left = 50
            crop_top = 179
            crop_right = 135
            crop_bot = 200
            # img= scrshot(46, 179, 135, 200) #p1 chips
        elif p == 'p2':
            crop_left = 347
            crop_top = 113
            crop_right = 435
            crop_bot = 131
            # img= scrshot(347, 113, 435, 131) #p2 chips
        elif p == 'p3':
            crop_left = 680
            crop_top = 179
            crop_right = 765
            crop_bot = 198
            # img= scrshot(680, 179, 765, 198) #p3 chips
        elif p == 'p4':
            crop_left = 680
            crop_top = 351
            crop_right = 765
            crop_bot = 369
            # img= scrshot(680, 351, 765, 369) #p4 chips
        elif p == 'p5':
            crop_left = 378
            crop_top = 447
            crop_right = 465
            crop_bot = 465
            # img= scrshot(378, 447, 465, 465) #p5 chips
        elif p == 'p6':
            crop_left = 46
            crop_top = 351
            crop_right = 135
            crop_bot = 369
            # img= scrshot(46, 351, 135, 369) #p6 chips
    elif act == 'hand':
        crop_left = 46
        crop_top = 53
        crop_right = 140
        crop_bot = 68
        # img = scrshot(64, 53, 140, 68) # hand

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

def get_vector(image):
    img = np.array(image)
    img = cv2.resize(img,(10,10))
    img = img.reshape((1,300))
    img = img.astype(np.float32)
    return img

def check_image(image, knn):
    img = get_vector(image)
    ret, results, neighbours, dist = knn.findNearest(img, 1)
    return ret, results, neighbours, dist

def lern_model(model_name):
    with open('models/%s/model_%s.pickle'%(model_name, model_name), 'rb') as f:
        l = pickle.load(f)
    
    model = []
    for mm in l:
        m = mm[1][0][0].astype(np.float32)
        model.append(m)
    model = np.array(model)

    res=[]
    for rr in l:
        res.append(rr[0])
    res = np.array(res).astype(np.float32)

    index=[]
    for i in l:
        index.append([i[0], i[2]])

    return model, res, index

model_p1, res_p1, index_p1 = lern_model('walk_p1')
knn_p1 = cv2.ml.KNearest_create()
knn_p1.train(model_p1,cv2.ml.ROW_SAMPLE,res_p1)

model_p2, res_p2, index_p2 = lern_model('walk_p2')
knn_p2 = cv2.ml.KNearest_create()
knn_p2.train(model_p2,cv2.ml.ROW_SAMPLE,res_p2)

model_p3, res_p3, index_p3 = lern_model('walk_p3')
knn_p3 = cv2.ml.KNearest_create()
knn_p3.train(model_p3,cv2.ml.ROW_SAMPLE,res_p3)

model_p4, res_p4, index_p4 = lern_model('walk_p4')
knn_p4 = cv2.ml.KNearest_create()
knn_p4.train(model_p4,cv2.ml.ROW_SAMPLE,res_p4)

model_p5, res_p5, index_p5 = lern_model('walk_p5')
knn_p5 = cv2.ml.KNearest_create()
knn_p5.train(model_p5,cv2.ml.ROW_SAMPLE,res_p5)

model_p6, res_p6, index_p6 = lern_model('walk_p6')
knn_p6 = cv2.ml.KNearest_create()
knn_p6.train(model_p6,cv2.ml.ROW_SAMPLE,res_p6)

def walk2(p, act):
    if act == 'walk':
        if p == 'p1':
            knn = knn_p1
            index = index_p1
        elif p == 'p2':
            knn = knn_p2
            index = index_p2
        elif p == 'p3':
            knn = knn_p3
            index = index_p3
        elif p == 'p4':
            knn = knn_p4
            index = index_p4
        elif p == 'p5':
            knn = knn_p5
            index = index_p5
        elif p == 'p6':
            knn = knn_p6
            index = index_p6
        
        img= scrshot(p, act)
        # img = Image.open('img/p2/postBB.png')
        ret, results, neighbours, dist = check_image(img, knn)
        if dist[0][0] == 0:
            return (index[int(ret)][1][0])
    elif act == 'chips':
        img= scrshot(p, act)
        return chips(img)