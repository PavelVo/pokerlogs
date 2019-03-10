#%%
from processes import *
import os
import time


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

def save_new_images(folder_name, scrshot_val1, scrshot_v2):
    if not os.path.exists('img/'+folder_name):
        os.makedirs('img/'+folder_name)
    
    for x in range(500):
            
        if len(os.listdir('img/'+folder_name)) == 0:
            new_img1 = scrshot(scrshot_val1, scrshot_v2)
            new_img1.save('img/'+folder_name+'/input1.png')
        
        nom_arr = array_list(folder_name)

        new_img = scrshot(scrshot_val1, scrshot_v2)
        
        if in_array(get_vector(new_img), nom_arr) == False:
            new_img.save('img/'+folder_name+'/input'+str(n(folder_name))+'.png')
            nom_arr = array_list(folder_name)
        time.sleep(1)