#%%

import shutil
from engine.processes import *
import time
import os


# def in_array(array, arrays):
#     for ars in arrays:
#         if np.array_equal(array, ars) == True:
#             return True
#         else:
#             return False

# def array_list():
#     nom_arr=[]
#     nom_list = os.listdir('img/nom')
#     for nl in nom_list:
#         img_nom = get_vector(Image.open('img/nom/'+nl))
#         nom_arr.append(img_nom)
#     return nom_arr

# n=1
# new_img = scrshot('flop1', 'board_nom')
# new_img.save('img/nom/input'+str(n)+'.png')
# nom_arr = array_list()

# for x in range(10):
#     new_img = scrshot('flop1', 'board_nom')
#     print(in_array(get_vector(new_img), nom_arr))
#     if in_array(get_vector(new_img), nom_arr) == False:
#         new_img.save('img/nom/input'+str(n)+'.png')
#         nom_arr = array_list()
#         n=n+1
#     time.sleep(5)

scrshot('flop1', 'board_nom')
def in_array(array, arrays):
    for ars in arrays:
        if np.array_equal(array, ars) == True:
            return True
    return False

def array_list(source):
    nom_arr=[]
    nom_list = os.listdir('img/'+source)
    for nl in nom_list:
        img_nom = get_vector(Image.open('img/'+source+'/'+nl))
        nom_arr.append(img_nom)
    return nom_arr

def n(source):
    n=[]
    for l in os.listdir('img/'+source):
        n.append(int(l.replace('input','').replace('.png','')))
    return max(n)+1

for x in range(100):
    if len(os.listdir('img/nom')) == 0:
        new_img = scrshot('flop1', 'board_nom')
        new_img.save('img/nom/input1.png')
    
    if len(os.listdir('img/suit')) == 0:
        new_img1 = scrshot('flop1', 'board_suit')
        new_img1.save('img/suit/input1.png')
    
    nom_arr = array_list('nom')
    nom_arr1 = array_list('suit')

    
    for st in ['flop1', 'flop2', 'flop3','turn','river']:
        new_img = scrshot(st, 'board_nom')
        # print(in_array(get_vector(new_img), nom_arr))
        if in_array(get_vector(new_img), nom_arr) == False:
            new_img.save('img/nom/input'+str(n('nom'))+'.png')
            nom_arr = array_list('nom')
        time.sleep(1)

    for st in ['flop1', 'flop2', 'flop3','turn','river']:
        new_img1 = scrshot(st, 'board_suit')
        # print(in_array(get_vector(new_img), nom_arr))
        if in_array(get_vector(new_img1), nom_arr1) == False:
            new_img1.save('img/suit/input'+str(n('suit'))+'.png')
            nom_arr1 = array_list('suit')
        time.sleep(1)
    time.sleep(1)


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
#     stage = 
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


