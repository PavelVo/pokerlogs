import pyscreenshot as ImageGrab
from PIL import Image
import PIL
import pytesseract
import cv2
import os
from operator import itemgetter
import numpy as np
import pickle
import time
import math, operator
import functools
from engine.processes import get_vector
from engine.processes import scrshot



# def new_walk_model(names):
#     tm = []
#     for num_x in names:
#         for num_xx in num_x[1]:
#             tm.append(num_xx)
#     dist = list(set(tm))

#     ndist = {}
#     i=0
#     for ts in dist:
#         ndist[ts] = i
#         i=i+1

#     l=[]
#     for a in names:
#         way = a[0]
#         name = a[1]
#         img = cv2.imread(way)
#         hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#         hsv_pt = np.array([ 0,  0, 120], dtype='uint8')
#         hsv_min = (hsv_pt * 0.01).astype('uint8')
#         hsv_max = (hsv_pt - 1).astype('uint8')
#         result = cv2.inRange(hsv_img, hsv_min, hsv_max)
#         cv2.imwrite('output.png', result)
#         img = cv2.imread('output.png')
#         #img = result
#         imgx = np.invert(np.array(img, dtype='uint8'))
#         image = cv2.cvtColor(imgx, cv2.COLOR_BGR2GRAY)
#         ret, thresh = cv2.threshold(image, 200,255,0)

#         _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

#         for cnt, n in zip(contours, name):
#             rect = cv2.minAreaRect(cnt)
#             box = cv2.boxPoints(rect)
#             box = np.int0(box)
#             area = int(rect[1][0]*rect[1][1])
#             if area > 10:
#                 img = cv2.drawContours(img, [box], 0, (0,255,0), 1)
#                 x, y, width, height = cv2.boundingRect(cnt)
#                 roi = thresh[y:y+height, x:x+width]

#                 j = ndist[n]

#                 img = cv2.resize(roi,(10,10))
#                 img = img.reshape((1,100))
#                 l.append([[img], [n], [j]])

#     res=[]
#     for ll in l:
#         res.append(ll[2])
#     res = np.array(res).astype(np.float32)

#     model = []
#     for mm in l:
#         m = mm[0][0][0].astype(np.float32)
#         model.append(m)
#     model = np.array(model)


#     lst = {}
#     for nl in l:
#         lst[nl[2][0]] = nl[1][0]
        
#     names_list = []
#     for n_l in names:
#         names_list.append(n_l[1])
    
#     return model, res, lst, names_list


def create_l(l, image, ids, name):
    img = get_vector(image)
    l.append([[ids], [img], [name]])
    return l

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

def create_model(image, name, model_name, new=True):
    if new==True:
        ids = 0
        new = []
        new = create_l(new, image, ids, name)
        os.makedirs('models/%s'%model_name)
        with open ('models/%s/model_%s.pickle'%(model_name, model_name), 'wb') as f:
            pickle.dump(new, f)
        print('create new model at models/%s/model_%s.pickle'%(model_name, model_name))
    else:
        with open('models/%s/model_%s.pickle'%(model_name, model_name), 'rb') as f:
            new = pickle.load(f)
        ids = new[-1][0][0] + 1
        new = create_l(new, image, ids, name)
        with open ('models/%s/model_%s.pickle'%(model_name, model_name), 'wb') as f:
            pickle.dump(new, f)
        print('add to model at models/%s/model_%s.pickle'%(model_name, model_name))

def save_image(p, act):
    img = scrshot(p, act)
    new = get_vector(img)
    arr_lst = [sum(new[0])]
    os.makedirs('img/%s'%p)
    while len(os.listdir('img/'+p))<100:
        img = scrshot(p, act)
        new = get_vector(img)
        if sum(new[0]) not in arr_lst:
            arr_lst.append(sum(new[0]))
            img.save('img/'+p+'/image_'+str(sum(new[0]))+'.png')
            print(p+' save to file '+str(sum(new[0])))
        time.sleep(1)
    print(p+' .......save compleat')
