#%%

import shutil
from processes import *
import time
import os


model_nom, res_nom, index_nom = lern_model('nom')
knn_nom = cv2.ml.KNearest_create()
knn_nom.train(model_nom,cv2.ml.ROW_SAMPLE,res_nom)

model_suit, res_suit, index_suit = lern_model('suit')
knn_suit = cv2.ml.KNearest_create()
knn_suit.train(model_suit,cv2.ml.ROW_SAMPLE,res_suit)

def board_pos(pos, name):
    if name == 'board_nom':
        knn = knn_nom
        index = index_nom
    else:
        knn = knn_suit
        index = index_suit
    
    img = scrshot(pos, name)
    ret, results, neighbours, dist = check_image(img, knn)
    # print(ret, results, neighbours, dist)
    r = (index[int(ret)][1][0])[:1]
    if r == '1':
        r = '10'

    return r, dist

def board(pos):
    if pos == 'flop':
        res = []
        nom, dist = board_pos('flop1', 'board_nom')
        if dist[0][0] == 0:

            suit, dist = board_pos('flop1', 'board_suit')
            res.append(nom+suit)
            
            nom, dist = board_pos('flop2', 'board_nom')
            suit, dist = board_pos('flop2', 'board_suit')
            res.append(nom+suit)

            nom, dist = board_pos('flop3', 'board_nom')
            suit, dist = board_pos('flop3', 'board_suit')
            res.append(nom+suit)
        
        return res
    elif pos == 'turn':
        res = []
        nom, dist = board_pos('turn', 'board_nom')
        if dist[0][0] == 0:
            suit, dist = board_pos('turn', 'board_suit')
            res.append(nom+suit)
        return res

    elif pos == 'river':
        res = []
        nom, dist = board_pos('river', 'board_nom')
        if dist[0][0] == 0:
            suit, dist = board_pos('river', 'board_suit')
            res.append(nom+suit)
        return res

card = board('flop')
#%%
print(card[0])

# bb = ['flop', 'turn', 'river']
# for x in range(500):
#     for b in bb:
#         card = board(b)
#         if len(card) != 0:
#             print(card)
#             bb.remove(b)
#     time.sleep(0.5)