#%%

import shutil
from engine.processes import *
import time
import os
from models.create_model import *


continium_model('nom')


# scrshot('flop1', 'board_nom')
# def in_array(array, arrays):
#     for ars in arrays:
#         if np.array_equal(array, ars) == True:
#             return True
#     return False

# def array_list(source):
#     nom_arr=[]
#     nom_list = os.listdir('img/'+source)
#     for nl in nom_list:
#         img_nom = get_vector(Image.open('img/'+source+'/'+nl))
#         nom_arr.append(img_nom)
#     return nom_arr

# def n(source):
#     n=[]
#     for l in os.listdir('img/'+source):
#         n.append(int(l.replace('input','').replace('.png','')))
#     return max(n)+1

# for x in range(100):
#     if len(os.listdir('img/nom')) == 0:
#         new_img = scrshot('flop1', 'board_nom')
#         new_img.save('img/nom/input1.png')
    
#     if len(os.listdir('img/suit')) == 0:
#         new_img1 = scrshot('flop1', 'board_suit')
#         new_img1.save('img/suit/input1.png')
    
#     nom_arr = array_list('nom')
#     nom_arr1 = array_list('suit')

    
#     for st in ['flop1', 'flop2', 'flop3','turn','river']:
#         new_img = scrshot(st, 'board_nom')
#         # print(in_array(get_vector(new_img), nom_arr))
#         if in_array(get_vector(new_img), nom_arr) == False:
#             new_img.save('img/nom/input'+str(n('nom'))+'.png')
#             nom_arr = array_list('nom')
#         time.sleep(1)

#     for st in ['flop1', 'flop2', 'flop3','turn','river']:
#         new_img1 = scrshot(st, 'board_suit')
#         # print(in_array(get_vector(new_img), nom_arr))
#         if in_array(get_vector(new_img1), nom_arr1) == False:
#             new_img1.save('img/suit/input'+str(n('suit'))+'.png')
#             nom_arr1 = array_list('suit')
#         time.sleep(1)
#     time.sleep(1)