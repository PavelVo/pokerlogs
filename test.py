#%%

import shutil
from engine.processes import *
import time
import os


def in_array(array, arrays):
    for ars in arrays:
        if np.array_equal(array, ars) == True:
            return True
        else:
            return False

def array_list():
    nom_arr=[]
    nom_list = os.listdir('img/nom')
    for nl in nom_list:
        img_nom = get_vector(Image.open('img/nom/'+nl))
        nom_arr.append(img_nom)
    return nom_arr

# n=1
# new_img = scrshot('flop1', 'board_nom')
# new_img.save('img/nom/input'+str(n)+'.png')
# nom_arr = array_list()

for x in range(10):
    new_img = scrshot('flop1', 'board_nom')
    print(in_array(get_vector(new_img), nom_arr))
    if in_array(get_vector(new_img), nom_arr) == False:
        new_img.save('img/nom/input'+str(n)+'.png')
        nom_arr = array_list()
        n=n+1
    time.sleep(5)



# Image.open('img/nom/input1.png')
# image = scrshot('flop1', 'board_nom')
# image.save('img/nom/input1.png')

# y=[]
# x = get_vector(scrshot('flop1', 'board_nom'))
# y.append(x)
# x = get_vector(scrshot('flop2', 'board_nom'))
# y.append(x)
# x = get_vector(scrshot('flop3', 'board_nom'))
# y.append(x)

# x = get_vector(scrshot('flop1', 'board_nom'))








# np.array_equal(x,x2)

# n = 1
# image = scrshot('flop1', 'board_nom')
# image.save('img/nom/input'+str(n)+'.png')
# for x in range(5):
#     stage = ['flop1', 'flop2', 'flop3','turn','river']
#     i = 1
#     for s in stage:
#         image = scrshot(s, 'board_nom')
#         image.save('img/tmp/input'+str(i)+'.png')
#         i=i+1

#     tmp_list = os.listdir('img/tmp')
#     nom_list = os.listdir('img/nom')
#     q=0

#     for tl in tmp_list:
#         im_tmp = Image.open('img/tmp/'+tl)
#         for nl in nom_list:
#             im_nom = Image.open('img/nom/'+nl)
#             if im_nom==im_tmp:
#                 q = 1
#                 print()
#         if q==0:
#             n=n+1
#             im_tmp.save('img/nom/input'+str(n)+'.png')
#             nom_list = os.listdir('img/nom')
#             q=0





# image.save('img/nom/input2.png')


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


