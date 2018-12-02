#%%
from engine.processes import *
from models.data import *
# image = scrshot(80, 157, 135, 195) # empty
# l = create_model(image, 'empty', 'empty')
# image

image = scrshot(80, 157, 135, 195) # empty

# empty = lern_model('empty')
check_image(image, empty)
image

mage= scrshot(46, 179, 135, 200) #p1 chips
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



