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

def main():
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
                    old_res = x[p]
                    new_res = walk2(p,'chips') 
                    res =  old_res - new_res
                    x[p] = new_res
                    pp = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
                    pp.remove(p)
                    print(p+' ... '+ wlc)
                    # print(old_res, new_res)
                else:
                    old_res = x[p]
                    new_res = walk2(p,'chips') 
                    res =  old_res - new_res
                    x[p] = new_res
                    pp = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']
                    pp.remove(p)
                    print(p+' ... '+ wlc+' ... '+str(res))
                    # print(old_res, new_res)
        time.sleep(0.5)

# def main():
#     image= scrshot(46, 179, 135, 200) #p1 chips
#     x = chips(image)

#     for i in range(1000):
#         img= scrshot(46, 157, 135, 177) #p1 walk
#         new = walk(img)
        
#         image= scrshot(46, 179, 135, 200) #p1 chips
#         y = chips(image)

#         if (x-y)<0:
#             print('P1 winns pot ', str(x)+' '+str(y))
#             time.sleep(1)
#             image= scrshot(46, 179, 135, 200) #p1 chips
#             x = chips(image)
#             y = chips(image)
#             #print(str(x)+' '+str(y))
#         else:
#             if  new in ['Call', 'PostSB', 'PostBB', 'Raise', 'Ralse', 'Bet']:
#                 #print('P1 ... '+new+' '+ str(x-y)+ ' ... '+str(x)+' '+str(y))
#                 print('P1 ... '+new+' '+ str(x-y))
#                 image= scrshot(46, 179, 135, 200) #p1 chips
#                 x = chips(image)
#                 #time.sleep(0.10)
#             #elif x-y==0:
#             elif new in ['Fold', 'Check', 'Muck']:
#                 #print('P1 ... '+new+' ... '+str(x)+' '+str(y))
#                 print('P1 ... '+new)
#                 time.sleep(0.60)

if __name__ == "__main__":
    main()