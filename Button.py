import pygame

#Button class
# -- to add buttons on the screen and evaluate actions on the buttons --
class Button():


    def __init__(self, x, y, img_idle, img_active, img, scale):
        self.x = x
        self.y = y
        self.img_idle = img_idle
        self.img_active = img_active
        self.scale = scale

        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos() #To get the mouse's position

        if self.rect.collidepoint(pos): #if the mouse is over the button
            
            self.__init__(self.x, self.y, self.img_idle, self.img_active, self.img_active, self.scale)

            if (pygame.mouse.get_pressed()[0] == 1 and self.clicked == False): #if button is clicked
                self.clicked = True
                action = True
        else:
            self.__init__(self.x, self.y, self.img_idle, self.img_active, self.img_idle, self.scale)

        if (pygame.mouse.get_pressed()[0] == 0): # if button is not clicked
            self.clicked = False

        surface.blit(self.img, (self.rect.x, self.rect.y))

        return action
