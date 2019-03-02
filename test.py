#%%
<<<<<<< HEAD

# import shutil
# from engine.processes import *
# from models.data import *
# import time
# image = scrshot(64, 53, 140, 68) # hand
# l = create_model(image, 'hand', 'hand')
# image
=======
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

x =  {'p1':walk2('p1','chips')
        ,'p2':walk2('p2','chips')
        ,'p3':walk2('p3','chips')
        ,'p4':walk2('p4','chips')
        ,'p5':walk2('p5','chips')
        ,'p6':walk2('p6','chips')
        }
x
# im = scrshot('p1', 'chips')
# im
# chips(im)
# walk2('p1','chips')

# pp = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
# x =  {'p1':walk2('p1','chips')
#     ,'p2':walk2('p2','chips')
#     ,'p3':walk2('p3','chips')
#     ,'p4':walk2('p4','chips')
#     ,'p5':walk2('p5','chips')
#     ,'p6':walk2('p6','chips')
#     }
# y=x
# image = scrshot('p', 'hand')
# x_hand = get_vector(scrshot('p', 'hand'))
>>>>>>> origin/master

# while True:
#     y_hand = get_vector(scrshot('p', 'hand'))
#     if not np.array_equal(x_hand, y_hand):
#         print('new hand')
#         x_hand=y_hand
#     for p in pp:
#         wlc = walk2(p, 'walk')
#         if wlc != None:
#             if wlc in ['fold', 'check', 'muck']:
#                 res = x[p] - walk2(p,'chips') 
#                 x['p6'] = res
#                 print(p+' ... '+ wlc)
#                 pp = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
#                 pp.remove(p)
#             else:       
#                 res = x[p] - walk2(p,'chips') 
#                 x['p6'] = res
#                 print(p+' ... '+ wlc+' ... '+str(res))
#                 pp = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
#                 pp.remove(p)
#     time.sleep(0.5)



# img= scrshot('p3')
# img
# new = walk(img)
# new

<<<<<<< HEAD
# img= scrshot(350, 90, 435, 110) #p2 walk
# # img
# new = walk(img)
# new
# shutil.rmtree('models/hand')
# image = scrshot(64, 53, 140, 68) # hand
# create_model(image, 'hand', 'hand')
# hand = lern_model('hand')
# ret, results, neighbours, dist = check_image(image, hand)
# for x in range(50):
#     image = scrshot(64, 53, 140, 68) # hand
#     ret, results, neighbours, dist = check_image(image, hand)
#     if dist[0][0] > 0:
#         shutil.rmtree('models/hand')
#         create_model(image, 'hand', 'hand')
#         hand = lern_model('hand')
#         print('new hand')
#     print('last hand')
#     time.sleep(3)



=======
# save_image('p1', 'walk')

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

# names = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
# for name in names:
#     m(name)
# m('p1')
>>>>>>> origin/master

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


