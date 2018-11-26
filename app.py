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
    image= scrshot(46, 179, 135, 200) #p1 chips
    x = chips(image)

    for i in range(1000):
        img= scrshot(46, 157, 135, 177) #p1 walk
        new = walk(img)
        
        image= scrshot(46, 179, 135, 200) #p1 chips
        y = chips(image)

        if (x-y)<0:
            print('P1 winns pot ', str(x)+' '+str(y))
            time.sleep(1)
            image= scrshot(46, 179, 135, 200) #p1 chips
            x = chips(image)
            y = chips(image)
            #print(str(x)+' '+str(y))
        else:
            if  new in ['Call', 'PostSB', 'PostBB', 'Raise', 'Ralse', 'Bet']:
                #print('P1 ... '+new+' '+ str(x-y)+ ' ... '+str(x)+' '+str(y))
                print('P1 ... '+new+' '+ str(x-y))
                image= scrshot(46, 179, 135, 200) #p1 chips
                x = chips(image)
                #time.sleep(0.10)
            #elif x-y==0:
            elif new in ['Fold', 'Check', 'Muck']:
                #print('P1 ... '+new+' ... '+str(x)+' '+str(y))
                print('P1 ... '+new)
                time.sleep(0.60)

if __name__ == "__main__":
    main()


# from engine.processes import *
# scrshot(660, 1, 1, 1)