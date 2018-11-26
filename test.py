#%%
import cv2
import pickle
import numpy as np
import win32gui
import win32ui
from ctypes import windll
from PIL import Image

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

scrshot(46, 157, 135, 177)


