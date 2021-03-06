#%%
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
from processes import get_vector
from processes import scrshot


def create_l(l, image, ids, name):
    img = get_vector(image)
    l.append([[ids], [img], [name]])
    return l

def create_model(model_name): #must to be like img folder
    # if new==True:
    if not os.path.exists('models/'+model_name):
        os.makedirs('models/'+model_name)
    
    ids = 0
    new = []
    
    for img_name in os.listdir('img/'+model_name):
        image = Image.open('img/'+model_name+'/'+img_name)
        name = img_name[:-4]
        if len(new)==0:
            new = create_l(new, image, ids, name)
            with open ('models/%s/model_%s.pickle'%(model_name, model_name), 'wb') as f:
                pickle.dump(new, f)
        else:
            with open('models/%s/model_%s.pickle'%(model_name, model_name), 'rb') as f:
                new = pickle.load(f)
            ids = new[-1][0][0] + 1
            new = create_l(new, image, ids, name)
            with open ('models/%s/model_%s.pickle'%(model_name, model_name), 'wb') as f:
                pickle.dump(new, f)
    print('create new model '+model_name+' comleat')

create_model('suit')
# ---------------------------------------------
# old code!!!!!

# def continium_model(names):
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
    
#     with open ('models/walk/model_walk.pickle', 'wb') as f:
#         pickle.dump(model, f)
#     with open ('models/walk/result_walk.pickle', 'wb') as f:
#         pickle.dump(res, f)
#     with open ('models/walk/convert_walk.pickle', 'wb') as f:
#         pickle.dump(lst, f)
#     with open ('models/walk/names_list.pickle', 'wb') as f:
#         pickle.dump(names_list, f)
    
#     print('models sevd to models/walk')
# ---------------------------------------------------------------

#%%
