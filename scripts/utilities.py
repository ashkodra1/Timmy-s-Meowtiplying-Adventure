import pygame
import os

IMAGE_PATH = 'data/images/'

#Loads a single image
def load_image(path):
    #Ignores files that generate from the Mac
    if '.DS_Store' in path:
        pass
    else:
        #convert_alpha() deals with the transparent background of images!
        image = pygame.image.load(IMAGE_PATH + path).convert_alpha()
        return image
    

#Loads multiple images in a folder (for animation)
#If ever it's a side view i can add clouds
def load_images(path):
    list_imgs=[]
    for img_name in sorted(os.listdir(IMAGE_PATH+path)):  #Gives all images from the specific path
        if '.DS_Store' in path:
            pass
        else:
            list_imgs.append(load_image(path + '/' + img_name))
    return list_imgs


#Class to animate sprites
class Animation:
    def __init__(self,imgs,img_dur=5,loop=True):
        self.imgs = imgs
        self.loop = loop
        self.img_dur=img_dur
        self.done =False
        self.frame=0    #Frame of the game

    #Copy constructor pretty much
    def copy(self):
        return Animation(self.imgs,self.img_dur,self.loop)
    
    def update(self):
        if self.loop:
            #modulos will create the looping
            self.frame = (self.frame+1) % (self.img_dur* len(self.imgs))
        else:
            #-1 since we start at 0
            self.frame = min(self.frame+1,self.img_dur*len(self.imgs)-1)
            if self.frame >= self.img_dur*len(self.imgs)-1:
                self.done=True

    #switches the image for the frame of the anim
    def img(self):
        return self.images[int(self.frame/self.img_dur)]
