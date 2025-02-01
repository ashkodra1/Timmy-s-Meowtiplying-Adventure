import pygame

class Player:
    def __init__(self, game, pos, size):
        #super().__init__(game, 'player', pos, size)
        self.game=game
        self.flip=False
        self.action=''
        self.set_action('idle')

    #def update(self, tilemap, movement = (0,0)):
    def set_action(self,action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()


    def update(self, movement = (0,0)):
        #super().update(tilemap, movement = movement)

        #self.air_time += 1
        #if self.collisions['down']:
        #    self.air_time=0
        
        # if self.air_time > 4:           #jump priority over run
        #     self.set_action('jump')

        if movement[0] > 0:    #we flip the image if it's facing left 
            self.flip = False
        if movement[0] < 0:
            self.flip=True

        if movement[0] !=0:
            self.set_action('run')
        else:
            self.set_action('idle')


    def render(self,surf):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        #self.animation.img().fill((255,0,0),special_flags= pygame.BLENDMODE_ADD) #this acts like a multiply layer