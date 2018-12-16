#%%
import shutil
import os
import numpy as np
from PIL import Image
import cv2
import pickle
import numpy as np
import win32gui
import win32ui
from ctypes import windll

import pyscreenshot as ImageGrab
from PIL import Image
import PIL
import pytesseract
from operator import itemgetter
import os
import time
import math, operator
import functools

from engine.processes import *
from models.data import *
import time
from models.create_model import *
from img.imp_list import *




pp = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
x =  {'p1':walk2('p1','chips')
    ,'p2':walk2('p2','chips')
    ,'p3':walk2('p3','chips')
    ,'p4':walk2('p4','chips')
    ,'p5':walk2('p5','chips')
    ,'p6':walk2('p6','chips')
    }
y=x
image = scrshot('p', 'hand')
x_hand = get_vector(scrshot('p', 'hand'))

while True:
    y_hand = get_vector(scrshot('p', 'hand'))
    if not np.array_equal(x_hand, y_hand):
        print('new hand')
        x_hand=y_hand
    for p in pp:
        wlc = walk2(p, 'walk')
        if wlc != None:
            if wlc in ['fold', 'check', 'muck']:
                res = x[p] - walk2(p,'chips') 
                x['p6'] = res
                print(p+' ... '+ wlc)
                pp = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
                pp.remove(p)
            else:       
                res = x[p] - walk2(p,'chips') 
                x['p6'] = res
                print(p+' ... '+ wlc+' ... '+str(res))
                pp = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
                pp.remove(p)
    time.sleep(0.5)

# nn.remove('p1')
# x['p6'] = 10
# image = scrshot('p', 'hand')
# image = Image.open('img/status/ts.png')
# x = get_vector(scrshot('p', 'hand'))
# while True:
#     y = get_vector(scrshot('p', 'hand'))
#     if not np.array_equal(x,y):
#         print('new hand')
#         nn = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
#         for n in nn:
#             x = walk2(n, 'walk')
#             if x != None:
#             print(n+' '+ x)

#         x = get_vector(scrshot('p', 'hand'))
#     time.sleep(0.5)


# status('p4', 'chips')
# walk2('p3', 'chips')
# p='p5'
# pp = scrshot(p, 'chips')
# pp.save('img/status/'+p+'/ts.png')
# pp
# nn = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
# while True:
#     for n in nn:
#         x = walk2(n, 'walk')
#         if x != None:
#             print(n+' '+ x)    
#     time.sleep(1)

# image = scrshot(64, 53, 140, 68) # hand
# l = create_model(image, 'hand', 'hand')
# image

# image = scrshot(80, 157, 135, 195) # empty

# # empty = lern_model('empty')
# ret, results, neighbours, dist = check_image(image, empty)
# image

# img= scrshot('p3')
# img
# new = walk(img)
# new

# img= scrshot(46, 157, 135, 177) #p1 chips
# img= scrshot('p3')
# img
# new = walk(img)
# new

# save_image('p2')
# save_image('p4')
# save_image('p5')
# save_image('p6')

# print('start')
# names = img_p1()
# continium_model(names)


# nm = ('bet','fold','call','check','muck','postBB','postSB','raise')
# for xx in nm:
#     img = Image.open('img/p1/%s.png'%xx)
#     new = walk(img)
#     print(new)
    
# def m(p):
#     im = os.listdir('img/'+p)[0]
#     im_name = os.listdir('img/'+p)[0][:-4]
#     img = Image.open('img/'+p+'/'+im)
#     model_name = 'walk_'+p
#     create_model(img, im_name, model_name, new=True)
#     nm = os.listdir('img/'+p)[1:]
#     for n in nm:
#         img = Image.open('img/'+p+'/'+n)
#         im_name = n[:-4]
#         create_model(img, im_name, model_name, model_name)
# m('p6')

# with open('models/walk_p2/model_walk_p2.pickle', 'rb') as f:
#         l = pickle.load(f)
# l
# x = walk2('p1')
# nn = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
# while True:
#     for n in nn:
#         x = walk2(n)
#         if x != None:
#             print(n+' '+ x)    
#     time.sleep(1)

# def s_shot(p):
#     if p == 1:
#         return scrshot(46, 157, 135, 177) #p1 walk
#     elif p == 2:
#         return scrshot(350, 90, 435, 110) #p2 walk

# def walkin(p):
#     for nn in range(5000):
#         img = s_shot(p)
#         new = walk(img)
#         if new in ['Check', 'Call', 'Bet', 'PostBB', 'PostSB', 'Rais']:
#             return new+' p'+str(p)
#         time.sleep(1)


# shutil.rmtree('models/hand')
# image = scrshot(64, 53, 140, 68) # hand
# create_model(image, 'hand', 'hand')
# hand = lern_model('hand')
# p=[1,2]
# for x in range(500):
#     image = scrshot(64, 53, 140, 68) # hand
#     ret, results, neighbours, dist = check_image(image, hand)
#     if dist[0][0] > 0:
#         shutil.rmtree('models/hand')
#         create_model(image, 'hand', 'hand')
#         hand = lern_model('hand')
#         print('new hand')
#     else:
#         for pp in p:
#             res = walkin(pp)
#             print(res)
#     time.sleep(1)


# img= scrshot(675, 157, 767, 178) #p3 walk
# img.save('tst.png', 'PNG')
# y = get_vector(img)
# img
# np.array_equal(x,y)



