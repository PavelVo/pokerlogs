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
    image=ImageGrab.grab(bbox=(607,321,696,341)) # X1,Y1,X2,Y2
    x = chips(image)

    for i in range(100):
        img=ImageGrab.grab(bbox=(603,300,696,320)) # X1,Y1,X2,Y2
        new = walk(img)
        
        image=ImageGrab.grab(bbox=(607,321,696,341)) # X1,Y1,X2,Y2
        y = chips(image)

        if (x-y)<0:
            print('P1 winns pot ', str(x)+' '+str(y))
            time.sleep(1)
            image=ImageGrab.grab(bbox=(607,321,696,341)) # X1,Y1,X2,Y2
            x = chips(image)
            y = chips(image)
            #print(str(x)+' '+str(y))
        else:
            if  new in ['Call', 'PostSB', 'PostBB', 'Raise', 'Ralse', 'Bet']:
                #print('P1 ... '+new+' '+ str(x-y)+ ' ... '+str(x)+' '+str(y))
                print('P1 ... '+new+' '+ str(x-y))
                image=ImageGrab.grab(bbox=(607,321,696,341)) # X1,Y1,X2,Y2
                x = chips(image)
                #time.sleep(0.10)
            #elif x-y==0:
            elif new in ['Fold', 'Check', 'Muck']:
                #print('P1 ... '+new+' ... '+str(x)+' '+str(y))
                print('P1 ... '+new)
                time.sleep(0.60)

if __name__ == "__main__":
    main()